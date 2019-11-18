import smtplib as mailsender

sender = "oalade@wavepoint.com.ng"
receivers = ['dapcigar@gmail.com','earnwithd33@gmail.com','o.alade@henrywilsonltd.com']
subject = "Hello World"
message = '''
        From: From Person <oalade@wavepoint.com.ng>
        to: Brandy <dapcigar@gmail.com>
        subject: Let us meet at Yaba or Unilag
        This is just a mail to you.
'''
try:
    hostObj = mailsender.SMTP('localhost')
    hostObj.sendmail(sender,receivers,message)
    print('Email Sent successfully')
except mailsender.SMTPException:
    print('Email not sent successfully')

