import os
import win32com.client as outlook
import datetime


class MyOutlook:
    def __init__(self):
        self.outlook = outlook.Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder(6)
        self.timestamp = datetime.datetime.now()
        self.save_path = os.environ["USERPROFILE"] + r"\Downloads"
        self.get_dates()

    def get_dates(self):
        today = self.timestamp.date()
        self.today = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
        self.yesterday = self.today + datetime.timedelta(days=-1)

    def set_save_path(self, path_name):
        self.save_path = path_name
    
    def get_email_list(self, folder_name, start_date=None, end_date=None):
        if not start_date:
            start_date = self.today
        if not end_date:
            end_date = datetime.datetime.now()
        mail_list = []
        folders = self.inbox.Folders

        for folder in folders:
            if str(folder) == folder_name:
                mails = folder.Items
                for mail in mails:
                    rt = mail.receivedtime
                    received_time = datetime.datetime(rt.year, rt.month, rt.day, rt.hour, rt.minute, rt.second)

                    if received_time >= start_date and received_time <= end_date:
                        mail_detail = {
                            "subject": mail.subject,
                            "sender": mail.sendername,
                            "sender_address": mail.senderEmailAddress,
                            "received_time": mail.receivedtime,
                            "flg_unread": mail.Unread,
                            "body": mail.body,
                            "attachments": mail.attachments,
                        }
                        mail_list.append(mail_detail)
            return mail_list
    
    def save_attachments(self, folder_name, subject, sender_address, start_date=None, end_date=None):
        mails = self.get_email_list(folder_name, start_date=start_date, end_date=end_date)
        target_mails = []
        for mail in mails:
            if subject in mail["subject"] and sender_address in mail["sender_address"]:
                target_mails.append(mail)
                attachments = mail["attachments"]
                for attachment in attachments:
                    attachment.SaveAsFile(os.path.join(self.save_path, attachment.filename))
        return target_mails


if __name__ == "__main__":
    pass