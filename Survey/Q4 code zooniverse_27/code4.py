class AdminInterface:
    def assess_image(self, image_id):
        print("Admin Interface -> Backend Server: Assess image ({})".format(image_id))

    def display_results(self, results):
        print("Admin Interface -> Admin: Display assessment results")

    def display_error(self, error_message):
        print("Admin Interface -> Admin: Display error:", error_message)

class BackendServer:
    def fetch_image_details(self, image_id):
        print("Backend Server -> Database: Fetch image details ({})".format(image_id))
        # Simulating database retrieval
        return {"image_id": image_id, "details": "Sample details"}

    def analyze_image(self, image_id):
        print("Backend Server -> Image Analysis Service: Analyze image")
        # Simulating image analysis
        return {"analysis_data": "Sample analysis data"}

    def fetch_citizen_annotations(self, image_id):
        print("Backend Server -> Database: Fetch citizen annotations")
        # Simulating database retrieval
        return {"annotations": "Sample annotations"}

    def fetch_comments(self, image_id):
        print("Backend Server -> Talk Service: Fetch comments from Talk")
        # Simulating talk service
        return {"comments": "Sample comments"}

class ImageAnalysisService:
    def analyze_image(self, image_id):
        print("Image Analysis Service: Analyze image")
        # Simulating image analysis
        return {"analysis_data": "Sample analysis data"}

class TalkService:
    def fetch_comments(self, image_id):
        print("Talk Service: Fetch comments from Talk")
        # Simulating talk service
        return {"comments": "Sample comments"}

# Simulating user input
image_id = "123"

# Creating instances of components
admin_interface = AdminInterface()
backend_server = BackendServer()
image_analysis_service = ImageAnalysisService()
talk_service = TalkService()

# Admin requests image assessment
print("Admin -> Admin Interface: Request image assessment")
admin_interface.assess_image(image_id)

# Backend Server assesses image
print("Admin Interface -> Backend Server: Assess image ({})".format(image_id))
image_details = backend_server.fetch_image_details(image_id)

# Backend Server analyzes image
print("Backend Server -> Image Analysis Service: Analyze image")
analysis_data = image_analysis_service.analyze_image(image_id)

# Backend Server fetches citizen annotations
print("Backend Server -> Database: Fetch citizen annotations")
annotations = backend_server.fetch_citizen_annotations(image_id)

# Backend Server fetches comments
print("Backend Server -> Talk Service: Fetch comments from Talk")
comments = talk_service.fetch_comments(image_id)

if analysis_data:
    print("Image Analysis Available")
    # Backend Server aggregates assessment data
    print("Backend Server -> Admin Interface: Aggregate assessment data")
    assessment_results = {
        "image_details": image_details,
        "analysis_data": analysis_data,
        "annotations": annotations,
        "comments": comments
    }
    # Admin Interface displays assessment results
    admin_interface.display_results(assessment_results)
else:
    print("No Analysis Data Found")
    # Admin Interface displays error message
    admin_interface.display_error("No analysis data found for image {}".format(image_id))

print("Sequence completed.")
