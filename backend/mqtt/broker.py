"""MQTT Handler"""
import paho.mqtt.client as mqtt
from loguru import logger
import os
import json

class MQTTBroker:
    """MQTT broker interface"""
    
    def __init__(self):
        self.client = mqtt.Client()
        self.is_connected = False
        self.setup_callbacks()
    
    def setup_callbacks(self):
        """Setup MQTT callbacks"""
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.on_message = self._on_message
    
    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.is_connected = True
            logger.info("MQTT broker connected")
            # Subscribe to topics
            client.subscribe("telemetry/#")
            client.subscribe("commands/#")
        else:
            logger.error(f"MQTT connection failed with code {rc}")
    
    def _on_disconnect(self, client, userdata, rc):
        self.is_connected = False
        logger.warning(f"MQTT disconnected with code {rc}")
    
    def _on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            logger.debug(f"MQTT message: {msg.topic}")
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")
    
    def connect(self):
        """Connect to MQTT broker"""
        try:
            host = os.getenv('MQTT_BROKER_HOST', 'localhost')
            port = int(os.getenv('MQTT_BROKER_PORT', 1883))
            self.client.connect(host, port, keepalive=60)
            self.client.loop_start()
            logger.info(f"Connecting to MQTT broker at {host}:{port}")
        except Exception as e:
            logger.error(f"MQTT connection error: {e}")
    
    def publish(self, topic: str, payload: dict):
        """Publish message to MQTT broker"""
        try:
            self.client.publish(topic, json.dumps(payload))
        except Exception as e:
            logger.error(f"MQTT publish error: {e}")
    
    def disconnect(self):
        """Disconnect from MQTT broker"""
        self.client.loop_stop()
        self.client.disconnect()

mqtt_broker = MQTTBroker()
