from django.core.mail import send_mail

class DjangoMail():

    def __init__(self):
        self.from_email =  "beebayk63478@gmail.com"
        self.fail_silently = False
        
    def send(self, dct):
        subject = dct["subject"]
        message = dct["message"]
        to_emails = dct["to"]
        send_mail(
            subject,
            message,
            self.from_email,
            to_emails,
            fail_silently=self.fail_silently
        )