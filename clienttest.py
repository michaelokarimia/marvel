import client
import unittest

class clienttest(unittest.TestCase):

    def test_client_APIKey_Can_authenticate(self):

        subject = client.Client()

        status = subject.status()

        self.assertEqual(200, status, status)

    def test_can_get_characters(self):

        subject = client.Client()


        result = subject.request('characters')

        print('Status: {}'.format(result['status']))

        self.assertEqual(result['status'], 200)

        json = result['data']

        print(json)


        self.assertEqual(json, "f")


if __name__ == '__main__':
    unittest.main()