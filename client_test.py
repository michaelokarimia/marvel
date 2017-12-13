import client
import unittest


class ClientTest(unittest.TestCase):

    def test_client_APIKey_Can_authenticate(self):

        subject = client.Client()

        status = subject.status()

        self.assertEqual(200, status, status)

    def test_can_get_characters(self):

        subject = client.Client()

        result = subject.request('characters')

        self.assertEqual(result['status'], 200)


if __name__ == '__main__':
    unittest.main()