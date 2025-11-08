# Food Sensor Handler for real-time stock monitoring
import paho.mqtt.client as mqtt

BROKER = "mqtt://localhost"
TOPIC = "campusfoods/sensors"

def on_message(client, userdata, msg):
    print(f"[Sensor Data] {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe(TOPIC)
client.on_message = on_message

print("Food sensor monitoring started...")
client.loop_forever()
