while True:
    try:
        response = irc.recv(2048).decode('utf-8').lower()
        print(response)
        handle_command(irc,response,"temp")