from smtplib import SMTP
import datetime
from src.sender import MailSender

SENDER_MAIL = ""
MASTER_RECEIVER_MAIL = ""
JSON_FILE_PATH = "JSON/subscriptions.json"

class Main:
    def __init__(self) -> None:
        self.mail_sender = MailSender(SENDER_MAIL, MASTER_RECEIVER_MAIL)
        self.mail_sender.connect_to_mail_server()
    
    def main(self):
        self.mail_sender.sender()
        
if __name__ == "__main__":
    main = Main()
    main.main()



    