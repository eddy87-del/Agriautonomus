from pymavlink import mavutil

master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

master.wait_heartbeat()
print("Drone Connected")
