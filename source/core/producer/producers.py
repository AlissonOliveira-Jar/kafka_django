from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, servers='kafka:9092'):
        self.producer = Producer({'bootstrap.servers': servers})
        
    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Falha na entrega da menssagem: {err}')
        else:
            print(f'Mensagem entregue no {msg.topic()} [{msg.partition()}]')
            
    def publish_message(self, topic, message):
        self.producer.produce(topic, message.encode('utf-8'), callback=self.delivery_report)
        self.producer.poll(0)
        
    def flush(self):
        self.producer.flush()
