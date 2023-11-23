from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
# Create your tests here.

class UserProfileTest(TestCase):
    def test_something(self):
        # Create a test instance of the User model
        user = User.objects.create(username="testuser")

        # Create a test instance of the UserProfile model
        instance = UserProfile.objects.create(user=user,)
        
        # Perform assertions to check if the expected behavior is met
        self.assertEqual(instance.user, user)
    
