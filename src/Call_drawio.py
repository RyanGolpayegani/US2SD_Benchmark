import drawio

SDt = """
@startuml
actor Practitioner
boundary "Profile Page" as Profile
database "Data Storage" as DB
  
Practitioner -> Profile: Access profile page
Profile --> Practitioner: Show profile data
Practitioner -> Profile : Request to add additional details
Profile --> Practitioner: Provide form for additional details
Practitioner -> Profile: Submit form with new details
Profile -> DB: Push new details to database
DB --> Profile: Confirm receipt of data
Profile --> Practitioner: Success message

@enduml
"""

drawio.diagram