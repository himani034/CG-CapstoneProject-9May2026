from datetime import datetime

from app.database import db

def create_log(action, user):

    log = {
        "action": action,
        "user": user,
        "time": str(datetime.now())
    }

    db.audit_logs.insert_one(log)