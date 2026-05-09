from app.database import db

def add_member_service(member_data):

    existing_member = db.members.find_one(
        {"email": member_data["email"]}
    )

    if existing_member:

        return {
            "error": "Member already exists"
        }

    db.members.insert_one(member_data)

    return {
        "message": "Member Added Successfully"
    }

def get_members_service():

    members = list(
        db.members.find({}, {"_id": 0})
    )

    return members