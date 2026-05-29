"""WebSocket Events Handler"""
from flask_socketio import emit, join_room, leave_room
from loguru import logger

def setup_websocket_events(socketio):
    """Setup WebSocket event handlers"""
    
    @socketio.on('connect')
    def handle_connect():
        """Handle client connection"""
        logger.info("Client connected")
        emit('connection_response', {'data': 'Connected to Agriautonomous'})
    
    @socketio.on('disconnect')
    def handle_disconnect():
        """Handle client disconnection"""
        logger.info("Client disconnected")
    
    @socketio.on('subscribe_telemetry')
    def handle_subscribe_telemetry(data):
        """Subscribe to asset telemetry"""
        asset_id = data.get('asset_id')
        join_room(f'telemetry_{asset_id}')
        logger.info(f"Subscribed to telemetry: {asset_id}")
        emit('subscription_response', {'asset_id': asset_id, 'subscribed': True})
    
    @socketio.on('request_mission_command')
    def handle_mission_command(data):
        """Handle mission command"""
        mission_id = data.get('mission_id')
        command = data.get('command')
        logger.info(f"Mission command: {command} for {mission_id}")
        emit('mission_response', {'mission_id': mission_id, 'status': 'received'})
    
    @socketio.on('emergency_stop_request')
    def handle_emergency_stop(data):
        """Handle emergency stop request"""
        asset_id = data.get('asset_id')
        logger.critical(f"EMERGENCY STOP requested for {asset_id}")
        emit('emergency_stop_response', {'asset_id': asset_id, 'status': 'executed'}, broadcast=True)
