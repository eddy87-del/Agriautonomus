"""ROS2 Integration"""
from loguru import logger

class ROS2Node:
    """ROS2 node for UGV"""
    
    def __init__(self, node_name: str):
        self.node_name = node_name
        logger.info(f"Initializing ROS2 node: {node_name}")
    
    def publish(self, topic: str, message):
        """Publish message to ROS2 topic"""
        logger.debug(f"Publishing to {topic}")
    
    def subscribe(self, topic: str, callback):
        """Subscribe to ROS2 topic"""
        logger.debug(f"Subscribing to {topic}")
