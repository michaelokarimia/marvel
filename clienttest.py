import client
import unittest

class clienttest(unittest.TestCase):

    def test_client_loads_APIKey_Correctly(self):

        subject = client.Client();


        self.assertEqual('Public key: 3ed7f03032576c0b754b5b356266e05b Private key: 766666d17836a85476588539f0fd2cf3fcf5297c', subject.status())

if __name__ == '__main__':
    unittest.main()