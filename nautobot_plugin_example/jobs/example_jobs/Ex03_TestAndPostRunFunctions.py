# Importing Job from nautobot.extras.jobs is required for any Nautobot job.
from nautobot.extras.jobs import Job
from nautobot.extras.jobs import BooleanVar

# This is the job grouping within the Nautobot UI.
name = "AD Example jobs"

# This is the job being imported.
class Ex03_TestAndPostRunFunctions(Job):
  # This example demonstrates the test_*() and post_run() functions. These are
  # run after the run() function in order to validate data/objects/state and
  # complete clean-ups or other efforts in the event that the run() function
  # fails.

  # Of note, test_*() functions are NOT run on job failure but the post_run()
  # function is.

  # This boolean var is used to raise an exception within the fun() function to
  # show that the test_*() and post_run() functions are still processed.
  var_induce_failure = BooleanVar(
    default = False,
    description = "Check this to induce a job failure/exception",
    label = "Create exception in run()"
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 03 - Test and post-run functions"
    # The first line of the description will be displayed but other lines will
    #   only be displayed on job details.
    description = """
      Demonstrate the test_*() and post_run() functions.

      These functions are run after the run() function in order to validate the
      data/objects/state and complete clean-ups or other efforts in the event
      that the run() function.

      Of note, test_*() functions are NOT run on job failure but the post_run()
      function is.
    """

  def run(self, data, commit):
    self.log_info("Job start - Ex03")

    induce_failure = data.get('var_induce_failure')
    self.log_info(f"Checkbox to induce a failure was set to {induce_failure}")
    if induce_failure:
      self.log_debug("The induce failure box was checked; raising exception.")
      raise ValueError("User requested to induce a failure (intentional).")
    else:
      self.log_success("The induce failure checkbox was not checked.")

    self.log_info("Job complete")

  # All test_* functions will be implicitly called *after* the run() function
  # ONLY if there is not a failure. If there is a failure, these are skipped.
  # These are processed in the order they are defined.
  # test_ functions are OPTIONAL
  def test_02(self):
    msg = "Test02 function run"
    self.log(msg)

  def test_01(self):
    msg = "Test01 function run"
    self.log_debug(msg)

  # Finally, the post_run() will always run after the run() and test_*()
  # functions are run regardless of any failures. This method can be used to
  # ensure clean-ups are completed in all cases.
  # The post_run() function is OPTIONAL
  def post_run(self):
    self.log_info("Post run func.")
