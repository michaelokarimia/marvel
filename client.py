#!/usr/bin/python


apiPublicKey = '3ed7f03032576c0b754b5b356266e05b'

apiSecretPath = './privateKey.txt'

class Client:

    def getAllCharacters(self):

        secretFile = open(apiSecretPath, 'r')

        secret = secretFile.readline()

        print("Public key: " + apiPublicKey)
        print("Private key: " + secret)


Client.getAllCharacters(Client)