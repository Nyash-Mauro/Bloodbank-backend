from django.test import TestCase
from .models import Donor,Stock

# Create your tests here.

class DonorTestClass(TestCase):
    '''
    Set Up method that creates instance of Donor Class
    '''
    
    def setUp(self):
        self.donor = Donor.objects.create(first_name='John',middle_name='Doe',
                                        last_name='Bond',email='user@example.com',age='50',
                                        gender='male',date_of_birth='01-01-2000',blood_group='AB+',
                                        phone_number='0721123456',location='Nairobi',weight'45'=,
                                        date_registered='10-12-2020')
    def tearDown(self):
        pass

    def test_instance(self):
        """
        Test if instance of Hood
        """
        self.assertIsInstance(self.hood, Hood)


    
