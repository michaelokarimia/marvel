#!/usr/bin/python


apiPublicKey = '3ed7f03032576c0b754b5b356266e05b'

apiSecretPath = './privateKey.txt'

secret = ''

class Client:

    def __init__(self):

        secretFile = open(apiSecretPath, 'r')

        self.secret = secretFile.readline()

        secretFile.close()


    def status(self):
        return "Public key: {} Private key: {}".format(apiPublicKey, self.secret)