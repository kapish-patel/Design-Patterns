# code up SMS class
from Notification import Notification

class SMS(Notification):

    def Notify(self):
        # logic related to sending a SMS to a given phone number
        phoneNumber = input("Enter recipient Phone Number: ")
        message = input("Enter message: ")
        return f"SMS sent to {phoneNumber}: {message}"