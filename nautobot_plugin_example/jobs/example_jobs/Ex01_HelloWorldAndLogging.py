from .. import common
from nautobot.extras.jobs import Job

# This is the job grouping within the Nautobot UI.
name = ex_base_grouping_name

# This is the job being imported. We include "Job" in the class definition
# because our new class/Nautobot job will extend the built in functions that
# Nautobot Jobs have.
class Ex01_HelloWorld(Job):
  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 01 - Hello World"
    # The first line of the description will be displayed but other lines will
    # only be displayed on job details.
    description = """
      Example job for a simple "Hello World" output
    """

  def run(self, data, commit):
    # This is a simple job that outputs "Hello world" to the job output/result
    # data. It also outlines several different logging levels
    self.log_info("Hello world!")

    # Basic logging options
    self.log("Default log")
    self.log_info("Informational log")
    self.log_debug("Debugging log")
    self.log_success("Success log")
    self.log_warning("Warning log")

    # This is an example of a failure log. It is commented out as a single
    # failure log will cause the job to report as failed. Refer to Example 02
    # for an example of a failure log. There is an option to cause the job to
    # fail.
    #self.log_failure("Failure log")
