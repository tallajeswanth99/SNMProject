import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('tallajeswanth99@gmail.com','hlqp xblk bbsi nhlk')
    msg=EmailMessage()
    msg['FROM']='tallajeswanth99@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('msg sent')
    server.close()

