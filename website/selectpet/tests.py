from django.test import TestCase
from .models import Pet

# Create your tests here.
class PetModelTests(TestCase):
    def setUp(self):
        Pet.objects.create(name = 'chihuahua', hair='short', size='small')
    
    def test_dog_hair_length(Self):
        chi = Pet.objects.get(name='chihuahua')
        self.assertEqual(chi.hair, 'short')