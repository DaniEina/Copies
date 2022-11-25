import os
import datetime
import sys


#email:
import smtplib

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.utils import COMMASPACE, formatdate



import mimetypes


MatriuBidimensional= [
        
        ['/volume1/ANGELS_PC/ANGELS_Copia/', 'angels@grupeina.com', 10, '/volume1/Sistemes/rsync/angels.log'],
        ['/volume1/Sistemes/', 'tlopez2@grupeina.com', 5, '/volume1/Sistemes/rsync/jo2.log'],
        ['/volume1/XGONZALEZ/ /volume1/XGONZALEZ_ESCRIPTORI/', 'xavi@grupeina.com', 10, '/volume1/Sistemes/rsync/xavigonzalez.log'],
        ['/volume1/CATI/', 'cati@grupeina.com', 10, '/volume1/Sistemes/rsync/cati.log'],
        
        ['/volume1/FredVdhPC/', 'fredvdh@grupeina.com', 10, '/volume1/Sistemes/rsync/fred.log'],
        ['/volume1/RBARO/', 'rbaro@grupeina.com', 10, '/volume1/Sistemes/rsync/rbaro.log'],
        
        ['/volume1/NURIA/', 'npinent@grupeina.com', 10, '/volume1/Sistemes/rsync/npinent.log'],
        ['/volume1/BETLEM/', 'bmolas@grupeina.com', 10, '/volume1/Sistemes/rsync/betlem.log'],

        ['/volume1/NFABREGA/', 'nfabrega@grupeina.com', 10, '/volume1/Sistemes/rsync/nfabrega.log'],

        #['/volume1/FPOCH/', 'fpoch@grupeina.com', 10, '/volume1/Sistemes/rsync/xicu.log'],
        ['/volume1/CSABALLS/', 'csaballs@grupeina.com', 10, '/volume1/Sistemes/rsync/conxi.log'],

        ['/volume1/TCastilloPC', 'tcastillo@grupeina.com', 10, '/volume1/Sistemes/rsync/tania.log'],
        ['/volume1/DVALENTINOVA', 'daniela@grupeina.com', 10, '/volume1/Sistemes/rsync/daniela.log'],

        ['/volume1/ROSAPC', 'rosa@grupeina.com', 10, '/volume1/Sistemes/rsync/rosa.log']
    





        ]


#def crearmatriu(Sortida, Nom, llistat):
 #   if Sortida == 0:
  #      S="Ultims arxius modificats"
   # else:
    #    S="FAIL"
   # llistat=llistat
   # return llistat

for i in MatriuBidimensional:
    ruta=(i[0])
    numarxius=(i[2])
    numarxiusstr=str(numarxius)
    persona=(i[3])
    email=(i[1])
#    commanda=("ls"ruta)
    #llistat=os.system("ls" +ruta +"ls"  +numarxiusstr)
#    llistat=os.system("find i[0] -type f -mtime -1 -printf 'El dia %TY-%Tm-%Td a les %.8TT has editat %f\n' | sort -r | head -+i[2]")
#    email="tlopez@grupeina.com"
    
    llistat=os.system("find " +ruta +" -type f -mtime -1 -printf 'El dia %TY-%Tm-%Td a les %.8TT has editat %f\n' | sort -r | head -"+numarxiusstr +" > " +persona)
    fa=open (persona,'r')
    contingut=fa.read()
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
#    username = 'sistemes@grupeina.com'
#    password = '!Ein@Digit@1!'
    username = 'gedcopies@gmail.com'
    password = 'grupeina2011!'
    sender = 'AVIS!'
    targets = [email]
    msg = MIMEText("Aquests son els ultims arxius que has editat les ultimes 24h, segons la copia de seguretat:" +"\n" +contingut)
#    msg = MIMEText(contingut)
    msg['Subject'] = ("Ultims arxius editats - Avis de copia de seguretat")
    msg['From'] = sender
    msg['To'] = ', '.join(targets)
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
 
    server.quit()
 




#ENVIARADJUNT
#    to = ["tlopez@grupeina.com"]
#    gmail_user = 'avisgrupeina@gmail.com'
#    gmail_pwd = 'grupeina2011!'
#    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
#    smtpserver.starttls()
#    smtpserver.login(gmail_user, gmail_pwd)
#    msg = MIMEMultipart()
#    msg["From"] = "avisgrupeina@gmail.com"
#    msg["To"] = ",".join(to)
#    msg["Subject"] = ("Ultims arxius editats - Avis de copia de seguretat")
#    msg.preamble = "UltisArxius"

#    ctype, encoding = mimetypes.guess_type(persona)
#    if ctype is None or encoding is not None:
#            ctype = "application/octet-stream"

#            maintype, subtype = ctype.split("/", 1)


#            fp = open(persona)
#            # Note: we should handle calculating the charset
#            attachment = MIMEText(fp.read(), _subtype=subtype)
#            fp.close()

#            attachment.add_header("Content-Disposition", "attachment", filename=persona)
#            msg.attach(attachment)


#            smtpserver.sendmail(gmail_user, to, msg.as_string())
#            print 'done!'
#            smtpserver.close()








