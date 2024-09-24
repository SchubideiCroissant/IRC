from config import *

messages = {
    "!witz": "Hier ist ein Witz: Warum können Geister so schlecht lügen? Weil man durch sie hindurchsehen kann!",
    "!hilfe": "Verfügbare Befehle: !witz, !hilfe, !zeit",
    "!zeit": "Die aktuelle Zeit ist: {schau auf die Uhr}"  # Platzhalter für die Zeit
}


def priv_msg_handler(irc,response):
    if "privmsg" in response:
            user = response.split('!')[0][1:]  # Benutzername extrahieren
            message = response.split(':', 2)[2].strip()  # Die gesamte Nachricht extrahieren
            command = message.split()[0]  # Den ersten Teil der Nachricht als Befehl betrachten
            handle_command(irc,command,user)

def handle_command(irc,command, user):
    print(f"Empfangener Befehl: {command} von {user}")  # Debugging-Ausgabe
    if command in messages:
        send_msg(irc, messages[command]) 

def send_msg(irc, msg):
    message2 = f"PRIVMSG {channel} :{msg}\r\n"  # Wichtig: \r\n am Ende
    irc.send(message2.encode('utf-8'))
    
