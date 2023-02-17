from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


with open('aula100/template.html', 'r',  encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Murilo Akita', data=data_atual)


# Enviando HTML como email.
msg = MIMEMultipart()
msg['from'] = 'Murilo Quadros Akita'
msg['to'] = 'murilo.akita@gmail.com'
msg['subject'] = 'Atenção: este é um e-mail de testes.'
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# Enviando imagem e anexando ao email.
with open('aula100/picapau.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP("smtp.mailtrap.io", 2525) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("a50ba80617d88b", "aefb2d552c2574")
    smtp.send_message(msg)
    print('E-mail enviado com sucesso!')
