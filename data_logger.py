# TODO-DONE: capture data form arduino serial to csv format 
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1107
from time import sleep
from PIL import Image, ImageDraw, ImageFont
import os
import time
import serial
import re

serial_12c = i2c(port=1, address=0x3C)
device = sh1107(serial_12c, rotate=0, width=128)

font_path = os.path.abspath("firacode.ttf")
font_large = ImageFont.truetype(font_path,size=32)
font = ImageFont.truetype(font_path,size=16)

# Create an image with a black background
image = Image.new("1", (device.width, device.height))

4	# Create a drawing context
draw = ImageDraw.Draw(image)
y_pos = 10

def main(args):
    return 0
    
def replace_time(text, timestamp):
    pattern = r"^([^,]*)"
    return re.sub(pattern, str(timestamp), text)
    
if __name__ == '__main__':
    import sys
    #sys.exit(main(sys.argv))
    
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    #ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)

    ser.reset_input_buffer()
    
    # TODO: Open csv file
    # with open("log_data.csv","w", newline="") as file:
    # writer = csv.writer(file)
    # testing
    file = open("log_data.csv","w")
    file.write("Time,ECG,PCG,PPG\n")
    count = 0
    while count < 60000: # 60000 = 1 minute (60 seconds)
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip().replace(" ",",")
            data = replace_time(line, count)
            # TODO: Write to csv file
            #writer.writerow(data)
            file.write(data + "\n")
            print(data)
            # ~ x1, y1 = 0, 0
            # ~ x2, y2 = device.width - 1, device.height - 1
            # ~ draw.rectangle([(x1, y1), (x2, y2)], fill=0)
            # ~ # draw.text(x,y) -> (0,0) top-left
            # ~ draw.text((0, y_pos), "Logging Data..", font=font_large, fill=1)
            # ~ device.display(image)
            # Close file after 1 minutes
            count += 10
    file.close()
    # TODO: send file csv to tflite
