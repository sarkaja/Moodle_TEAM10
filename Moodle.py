from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import smtplib
import mimetypes
import creds
import os
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

#driver a jeho umisteni
driver = webdriver.Chrome('C:/users/dell/ted/chromedriver.exe')

#prihlaseni do moodlu a vstup do kurzu
driver.get("https://moodle.vse.cz/")

login = driver.find_element_by_xpath('//*[@id="banner"]/nav/div[2]/div[2]/div/span/a')
login.click()
login2 = driver.find_element_by_xpath('//*[@id="region-main"]/div[2]/div[2]/div/div/div/div/div/a')
login2.click()

mail = driver.find_element_by_xpath('//*[@id="i0116"]')
mail.send_keys(jmenomailu)  
mail.send_keys(Keys.RETURN) 
time.sleep(5)

password = driver.find_element_by_xpath('//*[@id="passwordInput"]')
password.send_keys(heslomailu)
password.send_keys(Keys.RETURN) 
time.sleep(3)

kurz = driver.find_element_by_link_text('4IT403')
kurz.click()
time.sleep(3)

#stazeni dat pro dimenzi Zaverecny test
zakonceni_kurzu = driver.find_element_by_link_text('Zakončení kurzu')
zakonceni_kurzu.click()
time.sleep(3)

zaverecna_evaluace = driver.find_element_by_link_text('Závěrečná evaluace')
zaverecna_evaluace.click()
time.sleep(3)

vysledky = driver.find_element_by_link_text('Výsledky')
vysledky.click()
time.sleep(3)

vyber_uzivatelu = driver.find_element_by_xpath('//*[@id="id_attempts"]')
vyber_uzivatelu.click()
time.sleep(3)

vsichni = driver.find_element_by_xpath('//*[@id="id_attempts"]/option[3]')
vsichni.click()
time.sleep(3)

zobrazeni_sestavy = driver.find_element_by_xpath('//*[@id="id_submitbutton"]')
zobrazeni_sestavy.click()
time.sleep(3)

vyber_formatu = driver.find_element_by_xpath('//*[@id="downloadtype_download"]')
vyber_formatu.click()
time.sleep(3)

excel = driver.find_element_by_xpath('//*[@id="downloadtype_download"]/option[1]')
excel.click()
time.sleep(3)

stahnout = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[1]/section/div[1]/form[2]/div/button')
stahnout.click()

time.sleep(10)

#poslat mailem


fileToSend = "4IT403-Závěrečná evaluace-hodnocení.csv"


msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "help I cannot send an attachment to save my life"
msg.preamble = "help I cannot send an attachment to save my life"

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)
fp = open(fileToSend, "rb")
attachment = MIMEBase(maintype, subtype)
attachment.set_payload(fp.read())
fp.close()
encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

server = smtplib.SMTP_SSL("smtp.seznam.cz", 465)
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()


path = "C:/users/dell/downloads/4IT403-Závěrečná evaluace-hodnocení.csv"

os.remove(path)