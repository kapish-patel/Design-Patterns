from Notification import Notification
from OtherNotificationType import OthernotificationType
from db import db

class Others(Notification):

    def sendNotification(self, serviceName: str, recipientName: str, message: str):
        otherNotificationTypeObj = db.getValue(serviceName)
        return f"Notification send using {otherNotificationTypeObj.name} to {recipientName}: {message}"
         
    def Notify(self):
        serviceName = input("Enter Notification Service Name: ")
        if db.isPresent(serviceName):
                #  send notification using already present service
                recipientName = input("Enter Recipient Name: ")
                message = input("Enter Message: ")
                return(self.sendNotification(serviceName, recipientName, message))
        else:
            serviceUrl = input("Enter Notification Service URL: ")
            serviceAPI_Key = input("Enter Notification Service API Key: ")
            recipientName = input("Enter Recipient Name: ")
            message = input("Enter Message: ")

            newOthernotificationType = OthernotificationType(serviceName, serviceUrl, serviceAPI_Key)
            db.setValue(serviceName, newOthernotificationType)

            return(self.sendNotification(serviceName, recipientName, message))
         