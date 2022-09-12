import smtplib
from email.mime.text import MIMEText

from GaiaX_py import settings

def enviar_Correo():
    try:
        # mailServer = smtplib.SMTP('smtp.gmail.com',587)
        # mailServer.ehlo()
        # mailServer.starttls()
        # mailServer.ehlo()
        # mailServer.login("proyecto.gaiax@gmail.com","#SoyFrachezco%")
        mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)

        # Variable temporal para no repetir correo
        emailEnvio = "gonzatuto01@gmail.com"

        #Enviar Mensajes
        mensaje = MIMEText("""" Este correo es de prueba enviado por GaiaProyectX y el jonatan  """)
        mensaje['From'] =  settings.EMAIL_HOST_USER
        mensaje['To'] = emailEnvio
        mensaje['Subject'] = "GaiaCorreo"

        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            emailEnvio,
                            mensaje.as_string())
        print('Correo enviado correctamente')

    except Exception as e:
        print(e)


enviar_Correo()