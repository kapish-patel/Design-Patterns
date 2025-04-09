# code up push class
from Notification import Notification

class Push(Notification):
    def Notify(self, Message: str, Email: str):
        # perform all the logic related to search of user using email and sending a push notification
        email = input("Enter recipient Email: ")
        message = input("Enter message: ")
        return f"Push notification sent to user of{email}: {message}"