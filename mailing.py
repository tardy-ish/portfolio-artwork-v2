from flask_mail import Message
import os

class clientMessage(Message):
    def __init__(self, recepient:str, name:str, message:str):
        super().__init__()
        self.subject = f"Hey {name}!"
        self.body = f"""
This is an automated message, I generally respond in a day.
You'll be hearing from me very soon on this mail chain.

Here's the message you sent me:

{message}

Thanks and Regards,
Lana Khayat
Website  |  lanakhayat.com
        """
        self.recipients = [recepient]
        self.bcc = [os.environ.get('EMAIL')]
        



