class WebInterface:
    def request_edit_form(self, item):
        print("Web Interface -> Application Server: Request edit form for item")
        return item

    def submit_update_request(self, edited_item):
        print("Web Interface -> Application Server: Submit update request with edited details")
        return edited_item

class ApplicationServer:
    def retrieve_item_details(self, item_id):
        print("Application Server -> Database: Retrieve item details")
        # Simulating database retrieval
        return {"item_id": item_id, "details": "Sample details"}

    def update_item(self, edited_item):
        print("Application Server -> Database: Update item in database")
        # Simulating database update
        return True

class Database:
    def confirm_update(self):
        print("Database -> Application Server: Confirm item updated")
        return True

# Simulating user input
item_id = 123

# Creating instances of components
web = WebInterface()
app = ApplicationServer()
db = Database()

# Moderator selects item to edit
print("Moderator -> Web Interface: Selects item to edit")
edited_item = web.request_edit_form(item_id)

# Web Interface shows edit form to moderator
print("Web Interface -> Moderator: Show edit form")

# Moderator submits edited item details
print("Moderator -> Web Interface: Submits edited item details")
updated_item = web.submit_update_request(edited_item)

# Application Server updates item in the database
item_updated = app.update_item(updated_item)

# Database confirms item update success
if item_updated:
    print("Database -> Application Server: Confirm item updated")
    print("Application Server -> Web Interface: Confirm update success")
    print("Web Interface -> Moderator: Display update success message")
else:
    print("Item update failed")

print("Sequence completed.")
