import imaplib

def get_email_code():
    imap_server = "imap.rambler.ru"
    imap_port = 993
    username = "ozon12-rew@rambler.ru"
    password = "rs13Tyzc"

    imap = imaplib.IMAP4_SSL(imap_server, imap_port)
    imap.login(username, password)
    imap.select("INBOX")
    sender = "mailer@sender.ozon.ru"
    _, message_ids = imap.search(None, f'(FROM "{sender}")')
    message_ids = message_ids[0].split()[::-1]
    newest_message_id = message_ids[0]
    _, msg_data = imap.fetch(newest_message_id, "(RFC822)")
    raw_email = msg_data[0][1].decode("utf-8")
    numbers = [int(x) for x in raw_email.split() if x.isdigit() and len(x) == 6]
    auth_code = numbers[0]
    if len(str(auth_code)) < 6:
        auth_code = f'0{auth_code}'
    imap.logout()
    return(auth_code)
