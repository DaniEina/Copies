import os
import mimetypes




import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.utils import COMMASPACE, formatdate

from os import remove
remove('/volume1/Sistemes/rsync/rsync.log')
remove('/volume1/Sistemes/rsync/rsyncLLISTATARXIUS.log')

def emplenaText(Sortida, NomDB, text):
        if Sortida == 0:
                S="Copia Completada RSYNC "
        else:
                S="ERROR RSYNC"
#        text=text+S+NomDB
#        return text+" feta a les: "+DATETIME+"\n"

fileToSend="/volume1/Sistemes/rsync/rsync.log"
CopiaOK="RSYNC GED2 OK"
AssumpteEmail=CopiaOK
CopiaFail="ERROR AL RSYNC DE GED2"
CodiDeError=0
text=""


ResultatDump=os.system("rsync -e ssh -ar --stats --delete --exclude-from=/volume1/Sistemes/rsync/excluir.txt /volume1/ copies@192.168.10.221:/volume1/10.222 > /volume1/Sistemes/rsync/rsync.log --log-file=/volume1/Sistemes/rsync/rsyncLLISTATARXIUS.log")
if ResultatDump != 0:
	AssumpteEmail=CopiaFail


#to = ["tlopez@grupeina.com", "dsanchez@grupeina.com"]

#to = ["tlopez@grupeina.com"]

#smtp_ssl_host = 'smtp.gmail.com'
#smtp_ssl_port = 465
#username = 'avisgrupeina@gmail.com'
#password = 'grupeina2011!'

#gmail_user = 'avisgrupeina@gmail.com'
#gmail_pwd = 'grupeina2011!'
#smtpserver = smtplib.SMTP("smtp.gmail.com",465)
#smtpserver = smtplib.SMTP("smtp.gmail.com",587)
#smtpserver.ehlo()
#smtpserver.starttls()
#smtpserver.ehlo
#smtpserver.login(gmail_user, gmail_pwd)

#msg = MIMEMultipart()
#msg["From"] = "avisgrupeina@gmail.com"
#msg["To"] = ",".join(to)
#msg["Subject"] = (AssumpteEmail)
#msg.preamble = "CopiesRsync"

#ctype, encoding = mimetypes.guess_type(fileToSend)
#if ctype is None or encoding is not None:
#    ctype = "application/octet-stream"

#maintype, subtype = ctype.split("/", 1)


#fp = open(fileToSend)
# Note: we should handle calculating the charset
#attachment = MIMEText(fp.read(), _subtype=subtype)
#fp.close()

#attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
#msg.attach(attachment)


#smtpserver.sendmail(gmail_user, to, msg.as_string())
#print 'done!'
#smtpserver.close()

logdetallat='/volume1/Sistemes/rsync/rsync.log'

fa=open (logdetallat,'r')
contingut=fa.read()

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

username = 'copieseina@gmail.com'
###password = '!Ein@Digit@1!'
password = 'grupeina2011!'

#username = 'sistemes@grupeina.com'
#password = '!Ein@Digit@1!'
sender = 'CopiesRsync'
targets = ["sistemes@grupeina.com"]
#targets = ["tlopez@grupeina.com"]




msg = MIMEText(contingut +"\n" +"Per mes info mirar el log que esta al 192.168.10.222/volume1/Sistemes/rsync/rsyncLLISTATARXIUS.log" +"\n" +"\n" +"\n" +"\n" +"\n" +"\n" +"\n" +"\n" +"\n")


msg['Subject'] = (AssumpteEmail)

msg['From'] = sender

msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

server.login(username, password)

server.sendmail(sender, targets, msg.as_string())


server.quit()




os.system("ssh copies@192.168.10.221 'touch /volume1/HaAcabatCopiaPowerOff/CopiaCompletada-10-222-volume1'")

os.system("ssh -t copies@192.168.10.221 python /volume1/HaAcabatCopiaPowerOff/TestExisteix.py")

