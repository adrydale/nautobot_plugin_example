from .. import common

# Importing Job from nautobot.extras.jobs is required for any Nautobot job.
from nautobot.extras.jobs import Job

# These imports are the type of inputs that are being used in this job.
from nautobot.extras.jobs import StringVar, ObjectVar

# Importing models allow us to work with/manipulate objects of these types
from nautobot.dcim.models import Site
from nautobot.extras.models import Status

# This is the job grouping within the Nautobot UI.
name = common.ex_base_grouping_name

# This is the job being imported.
class Ex05_CreatingSiteObjects(Job):
  # This will be a simple string for the site name
  site_name = StringVar(
    default = "Nautobot Examples - Example Site",
    description = "Name of the site to be created",
    label = "Site Name"
  )

  # Add a variable for the site status to user inputs. This is filtered to only
  # statuses that can be applied to sites.
  site_status = ObjectVar(
    description = "Set the configured status of the site",
    label = "Site status",
    model = Status,
    query_params = {"content_types": "dcim.site"},
    display_field = "name"
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 05 - Creating Site Objects"
    # The first line of the description will be displayed but other lines will
    #   only be displayed on job details.
    description = """
      This job will create a base site with the user inputted name.
    """

  # This will be run when the job starts.
  def run(self, data, commit):
    # Basic log
    self.log_info("Site creation job example")

    # Store the inputs and log them
    site_name = data.get("site_name")
    site_status = data.get("site_status")
    self.log_info(f"Site name: {site_name}")
    self.log_info(f"Site status: {site_status}")

    # Quick check to see if the site already exists
    try:
      # Check sites for sites with the same inputted name
      existing_site = Site.objects.get(name=site_name)

      # The above will either error out if there are no matches or it will
      # continue on to the next lines in this try block.
      error_msg = f"Error! The site \"{site_name}\" already exists!"
      self.log_failure(obj=existing_site, message = error_msg)

      # A return statement will stop further job processing. Because there was a
      # failure log, test_*() functions will not run but a post_run() would.
      return
    except Site.DoesNotExist:
      # This would mean that the site does not currently exist so we will
      # continue on with the rest of the job (pass)
      pass

    # This will actually create the site
    new_site = Site.objects.create(name=site_name, status=site_status)

    # With the new site created, we'll create a log with a hyperlinked reference
    # to the site object.
    self.log_success(obj=new_site, message=f"Site \"{site_name}\" created!")
