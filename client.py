#!/usr/bin/python
import http.client
import hashlib
import datetime


apiPublicKey = '3ed7f03032576c0b754b5b356266e05b'

apiSecretPath = './privateKey.txt'

secret = ''
urlroot = 'gateway.marvel.com'

urlpath = '/v1/public/comics?ts={}&apikey={}&hash={}'

class Client:

    def __init__(self):

        secretFile = open(apiSecretPath, 'r', )

        self.secret = secretFile.readline()

        secretFile.close()


    def status(self):

        ts = datetime.datetime.utcnow().toordinal()

        combo = str(ts) + self.secret + apiPublicKey

        m = hashlib.md5()

        m.update(combo.encode('utf-8'))

        hash = m.hexdigest()

        print(hash)

        conn = http.client.HTTPConnection(urlroot, 80)


        reqPath = urlpath.format(ts,apiPublicKey,hash)

        print(urlroot)

        print(reqPath)

        conn.request("GET", reqPath)

        response = conn.getresponse()

        print("status {}, reason {}".format(response.status, response.reason))

        conn.close()

        return response.status

