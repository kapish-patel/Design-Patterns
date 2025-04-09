#  code up email notification class
from Notification import Notification

class Email(Notification):

    def Notify(self):
        # logic related to sending a email to the given email
        email = input("Enter recipient Email: ")
        message = input("Enter message: ")
        return f"Email sent to {email}: {message}"