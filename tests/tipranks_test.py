import unittest
import boto3

from tipranks import TipRanks


class MyTestCase(unittest.TestCase):
    client = None
    def setUp(self):
        if not(self.client):
            ssm_client = boto3.client('ssm')
            email = ssm_client.get_parameter(Name='/side-hustle/tipranks/email')['Parameter']['Value']
            password = ssm_client.get_parameter(Name='/side-hustle/tipranks/password', WithDecryption=True)['Parameter'][
                'Value']
            try:
                self.client = TipRanks(email=email, password=password)
            except Exception as err:
                pass




if __name__ == '__main__':
    unittest.main()
