from NotificationFactory import NotificationFactory

# main method
def main():
    while True:
        # code up the main method
        notificationTypes = NotificationFactory.getNotificationTypeList()
        notificationType = input(f"Enter notification type ({notificationTypes}): ")
        notificationTypeInstance = NotificationFactory.getNotificationTypeInstance(notificationType)
        print(notificationTypeInstance.Notify())
if __name__ == '__main__':
    main()

