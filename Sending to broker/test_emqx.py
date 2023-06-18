import random
import time
import pandas as pd
from paho.mqtt import client as mqtt_client
import json

df = pd.read_csv('./data/fake_Railway.csv')

broker = '--ENTER YOU URL--'
port = 8883
topic = 'dataset'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = '--ENTER USERNAME--'
password = '--ENTER PASSWORD--'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # Set CA certificate
    client.tls_set(ca_certs='emqxsl-ca.crt')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    for ind in df.index[1:]:
        time.sleep(10)
        data = df.iloc[ind].to_dict()
        json_dataset = json.dumps(data)

        # Publish dataset to MQTT broker
        result = client.publish(topic, json_dataset)
        if result[0] == 0:
            print(f"published rail {ind}")
        else:
            print(f"Failed to send message to topic {topic}")
        

    # while True:
    #     time.sleep(1)
    #     msg = f"messages: {msg_count}"
    #     result = client.publish(topic, msg)
    #     # result: [0, 1]
    #     status = result[0]
    #     if status == 0:
    #         print(f"Send `{msg}` to topic `{topic}`")
    #     else:
    #         print(f"Failed to send message to topic {topic}")
    #     msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
