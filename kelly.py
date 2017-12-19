import telepot
import sys, string
import time
from pprint import pprint


bot = telepot.Bot("500381074:AAERSP1T-nSOtXVt0UuMJx4iwZPgH3AWagg")

"""
STILL WORKING
def impare():
    f = open("risposta.py", "w")
    f.write("  if x == ")
    f.write(x)
    f.write(":\n")
    f.write("  bot.sendMessage(chat_id, ")
    f.write(y)
    f.write(")")
"""


def avviso():
    import urllib
    import datetime
    anno = datetime.datetime.now().strftime('%Y')
    mese = datetime.datetime.now().strftime('%m')
    giorno = datetime.datetime.now().strftime('%d')
    data = anno + "/" + mese + "/" + giorno + "/"
    url = "https://www.liceo-orazio.gov.it/" + data
    return url

    """
    STILL WORKING
    
    print url
    sock = urllib.urlopen(url)
    html = []
    html = sock.read()
    print html
    y = ['<h2 style="text-align: center;font-size: 20em;line-height: 0;margin-top: 0.5em;">404</h2>']
    for x in html:
        if x == y[0]:
            print "YES"
    sock.close()
    """ 
    

def risposta(chat_id, x):
    
    x = x.lower()

    if x == "avviso":
        bot.sendMessage(chat_id, avviso())
    elif x == "come ti chiami":
        bot.sendMessage(chat_id, "ciao, mi chiamo kelly")

    elif x == "ciao":
        bot.sendMessage(chat_id, "chi sei? (solo il nome o mi confondi)")

    elif x == "giorgio":
        bot.sendMessage(chat_id, "ciao, mio padrone :-)")
    elif x == "gabriele":
        bot.sendMessage(chat_id, "ciao, mio padrone :-)")

    elif x == "paola":
        bot.sendMessage(chat_id, "ciao, mio padrone :-)")
    elif x == "giovanni":
        bot.sendMessage(chat_id, "ciao, mio padrone :-)")

    elif x == "abbaia":
        bot.sendMessage(chat_id, "wuof, wuof")

    elif x == "ringhia":
        bot.sendMessage(chat_id, "grrr")

    elif x == "barzelletta":
        bot.sendMessage(chat_id, "Cosa ci farà un cane su una terrazza?")
        bot.sendMessage(chat_id, "...")
        time.sleep(3)
        bot.sendMessage(chat_id, "RINGHIERA!!!")

    elif x == "aiuto":
        bot.sendMessage(chat_id, "prova a scrivere:")
        bot.sendMessage(chat_id, "come ti chiami")
        bot.sendMessage(chat_id, "ciao")
        bot.sendMessage(chat_id, "abbaia")
        bot.sendMessage(chat_id, "ringhia")
        bot.sendMessage(chat_id, "barzelletta")
        bot.sendMessage(chat_id, "canta")
        bot.sendMessage(chat_id, "avviso")


    elif x == "canta":
        bot.sendMessage(chat_id, "si")
        bot.sendMessage(chat_id, "so anche cantare xD")
        bot.sendVoice(chat_id, (open('file/canta.m4a', 'rb')))

    #elif x == "foto":
        #bot.sendMessage(chat_id, "sono un cagnolino bellissimo")
        #bot.sendPhoto(chat_id, (open('file/foto.jpg', 'rb')))
        

    else:
        bot.sendMessage(chat_id, "scusa, non ho capito.")
        #bot.sendMessage(chat_id, "cosa dovrei rispondere ?")
        #ls[0] = x
        bot.sendMessage(chat_id, "prova a scrivere aiuto")






def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id

    if content_type == "text":
        risposta(chat_id, msg['text'])

bot.message_loop(handle)

while 1:
    time.sleep(3)
