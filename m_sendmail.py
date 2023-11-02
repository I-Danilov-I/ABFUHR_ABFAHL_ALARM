import smtplib
from email.message import EmailMessage


class SendeEmail:
    def __init__(self, send_from, send_to, headline, message):
        print("E-Mail-Objekt initialisieren..")
        self.mail = EmailMessage()

        print("Betreffzeile wird eingefügt...")
        self.mail['Subject'] = headline

        print("Absender wird eingefügt...")
        self.mail['From'] = send_from

        print("Empfänger wird eingefügt...")
        self.mail['To'] = send_to

        print("Serverhost wird eingefügt...")
        self.sender = smtplib.SMTP("mail.gmx.net")
        self.sender.ehlo()
        self.sender.starttls()
        self.sender.ehlo()

        print("Login versuch...")
        try:
            self.sender.login("danilov.a@gmx.net", "$kylinE-3#gm")
        except smtplib.SMTPAuthenticationError:
            print("Falsche E-mail oder Passwort!")

        try:
            print("Inhalt der E-Mail wird definiert...")
            self.mail.set_content(message)
        except:
            print("Fehler")


        try:
            print("E-mail wird versendet...")
            self.sender.send_message(self.mail)
            print("Email erfolgreich versendet! ;)\n")

        except smtplib.SMTPSenderRefused:
            print("Email konnte nicht versendet werden.")
        self.sender.close()

