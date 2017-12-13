#!/usr/bin/python
import http.client
import hashlib
import datetime

apiPublicKey = '3ed7f03032576c0b754b5b356266e05b'

apiSecretPath = './privateKey.txt'

secret = ''
urlroot = 'gateway.marvel.com'

urlpath = '/v1/public/{}?limit={}&offset={}&ts={}&apikey={}&hash={}'

class Client:

    def __init__(self):

        secretFile = open(apiSecretPath, 'r', )

        self.secret = secretFile.readline()

        secretFile.close()


    def status(self):

        endpoint = 'comics'

        response = self.request(endpoint)

        return response['status']

    def request(self, endpoint, limit=1, offset=0):

        ts = datetime.datetime.utcnow().toordinal()

        combo = str(ts) + self.secret + apiPublicKey

        m = hashlib.md5()

        m.update(combo.encode('utf-8'))

        hash = m.hexdigest()

        conn = http.client.HTTPConnection(urlroot, 80)

        reqPath = urlpath.format(endpoint, limit, offset, ts, apiPublicKey, hash)



        try:

            conn.request("GET", reqPath)

            response = conn.getresponse()

            if response.status != 200:
                raise ValueError('Non-200 HTTP response when requesting url {}'.format(reqPath))

            data = None

            while not response.closed:
                data = response.readall()
                response.close()

            result = { 'status': response.status, 'reponse' : response, 'data': data.decode()}

            conn.close()

        except:
            raise ValueError('Exception when making HTTP request url {}'.format(reqPath))
        return result

