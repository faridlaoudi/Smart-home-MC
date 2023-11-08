import RPi_I2C_driver
import paho.mqtt.client as mqtt
from time import sleep

# MQTT settings
mqtt_broker = "127.0.0.1"
mqtt_topic = "water"

# LCD initialization
mylcd = RPi_I2C_driver.lcd()

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)

# MQTT on_message callback
def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print(f"Received message: {message}")
    mylcd.lcd_clear()  # Clear the LCD screen
    mylcd.lcd_display_string('WATER LEVEL ', 1)
    mylcd.lcd_display_string(message + ' CL', 2)  # Display the message on line 1

if __name__ == "__main__":
    # Create an MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect(mqtt_broker, 1883, 60)

    # Start the MQTT client loop
    client.loop_start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        client.disconnect()
