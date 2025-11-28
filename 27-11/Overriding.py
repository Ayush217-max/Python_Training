from email import message


class Notification:
    def send(self,message):
        print("sending notification",message)

class EmailNotification(Notification):
    def send(self,message):
        print("sending email",message)

class SMSNotification(Notification):
    def send(self,message):
        print("sending sms",message)

class PushNotification(Notification):
    def send(self,message):
        print("sending push",message)

n=EmailNotification()
n.send("hii")

m=SMSNotification()
m.send("OTP:3456")

o=PushNotification()
o.send("Goooooooo")