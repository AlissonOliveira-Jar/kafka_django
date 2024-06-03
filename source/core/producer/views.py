from django.http import JsonResponse
from django.shortcuts import render

from .producers import KafkaProducer

def publish_message(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        message = request.POST.get('message')
        
        if not message:
            return JsonResponse({'error': 'Mensagem não pode ser vazia'}, status=400)
        
        producer = KafkaProducer()
        producer.publish_message(topic, message)
        producer.flush()
        
        return JsonResponse({'status': 'Mensagem publicada com sucesso'})
    else:
        return render(request, 'producer/publish_form.html')
