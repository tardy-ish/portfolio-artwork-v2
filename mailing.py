from flask_mail import Message
import os

class clientMessage(Message):
    def __init__(self, recepient:str, name:str):
        super().__init__()
        self.subject = f"Hey {name}!"
        self.body = """
This is an automated message, I generally respond in a day.
You'll be hearing from me very soon on this mail chain.

Thanks and Regards,
Lana Khayat
Website  |  lanakhayat.com
        """
        self.recipients = [recepient]
        self.bcc = [os.environ.get('EMAIL')]
        

class selfMessage(Message):
    def __init__(self, name:str, email:str, message:str):
        super().__init__()
        self.subject = f"Message from {name} : {email}!"
        self.body = f"""
{name} with the email: {email} has sent you the following message:

{message}
"""
        self.recipients = [os.environ.get('EMAIL')]



