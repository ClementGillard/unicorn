#!/usr/bin/python3
# scrolling rainbows and text
# to be used as a lib
# when executed, just Display() the arguments

import unicornhat as u
import time, math, sys

class ScrollDisp:
    columns = []
    mappings = {'!': [" ",
                      "#",
                      "#",
                      "#",
                      "#",
                      " ",
                      "#",
                      " "],
                '\'': [" ",
                      "#",
                      "#",
                      " ",
                      " ",
                      " ",
                      " ",
                      " "],
                '(': ["  ",
                      " #",
                      "# ",
                      "# ",
                      "# ",
                      "# ",
                      " #",
                      "  "],
                ')': ["  ",
                      "# ",
                      " #",
                      " #",
                      " #",
                      " #",
                      "# ",
                      "  "],
                ',': ["  ",
                      "  ",
                      "  ",
                      "  ",
                      "  ",
                      "  ",
                      " #",
                      "# "],
                '-': ["   ",
                      "   ",
                      "   ",
                      "   ",
                      "###",
                      "   ",
                      "   ",
                      "   "],
                '.': [" ",
                      " ",
                      " ",
                      " ",
                      " ",
                      " ",
                      "#",
                      " "],
                '0': ["    ",
                      " ## ",
                      "#  #",
                      "#  #",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                '1': ["   ",
                      " # ",
                      "## ",
                      " # ",
                      " # ",
                      " # ",
                      "###",
                      "   "],
                '2': ["    ",
                      " ## ",
                      "#  #",
                      "   #",
                      "  # ",
                      " #  ",
                      "####",
                      "    "],
                '3': ["    ",
                      "####",
                      "   #",
                      "  # ",
                      "   #",
                      "#  #",
                      " ## ",
                      "    "],
                '4': ["    ",
                      "#  #",
                      "#  #",
                      "####",
                      "   #",
                      "   #",
                      "   #",
                      "    "],
                '5': ["    ",
                      "####",
                      "#   ",
                      "### ",
                      "   #",
                      "#  #",
                      " ## ",
                      "    "],
                '6': ["    ",
                      " ## ",
                      "#   ",
                      "### ",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                '7': ["    ",
                      "####",
                      "   #",
                      "  # ",
                      "  # ",
                      " #  ",
                      " #  ",
                      "    "],
                '8': ["    ",
                      " ## ",
                      "#  #",
                      " ## ",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                '9': ["    ",
                      " ## ",
                      "#  #",
                      " ###",
                      "   #",
                      "   #",
                      " ## ",
                      "    "],
                ':': [" ",
                      " ",
                      " ",
                      "#",
                      " ",
                      " ",
                      "#",
                      " "],
                'A': ["    ",
                      " ## ",
                      "#  #",
                      "#  #",
                      "####",
                      "#  #",
                      "#  #",
                      "    "],
                'B': ["    ",
                      "### ",
                      "#  #",
                      "### ",
                      "#  #",
                      "#  #",
                      "### ",
                      "    "],
                'C': ["    ",
                      " ## ",
                      "#  #",
                      "#   ",
                      "#   ",
                      "#  #",
                      " ## ",
                      "    "],
                'D': ["    ",
                      "### ",
                      "#  #",
                      "#  #",
                      "#  #",
                      "#  #",
                      "### ",
                      "    "],
                'E': ["    ",
                      "####",
                      "#   ",
                      "### ",
                      "#   ",
                      "#   ",
                      "####",
                      "    "],
                'F': ["    ",
                      "####",
                      "#   ",
                      "### ",
                      "#   ",
                      "#   ",
                      "#   ",
                      "    "],
                'G': ["    ",
                      " ## ",
                      "#  #",
                      "#   ",
                      "# ##",
                      "#  #",
                      " ## ",
                      "    "],
                'H': ["    ",
                      "#  #",
                      "#  #",
                      "####",
                      "#  #",
                      "#  #",
                      "#  #",
                      "    "],
                'I': ["   ",
                      "###",
                      " # ",
                      " # ",
                      " # ",
                      " # ",
                      "###",
                      "   "],
                'J': ["    ",
                      " ###",
                      "   #",
                      "   #",
                      "   #",
                      "#  #",
                      " ## ",
                      "    "],
                'K': ["    ",
                      "#  #",
                      "# # ",
                      "##  ",
                      "##  ",
                      "# # ",
                      "#  #",
                      "    "],
                'L': ["   ",
                      "#  ",
                      "#  ",
                      "#  ",
                      "#  ",
                      "#  ",
                      "###",
                      "   "],
                'M': ["     ",
                      "#   #",
                      "## ##",
                      "# # #",
                      "#   #",
                      "#   #",
                      "#   #",
                      "     "],
                'N': ["     ",
                      "#   #",
                      "##  #",
                      "# # #",
                      "#  ##",
                      "#   #",
                      "#   #",
                      "     "],
                'O': ["    ",
                      " ## ",
                      "#  #",
                      "#  #",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                'P': ["    ",
                      "### ",
                      "#  #",
                      "### ",
                      "#   ",
                      "#   ",
                      "#   ",
                      "    "],
                'Q': ["    ",
                      " ## ",
                      "#  #",
                      "#  #",
                      "#  #",
                      "# # ",
                      " # #",
                      "    "],
                'R': ["    ",
                      "### ",
                      "#  #",
                      "### ",
                      "##  ",
                      "# # ",
                      "#  #",
                      "    "],
                'S': ["    ",
                      " ###",
                      "#   ",
                      " #  ",
                      "  # ",
                      "   #",
                      "### ",
                      "    "],
                'T': ["     ",
                      "#####",
                      "  #  ",
                      "  #  ",
                      "  #  ",
                      "  #  ",
                      "  #  ",
                      "     "],
                'U': ["    ",
                      "#  #",
                      "#  #",
                      "#  #",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                'V': ["     ",
                      "#   #",
                      "#   #",
                      "#   #",
                      " # # ",
                      " # # ",
                      "  #  ",
                      "     "],
                'W': ["     ",
                      "#   #",
                      "#   #",
                      "#   #",
                      "# # #",
                      "## ##",
                      "#   #",
                      "     "],
                'X': ["   ",
                      "# #",
                      "# #",
                      " # ",
                      " # ",
                      "# #",
                      "# #",
                      "   "],
                'Y': ["     ",
                      "#   #",
                      "#   #",
                      " # # ",
                      "  #  ",
                      "  #  ",
                      "  #  ",
                      "     "],
                'Z': ["    ",
                      "####",
                      "   #",
                      "  # ",
                      " #  ",
                      "#   ",
                      "####",
                      "    "],
                '[': ["  ",
                      "##",
                      "# ",
                      "# ",
                      "# ",
                      "# ",
                      "##",
                      "  "],
                ']': ["  ",
                      "##",
                      " #",
                      " #",
                      " #",
                      " #",
                      "##",
                      "  "],
                '_': ["    ",
                      "    ",
                      "    ",
                      "    ",
                      "    ",
                      "    ",
                      "    ",
                      "####"],
                'a': ["    ",
                      "    ",
                      " ## ",
                      "   #",
                      " ###",
                      "#  #",
                      " ###",
                      "    "],
                'b': ["    ",
                      "#   ",
                      "#   ",
                      "### ",
                      "#  #",
                      "#  #",
                      "### ",
                      "    "],
                'c': ["    ",
                      "    ",
                      " ## ",
                      "#  #",
                      "#   ",
                      "#  #",
                      " ## ",
                      "    "],
                'd': ["    ",
                      "   #",
                      "   #",
                      " ###",
                      "#  #",
                      "#  #",
                      " ###",
                      "    "],
                'e': ["    ",
                      "    ",
                      " ## ",
                      "#  #",
                      "####",
                      "#   ",
                      " ## ",
                      "    "],
                'f': ["    ",
                      " ## ",
                      "#  #",
                      "#   ",
                      "##  ",
                      "#   ",
                      "#   ",
                      "    "],
                'g': ["    ",
                      "    ",
                      " ## ",
                      "#  #",
                      " ###",
                      "   #",
                      "### ",
                      "    "],
                'h': ["    ",
                      "#   ",
                      "#   ",
                      "# # ",
                      "## #",
                      "#  #",
                      "#  #",
                      "    "],
                'i': ["   ",
                      " # ",
                      "   ",
                      "## ",
                      " # ",
                      " # ",
                      "###",
                      "   "],
                'j': ["   ",
                      "  #",
                      "   ",
                      "  #",
                      "  #",
                      "  #",
                      "# #",
                      " # "],
                'k': ["    ",
                      "#   ",
                      "#  #",
                      "# # ",
                      "##  ",
                      "# # ",
                      "#  #",
                      "    "],
                'l': ["   ",
                      "## ",
                      " # ",
                      " # ",
                      " # ",
                      " # ",
                      "###",
                      "   "],
                'm': ["     ",
                      "     ",
                      "## # ",
                      "# # #",
                      "#   #",
                      "#   #",
                      "#   #",
                      "     "],
                'n': ["     ",
                      "     ",
                      "#### ",
                      "#   #",
                      "#   #",
                      "#   #",
                      "#   #",
                      "     "],
                'o': ["    ",
                      "    ",
                      " ## ",
                      "#  #",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                'p': ["    ",
                      "    ",
                      "### ",
                      "#  #",
                      "#  #",
                      "### ",
                      "#   ",
                      "#   "],
                'q': ["    ",
                      "    ",
                      " ###",
                      "#  #",
                      "#  #",
                      " ###",
                      "   #",
                      "   #"],
                'r': ["    ",
                      "    ",
                      "# ##",
                      "##  ",
                      "#   ",
                      "#   ",
                      "#   ",
                      "    "],
                's': ["    ",
                      "    ",
                      " ###",
                      "#   ",
                      " ## ",
                      "   #",
                      "### ",
                      "    "],
                't': ["    ",
                      " #  ",
                      "####",
                      " #  ",
                      " #  ",
                      " #  ",
                      "  ##",
                      "    "],
                'u': ["    ",
                      "    ",
                      "#  #",
                      "#  #",
                      "#  #",
                      "#  #",
                      " ## ",
                      "    "],
                'v': ["     ",
                      "     ",
                      "#   #",
                      "#   #",
                      " # # ",
                      " # # ",
                      "  #  ",
                      "     "],
                'w': ["     ",
                      "     ",
                      "#   #",
                      "#   #",
                      "# # #",
                      "# # #",
                      " # # ",
                      "     "],
                'x': ["    ",
                      "    ",
                      "#  #",
                      "#  #",
                      " ## ",
                      "#  #",
                      "#  #",
                      "    "],
                'y': ["    ",
                      "    ",
                      "#  #",
                      "#  #",
                      " ###",
                      "   #",
                      "#  #",
                      " ## "],
                'z': ["     ",
                      "     ",
                      "#####",
                      "   # ",
                      "  #  ",
                      " #   ",
                      "#####",
                      "     "],
               }

    def append_mapping(self, char, color):
        self.append_space()
        bitmap = self.mappings[char]
        n = len(bitmap[0]) 
        for x in range(n):
            self.columns.append([(color if bitmap[7 - i][x] == '#' else (0,0,0)) for i in range(8)])
                
    def append_rainbow(self):
        for x in range(8):
            r = int((math.cos(x * math.pi / 4) + 1) * 127)
            g = int((math.cos((x - 8.0 / 3.0) * math.pi / 4) + 1) * 127)
            b = int((math.cos((x + 8.0 / 3.0) * math.pi / 4) + 1) * 127)
            self.columns.append([(r,g,b) for i in range(8)])

    def append_space(self, n=1):
        for x in range(n):
            self.columns.append([(0,0,0) for i in range(8)])

    def append_buffer(self):
        self.append_space(8)

    def append_letter(self, char, color=None):
        if char == ' ':
            self.append_space(2)
        elif char == 0:
            self.append_rainbow()
        elif char in self.mappings.keys():
            self.append_mapping(char, color)
        else:
            self.columns.append([(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)])
            print("unknown char {0} ({1})".format(char, ord(char)))

    def append_string(self, text, color=(255,255,255)):
        i = 0
        while i < len(text):
            if text[i] == '~':
                i += 1
                if text[i] == 'R': #rainbow
                    self.append_letter(0)
            else:
                self.append_letter(text[i], color)
            i += 1

    def set_text(self, text, color=(255,255,255)):
        self.columns = []
        self.append_buffer()
        self.append_string(text)
        self.append_buffer()

    def __init__(self, text=""):
        self.set_text(text)
        
    def start(self, delay=0.1):
        for x in range(len(self.columns) - 8):
            u.set_pixels(self.columns[x:x+8])
            u.show()
            time.sleep(delay)

def Display(text, color=(255,255,255), delay=0.1):
    disp = ScrollDisp()
    disp.set_text(text, color)
    disp.start(delay)

if __name__ == '__main__':
    u.brightness(0.5)
    Display(' '.join(sys.argv[1:]))
