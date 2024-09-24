import socket
import time
from commands import *
from config import *

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Verbindung zum IRC-Server herstellen
irc.connect((server, port))
# Handshake mit dem IRC-Server
irc.send(f"NICK {nickname}\r\n".encode('utf-8'))
irc.send(f"USER {nickname} 0 * :Python IRC\r\n".encode('utf-8'))

# Warten, bis die Verbindung vollständig ist (Willkommensnachricht 001)
connected = False
while not connected:
    response = irc.recv(2048).decode('utf-8')
    print(response)
    
    if "001" in response:
        connected = True
        print("Verbindung erfolgreich hergestellt!")

    # PONG auf PING schicken, um die Verbindung aufrechtzuerhalten
    if "PING" in response:
        irc.send(f"PONG {response.split()[1]}\r\n".encode('utf-8'))

# Nachdem die Verbindung hergestellt ist, dem Channel beitreten und Nachricht senden
irc.send(f"JOIN {channel}\r\n".encode('utf-8'))
time.sleep(1)  # kurze Pause, um sicherzustellen, dass der Bot dem Channel beigetreten ist
irc.send(f"PRIVMSG {channel} :{message}\r\n".encode('utf-8'))

# Verbindung aktiv halten
while True:
    try:
        response = irc.recv(2048).decode('utf-8').lower()
        print(response)
        priv_msg_handler(irc,response)
        # PING-Nachrichten vom Server beantworten, um die Verbindung aktiv zu halten
        if "PING" in response:
            irc.send(f"PONG {response.split()[1]}\r\n".encode('utf-8'))
    
    except socket.error:
        print("Verbindung verloren.")
        break
