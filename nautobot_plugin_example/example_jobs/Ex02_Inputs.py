# This imports a sleep function used as an example time delay
from time import sleep

# Importing Job from nautobot.extras.jobs is required for any Nautobot job.
from nautobot.extras.jobs import Job

# These imports are the type of inputs that are being used in this job.
from nautobot.extras.jobs import StringVar, IntegerVar, BooleanVar, ChoiceVar

# This is the job grouping within the Nautobot UI.
name = "AD Example jobs"

# This is the job being imported.
class Ex02_Inputs(Job):
  # The following are the definitions of the job inputs. Reference the following
  # link for more details on available types of inputs.
  # https://nautobot.readthedocs.io/en/stable/additional-features/jobs/#variables
  var_text = StringVar(
    default = "Default value",
    description = "Test text value to be outputted to the JobResults",
    label = "Test text"
  )
  var_sleep = IntegerVar(
    default = 0,
    description = "Seconds to sleep as a test.",
    label = "Sleep seconds"
  )
  var_bool = BooleanVar(
    default = True,
    description = "This will cause the job to succeed or fail (intentionally)",
    label = "True/False boolean example"
  )
  var_choice = ChoiceVar(
    description = "Choice selection test",
    label = "Opportunities",
    choices = (("10","The wrong choice"),("20","The right choice"))
  )

  # The Meta class within the job class is used for job extensible data
  class Meta():
    # This is what the job will be named in the UI.
    name = "Example 02 - Inputs"
    # The first line of the description will be displayed but other lines will
    #   only be displayed on job details.
    description = """
      This is the first test job written.
      The variables inputting will be outputted or processed
    """
    # By default, job variables/inputs will be ordered in the order they are
    # defined. You can change this order by defining the optional field_order
    # var.
    field_order = ["var_text","var_sleep","var_choice","var_bool"]

  # This will be run when the job starts.
  def run(self, data, commit):
    # This job gives examples on how to log data and use inputs from the job
    # form data.

    # Basic log
    self.log_info("Job start")

    # By using data.get('VAR_NAME') you can access the inputted user data.
    self.log(f"Input - Text var: {data.get('var_text')}")
    self.log(f"Sleeping for {data.get('var_sleep')} seconds.")
    # An IntegerVar will default to an actual integer so no processing is needed
    sleep(data.get('var_sleep'))
    self.log_success("Done!")

    # Same for BooleanVar, no True/False processing is necessary.
    if data.get('var_bool'):
      self.log_success("Boolean var was True!")
    else:
      # Important! This log is a failure log. This will cause the job itself to
      # mark as "Failed." Because we're not stopping the job at the failure
      # though, the rest of the job will continue. Database changes will be
      # reverted at the end of the job, however.
      self.log_failure("Boolean var was False!")

    if data.get('var_choice') == "10":
      self.log_warning(f"Warning: Poor VLAN choice: {data.get('var_choice')}")
    else:
      self.log_success(f"Success: Good VLAN choice: {data.get('var_choice')}")
    self.log_info("Job complete")

