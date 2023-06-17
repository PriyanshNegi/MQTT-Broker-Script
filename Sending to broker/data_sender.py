import paho.mqtt.client as mqtt
import json

# Define MQTT broker settings
mqtt_broker = "broker.emqx.io"
mqtt_port = 1883

temp_topic = "temp"
speed_topic = "speed"

import time
# Define dataset to be published
import pandas as pd
import datetime

# dataset_list = ['']

df = pd.read_csv('./data/fake_Railway.csv')

response_received = False

def on_message(client, userdata, msg):
    print("Received message: Topic =", msg.topic, ", Payload =", msg.payload.decode())

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed")

# Connect to MQTT broker
client = mqtt.Client()
# client.username_pw_set("guest", "guest")
# client.on_connect = on_connect

client.connect(mqtt_broker, mqtt_port)

for ind in df.index[100:1000]:
    now = datetime.datetime.now()
    today = str(now.isoformat())
    
    time.sleep(10)

    data_temp = {
        "sensor_type": "temp",
        "value": str(df.iloc[ind]['rail_temperature']),
        "time": today,
        "month": f"{now.year}-{now.month}"
    }

    json_dataset_temp = json.dumps(data_temp)
    # Publish dataset to MQTT broker
    client.publish(temp_topic, json_dataset_temp)

    data_speed = {
        "sensor_type": "speed",
        "value": str(df.iloc[ind]['rail_speed']),
        "time": today,
        "month": f"{now.year}-{now.month}"
    }
    
    json_dataset_speed = json.dumps(data_speed)
    # Publish dataset to MQTT broker
    client.publish(speed_topic, json_dataset_speed)

    print(f"published rail-data {ind}")


client.disconnect()