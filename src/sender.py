from smtplib import SMTP
import datetime
import json

SMTP_SERVER = "mail.hurmaciniz.com" # SMTP mail server domain
SMTP_PORT = "587" # SMTP mail server port


class MailSender:
    def __init__(self,subscribtion_file_path, sender_mail, master_receiver_mail) -> None:
        self.sender_mail = sender_mail
        self.master_receiver_mail = master_receiver_mail
        
        with open(subscribtion_file_path) as subscribtions_file:
            self.subscribtions = json.load(subscribtions_file)
    
    def connect_to_mail_server(self):
        debug_level = 0
        self.smtp_connection = SMTP()
        self.smtp_connection.set_debuglevel(debug_level)
        self.smtp_connection.connect(SMTP_SERVER , SMTP_PORT)
        self.smtp_connection.login(self.sender_mail, "<MAIL_PASSWORD>")        
        
    def sender(self):
        asd = 123
        mail_subject = f"{asd} Abonelik numarali {asd} aboneliginin hatirlatmasi"
        mail_text = f"Abonelik : {asd}\nAbonelik numarasi : {asd}\nSon odeme tarihi: {asd}"
        
        mail = "From: %s\nTo: %s\nSubject: %s\n\n%s" % ( self.sender_mail, self.master_receiver_mail, mail_subject, mail_text )
        
        self.smtp_connection.sendmail(self.sender_mail, self.master_receiver_mail, mail)
        self.smtp_connection.quit()
            
    