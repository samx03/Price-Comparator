from smtplib import SMTP

def send_mail(sender,to,data):
    server = SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('justrandommails1992@gmail.com','hczsawywxsuajjof')
    subject = 'Alert! Prices have dropped!'
    body = f'Your product is: {data["p"]} \n\n Amazon link is: {data["a"]} \n Amazon price is: {data["pA"]} \n\n Flipkart link is: {data["f"]} \n Flipkart price is: {data["pF"]}'

    msg = f'subject: {subject} \n\n {body}'
    sender=sender
    to = to
    server.sendmail(sender,to,msg)
    print(to)
    print('Mail sent successfully!')
    server.quit()
