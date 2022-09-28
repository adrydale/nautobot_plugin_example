from .. import common
from nautobot.extras.jobs import Job

# This will import the Meraki SDK in for the job. This must be included on the
# servers installed libraries or included in the plugin build (reference the
# pyproject.toml file in the root of this repo.
import meraki

# This is the import that is necessary to access Nautobot secrets
from nautobot.extras.models.secrets import Secret

# This is the job grouping within the Nautobot UI.
name = common.ex_base_grouping_name

# This is the job being imported. We include "Job" in the class definition
# because our new class/Nautobot job will extend the built in functions that
# Nautobot Jobs have.
class ExES01_ExternalSys_Meraki(Job):
  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example - External Systems - 01 - Meraki"
    # The first line of the description will be displayed but other lines will
    # only be displayed on job details.
    description = """
      Example job for interacting with an external system - Meraki.

      This job will hit the Meraki API and show the organziation IDs associated
      with the given token.

      **Requirement**: You MUST setup a secret called "meraki_org01_token" for
      this job to work properly.
    """

  def run(self, data, commit):
    self.log_info("Pulling Meraki token from secrets")

    # This will pull the secret from Nautobot. Alternatively, the Meraki SDK
    # will try to import an environment variable (MERAKI_DASHBOARD_API_KEY) if
    # none is specified. This is the Meraki perferred way but it does give any
    # script accessibility to the API key by just importing it.
    try:
      meraki_secret = Secret.objects.get(slug="meraki_org01_token")
      meraki_token = meraki_secret.get_value()
    except Secret.DoesNotExist:
      self.log_failure("Error: Secret \"meraki_org01_token\" doesn't exist.")
      return

    self.log_info("Setting up the Meraki Dashboard connection.")

    # This will create the connection to the Meraki dashboard. By default the
    # Meraki SDK is very verbose when accessing the dashboard so we'll quiet it
    # a bit with suppress_logging=True.
    dash = meraki.DashboardAPI(api_key=meraki_token, suppress_logging=True)

    # Grab the list of organizations for the API key. Iterate through them and
    # log the org name and ID.
    orgs = dash.organizations.getOrganizations()
    for org in orgs:
      org_name = org["name"]
      org_id = org["id"]
      self.log_success(f"Org found! Name: {org_name}, ID: {org_id}")

    self.log_info("Complete!")

    # From here, you can use the dashboard object as in any Python script. Use
    # the following as additional resources for exploring the Meraki Python SDK.
    # https://github.com/meraki/dashboard-api-python
    # https://developer.cisco.com/meraki/api/#!python-meraki/usage
