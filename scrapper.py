import pandas as pd
import numpy as np
import re
import requests
import bs4
import smtplib
import time

def crous_scrapper(URL : str, MAIL : str, MAIL_mdp: str):
    '''
    URL: lien de la page de recherche
    MAIL: addresse mail ou l'on souhaite recevoir les informations mais aussi celle qui va envoyer les mails
    MAIL_mdp: mot de passe de la boite mail
    '''
    msg = ''
    while True:
        token = URL
        def get_pages(token, nb):
            pages = []
            for i in range(1,nb+1):
                j = token + str(i)
                pages.append(j)
            return pages
        pages = get_pages(token,1)
        for i in pages:
            response = requests.get(i)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        em_box = soup.find_all("li", {"class":"SearchResults-item"})
        l = []
        for link in soup.find_all('a',{"aria-hidden":"true"}):
            l.append(link.get('title'))
        df = pd.DataFrame(l)
        df = df.dropna().reset_index(drop=True)
        liste = []
        for i in range(len(df)):
            text = df.iloc[i].tolist()[0][22:]
            liste.append(re.sub(r'.*([0-9]{5}).*',r'\1',text))
        df = pd.DataFrame(liste,columns=['post code'])
        df["post code"] = pd.to_numeric(df["post code"])
        df = df.where(df['post code']!=2160).dropna()
        new_msg = str(df['post code'].tolist())
        

        if len(df) > 0 and new_msg != msg:
            # Specifying the from and to addresses
            fromaddr = MAIL
            toaddrs  = MAIL 

            # Writing the message (this message will appear in the email)

            msg = str(df['post code'].tolist()) 

            # Gmail Login

            username = MAIL
            password = MAIL_mdp 

            # Sending the mail  

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
        else:
            msg = str(df['post code'].tolist())