from django.test import TestCase, Client
from django.urls import reverse


class KafkaProducerTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_publish_message_view_form_data(self):
        url = reverse('publish_message')
        
        data = {
            'topic': 'meu_topico_teste',
            'message': 'mensagem_teste'
        }
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Mensagem publicada com sucesso', response.content.decode())
