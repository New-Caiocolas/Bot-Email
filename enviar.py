import smtplib
import email.message

emails = ['caiocolas2304@gmail.com', 'ryan.ferri2018@gmail.com']

def enviar_email(destinatarios):
    corpo_email = """
    <p>Teste python</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Teste python"
    msg['From'] = 'caiocolas2304@gmail.com'
    msg['To'] = ', '.join(destinatarios)

    password = 'tgxjzkhdtyhmbhcn' 

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], destinatarios, msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email(emails)