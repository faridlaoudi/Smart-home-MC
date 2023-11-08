import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

# MQTT settings
mqtt_broker = "127.0.0.1"
mqtt_topic_irrigation = "irrigation"

# Set up GPIO for analog input
analog_pin = 23  # GPIO 23 (pin 16) for analog input

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Read and publish analog values
def read_and_publish_analog_values():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(analog_pin, GPIO.IN)

    client = mqtt.Client()
    client.on_connect = on_connect

    # Connect to the MQTT broker
    client.connect(mqtt_broker, 1883, 60)
    client.loop_start()

    try:
        while True:
            # Read the analog value from GPIO
            analog_value = GPIO.input(analog_pin)

            # Publish the analog value to the "irrigation" topic
            client.publish(mqtt_topic_irrigation, str(analog_value))
            sleep(1)

    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    # Create a new thread for reading and publishing analog values
    import threading
    analog_thread = threading.Thread(target=read_and_publish_analog_values)
    analog_thread.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass
