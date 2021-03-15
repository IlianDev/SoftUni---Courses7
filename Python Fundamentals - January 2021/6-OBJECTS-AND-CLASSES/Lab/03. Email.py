class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []

email_data = input()
while not email_data == "Stop":
    sender_1, reciever_1, content_1 = email_data.split()
    current_email = Email(sender_1, reciever_1, content_1)
    emails_list.append(current_email)
    email_data = input()

indexes_mail_to_send = [int(index) for index in input().split(", ")]

for index_email in indexes_mail_to_send:
    email_to_send = emails_list[index_email]
    email_to_send.send()

for email in emails_list:
    print(email.get_info())
