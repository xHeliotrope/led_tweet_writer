

import sys
import time

from neopixel import *
from constants import alphabet, letterSpace, space

WAIT_MS = 75
NUMROWS = 8
NUMCOLS = 32

blue = Color(0, 0, 255)
off = Color(0, 0, 0)

LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2812_STRIP


def messageScroll(seconds, strip):
    message = "Error Reading File"
    with open ("examples/message.txt", "r") as msgFile:
        message = msgFile.read().replace('\n', '')
    message = message.lower()
    ledArr = [[] for row in range(NUMROWS)]
    loc = 0


def write_board(matrix):
    time.sleep(1)
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
        for row in matrix:
            this_arr.append(row[column_no])
        new_matrx.append(this_arr)
    return new_matrx


if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    matrix = [[0 for row in range(NUMROWS)] for col in range(NUMCOLS)]
    #line = [1 for row in range(NUMROWS)]
    line = [1,1,1,1,0,0,0,0]
    empty = [0 for row in range(NUMROWS)]
    matrix.pop()
    matrix = [line] + matrix
    while True:
        write_board(matrix)
        print(alphabet["a"])
        matrix.pop()
        matrix = [empty] + matrix

