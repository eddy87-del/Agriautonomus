import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "agriautonomous/telemetry"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

def send_telemetry(data):
    payload = json.dumps(data)
    client.publish(TOPIC, payload)
