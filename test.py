import RPi_I2C_driver
from time import sleep

def display_message_on_lcd(message):
    mylcd = RPi_I2C_driver.lcd()
    mylcd.lcd_display_string(message, 1)
    sleep(2)  # 2-second delay
    mylcd.lcd_clear()
    sleep(1)
    mylcd.backlight(0)

if __name__ == "__main__":
    message = "Hello world"
    display_message_on_lcd(message)
