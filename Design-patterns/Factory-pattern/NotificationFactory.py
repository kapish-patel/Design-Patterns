# notification factory

from Email import Email
from SMS import SMS
from Push import Push
from Others import Others

class NotificationFactory:
    
    _NotificationTypes = {
        "email": Email,
        "sms": SMS,
        "push": Push,
        "others": Others
    }

    @staticmethod
    def getNotificationTypeList():
        return NotificationFactory._NotificationTypes.keys()

    @staticmethod
    def getNotificationTypeInstance(NotificationType: str):
        # returns a instance of requested notification type

        notificationType = NotificationFactory._NotificationTypes.get(NotificationType.lower())

        if notificationType:
            return notificationType()
        raise ValueError(f"Notification type {NotificationType} is not supported at the moment")

    


