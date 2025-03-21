from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact

class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_about_us_view(self):
        response = self.client.get(reverse('core:about-us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about-us.html')

    def test_contact_form(self):
        # Test GET request
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

        # Test POST request
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('core:contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if contact was created
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'Test User')
        self.assertEqual(contact.email, 'test@example.com')

class ContactModelTestCase(TestCase):
    def test_contact_creation(self):
        contact = Contact.objects.create(
            name='Test User',
            email='test@example.com',
            subject='Test Subject',
            message='This is a test message'
        )
        self.assertEqual(str(contact), 'Test User - Test Subject')