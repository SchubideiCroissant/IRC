from config import *
from APIs.pokemon import *
from APIs.weather import *

messages = {
    "!witz": "Hier ist ein Witz: Warum können Geister so schlecht lügen? Weil man durch sie hindurchsehen kann!",
    "!hilfe": "Verfügbare Befehle: !witz, !hilfe, !zeit, !pokemon [pkmn_name] (nur engl Namen), !weather [Stadtname]" ,
    "!zeit": "Die aktuelle Zeit ist: {schau auf die Uhr}"  # Platzhalter für die Zeit
}


def priv_msg_handler(irc, response):
    if "privmsg" in response:
        user = response.split('!')[0][1:]  # Benutzername extrahieren
        message = response.split(':', 2)[2].strip()  # Die gesamte Nachricht hinter ':' extrahieren
        command_parts = message.split()  # Die Nachricht in Teile aufteilen
        command = command_parts[0]  # Den ersten Teil als Befehl betrachten
        arguments = command_parts[1:]  # Alle anderen Teile als Argumente betrachten
        handle_command(irc, command, user, arguments)  # Argumente übergeben
        print(command, arguments)  # Ausgabe von Befehl und Argumenten

def handle_command(irc, command, user, arguments):
    if command == "!pokemon" and arguments:
        pokemon_name = arguments[0]  # Das erste Argument als Pokémon-Namen verwenden
        pokemon_info = get_pokemon_info(pokemon_name)
        send_msg(irc, pokemon_info)
    elif command == "!weather" and arguments:
        city_name = arguments[0]  # Das erste Argument als Pokémon-Namen verwenden
        city_info = get_weather(city_name)
        send_msg(irc, city_info)

    elif command in messages:
        send_msg(irc, messages[command])


def send_msg(irc, msg):
    message2 = f"PRIVMSG {channel} :{msg}\r\n"  # Wichtig: \r\n am Ende
    irc.send(message2.encode('utf-8'))
    
