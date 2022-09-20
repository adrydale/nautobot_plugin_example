from .. import common
from nautobot.extras.jobs import Job

# The datetime library gives us access to date and time functions.
from datetime import datetime

# This is the job grouping within the Nautobot UI.
name = common.ex_base_grouping_name

# This is the job being imported. We include "Job" in the class definition
# because our new class/Nautobot job will extend the built in functions that
# Nautobot Jobs have.
class Ex06_SchedulingJobs(Job):
  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 06 - Scheduling Jobs"
    # The first line of the description will be displayed but other lines will
    # only be displayed on job details.
    description = """
      Example job for a job that can be scheduled.

      Jobs by default will have has_sensitive_variables set to True. These jobs
      cannot be scheduled. Changing has_sensitive_variables to False will enable
      the job to be scheduled for the future once or on a recurring schedule.
    """

  def run(self, data, commit):
    self.log_info("Example job for scheduling.")

    # This job isn't intended to do anything else. In the web GUI, when running
    # this job a "Job Execution" section will be added allowing the user to
    # choose when the job is run. By default, the options are:
    #  - Once immediately
    #  - Once in the future
    #  - Recurring hourly
    #  - Recurring daily
    #  - Recurring weekly
    #  - Recurring custom (crontab syntax)
