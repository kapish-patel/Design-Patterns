from OtherNotificationType import OthernotificationType

class db:
    _otherNotificationTypes  = {}

    @staticmethod
    def getValue(key: str):
        return db._otherNotificationTypes.get(key)
    
    @staticmethod
    def setValue(key: str, value: OthernotificationType):
        db._otherNotificationTypes[key] = value
    
    @staticmethod
    def isPresent(key: str):
        if key in db._otherNotificationTypes:
            return True
        return False