from django.test import TestCase
from .models import Profile,Blood_stock

# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    Set Up method that creates instance of Profile Class
    Runs before each test
    '''
    
    def setUp(self):
        self.profile = Profile.objects.create(first_name='John',middle_name='Doe',
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
        Testing instance to see if self.profile is instance of class Profile.
        """

        self.assertIsInstance(self.profile, Profile)

    def test_save_profile(self):
        '''
        Testing the Save Method on Profile class
        '''
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_profile_update(self):
        """
        TestCase to check if profile email is updated
        """
        self.profile.save_profile()
        self.profile.email_update('user2@example.com')
        self.assertEqual(self.profile.email, 'user2@example.com')

    def test_delete_profile(self):
        """
        TestCase to check if method deletes a profile instance
        """
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class Blood_stockTestClass(TestCase):
    '''
    Set Up method that creates instance of Blood_stock Class
    Runs before each test
    '''
    
    def setUp(self):
        self.stock = Blood_stock.objects.create(blood_type ='AB+',hospital_name='hospital',blood_volume='7.00')

    def tearDown(self):
        '''
        this tearDown method runs after every test.
        '''
        pass

    def test_instance(self):
        """
        Testing instance to see if self.stock is instance of class Blood_stock.
        """

        self.assertIsInstance(self.stock, Blood_stock)

    def test_save_blood_stock(self):
        '''
        Testing the Save Method on Profile class
        '''
        self.stock.save_bloodstock()
        stocks = Blood_stock.objects.all()
        self.assertTrue(len(stocks) > 0)


    def test_stock_update(self):
        """
        TestCase to check if profile email is updated
        """
        self.stock.save_bloodstock()
        self.stock.blood_volume_update('10.00')
        self.assertEqual(self.stock.blood_volume, '10.00')



    







    
