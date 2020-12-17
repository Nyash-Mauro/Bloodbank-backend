from django.test import TestCase
from .models import Donor,Stock

# Create your tests here.

class DonorTestClass(TestCase):
    '''
    Set Up method that creates instance of Donor Class
    Runs before each test
    '''
    
    def setUp(self):
        self.donor = Donor.objects.create(first_name='John',middle_name='Doe',
                                        last_name='Bond',email='user@example.com',age='50',
                                        gender='male',date_of_birth='2000-01-01',blood_group='AB+',
                                        phone_number='0721123456',location='Nairobi',weight='45',
                                        date_registered='10-12-2020')
    def tearDown(self):
        '''
        this tearDown method runs after every test.
        '''
        pass

    def test_instance(self):
        """
        Testing instance to see if self.donor is instance of class Donor.
        """

        self.assertIsInstance(self.donor, Donor)

    def test_save_donor(self):
        '''
        Testing the Save Method on Donor class
        '''
        self.donor.save_donor()
        donors = Donor.objects.all()
        self.assertTrue(len(profiles) > 0)





    
