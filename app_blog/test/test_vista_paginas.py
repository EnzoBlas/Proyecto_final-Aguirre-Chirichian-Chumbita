from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """La página de inicio carga correctmente"""
        response = self.client.get('//home.html')
        self.assertEqual(response.status_code, 200)

class ViewsTestCase2(TestCase):
    def test_index_loads_properly(self):
        """La página de publicaciones carga correctmente"""
        response = self.client.get('//post_list.html')
        self.assertEqual(response.status_code, 200)

class ViewsTestCase3(TestCase):
    def test_index_loads_properly(self):
        """La página de mensajes carga correctmente"""
        response = self.client.get('//message_list.html')
        self.assertEqual(response.status_code, 200)
