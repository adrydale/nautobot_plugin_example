from .. import common

# Importing Job from nautobot.extras.jobs is required for any Nautobot job
from nautobot.extras.jobs import Job

# This import is to enable the user input variable(s)
from nautobot.extras.jobs import BooleanVar

# This is the import that is necessary to access Nautobot secrets
from nautobot.extras.models.secrets import Secret

# This is the job grouping within the Nautobot UI.
name = common.ex_base_grouping_name

# This is the job being imported.
class Ex04_AccessingSecrets(Job):
  var_display_secret = BooleanVar(
    default = False,
    description = """
      Display the example secret in the job result/output. It is NOT recommended
      to do this for any actual secret. Job result data is stored and accessable
      to authorized users in plain text.
    """,
    label = "Display example secret"
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 04 - Accessing Secrets"
    # The first line of the description will be displayed but other lines will
    # only be displayed on job details.
    description = """
      This example shows how to access Nautobot secrets.

      It is assumed that the Nautobot secret "example_secret_01" is already
      setup within Nautobot. Please refer to the Nautobot documentation for
      details on how to add a secret.

      Secrets were added in Nautobot version 1.2.0.
      https://nautobot.readthedocs.io/en/stable/core-functionality/secrets/
    """

  def run(self, data, commit):
    # This job shows how to access Nautobot secrets.

    self.log_info("Job start")

    # This will pull the secret from Nautobot
    try:
      secret = Secret.objects.get(slug="example_secret_01")
    except Secret.DoesNotExist:
      self.log_failure("Error: \"example_secret_01\" isn't setup.")
      return

    # The printed value of the secret is the secret NAME
    self.log_debug(f"The name of the secret object is: {secret}")
    # Get the raw value of the secret instead of the secret object
    val = secret.get_value()

    self.log_success("Secret value retreived!")
    self.log_debug(f"Secret value length is {len(val)}")

    if data.get("var_display_secret"):
      self.log_warning("REMINDER: You should not print secrets to job output.")
      self.log_success(f"The value is {val}")

    self.log_success("Job completed.")
