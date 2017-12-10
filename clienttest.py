import client
import unittest

class clienttest(unittest.TestCase):

    def test_client_APIKey_Can_authenticate(self):

        subject = client.Client()

        status = subject.status()

        self.assertEqual(200, status, status)

if __name__ == '__main__':
    unittest.main()