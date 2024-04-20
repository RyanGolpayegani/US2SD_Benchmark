class SubmissionInterface:
    def validate_submission(self, data):
        if self.is_valid(data):
            return True
        else:
            return False

    def is_valid(self, data):
        # Simulating validation logic
        if len(data) > 0:
            return True
        else:
            return False

class Validator:
    def validate(self, data):
        # Simulating validation logic
        if len(data) > 0:
            return True
        else:
            return False

class ErrorHandler:
    def report_errors(self, error_details):
        # Simulating error reporting
        print("Error reported:", error_details)

class FeedbackMechanism:
    def format_error_messages(self, error_details):
        # Simulating formatting of error messages
        formatted_errors = "Formatted errors: " + error_details
        return formatted_errors

# Simulating user input
user_data = "Sample data"

# Creating instances of components
interface = SubmissionInterface()
validator = Validator()
error_handler = ErrorHandler()
feedback = FeedbackMechanism()

# Submitting data
print("User -> Interface: Submit Data")
if interface.validate_submission(user_data):
    print("Interface -> Validator: Validate Submission")
    if validator.validate(user_data):
        print("Validator -> Interface: Validation Success")
        print("Interface -> User: Success Message")
    else:
        print("Validator -> ErrorHandler: Report Errors")
        error_details = "Some error details here."
        error_handler.report_errors(error_details)
        print("ErrorHandler -> Validator: Error Details")
        print("Validator -> Interface: Validation Fail + Error Details")
        print("Interface -> Feedback: Format Error Messages")
        formatted_errors = feedback.format_error_messages(error_details)
        print("Feedback -> Interface: Formatted Error Messages")
        print("Interface -> User: Error Messages")
else:
    print("User input is invalid.")

print("User deactivated")
