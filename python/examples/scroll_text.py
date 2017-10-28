import sys
import time
import re

from neopixel import *
from constants import alphabet, letter_space, space

WAIT_MS = 75
NUMROWS = 8
NUMCOLS = 32

blue = Color(0, 0, 255)
off = Color(0, 0, 0)

LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2812_STRIP



def write_board(matrix):
    for column, row in enumerate(matrix):
        #flip the column on odd rows to account for how the board is wired
        if column % 2 == 1:
            row = row[::-1]
        for curr_column, curr_row in enumerate(row):
            color = blue if curr_row else off
            current_spot = curr_column + (column -1) * NUMROWS
            strip.setPixelColor(current_spot, color)    
        strip.show()

def rot_ninety(matrx):
    new_matrx = []
    for column_no in range(len(matrx[0])):
        this_arr = []
        for row in matrx:
            this_arr.append(row[column_no])
        new_matrx.append(this_arr)
    return new_matrx


def write_message(matrix, empty, msg):
    blanks = 0
    msg_matrix = []
    for letter in msg:
        for row in rot_ninety(alphabet[letter]):
            msg_matrix.append(row)
            print(row, letter_space)
            msg_matrix.append(letter_space)
    while True:
        write_board(matrix)
        if msg_matrix:
            line = msg_matrix.pop(0)
        else:
            line = empty
            blanks += 1
        if blanks > NUMCOLS
            break
        matrix.pop()
        matrix = [line] + matrix

def get_message():
    message = "Error Reading File"
    with open ("examples/message.txt", "r") as msgFile:
        message = msgFile.read().replace('\n', '')
    message = re.sub(r'^\W+', '', message.lower())
    return message


if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    empty = [0 for row in range(NUMROWS)]
    matrix = [empty for col in range(NUMCOLS)]
    while True:
        msg = get_message()
        write_message(matrix, empty, msg)
        

