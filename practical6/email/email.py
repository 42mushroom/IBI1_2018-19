# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:05:46 2019

@author: 30389
"""
import re
address_information= open('address_information.csv')
for address in address_information:
   L=re.split(r'[,]',address)
   for elementsinL in L:
       addressString = re.findall('ibifiletest\S+', elementsinL)
       if (len(addressString)>0) :
          legal=""
          legal=legal+str(addressString)
          print(legal)
          l=str.split("",legal)
          print (l)
import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host="smtp."
mail_user="jiayid.18@intl.zju.edu.cn"
mail_pass="Fuga@7877"   #口令 
 
maintext = open('body.txt')
maintext =str(maintext)
sender ="jiayid.18@intl.zju.edu.cn"
receivers =["ibifiletest@163.com"]
message = MIMEText(maintext,'plain', 'utf-8')
message['From'] = Header("Dong Jiayi", 'utf-8')
message['To'] =  Header("user", 'utf-8')
subject="test"
message['Subject'] = Header(subject, 'utf-8')
smtpObj =smtplib.SMTP('smtp.zju.edu.cn',25) 
smtpObj.connect(mail_host, 25)
smtpObj.login(mail_user,mail_pass)  
smtpObj.sendmail(sender, receivers, message.as_string())
