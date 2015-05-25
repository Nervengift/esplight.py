#!/usr/bin/env python3
import socket
import copy
import time
import binascii
import sys
from PIL import Image

IP = "192.168.4.218"
PORT = 6454
WIDTH = 10
HEIGHT = 6

FONT = {"A" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
        "B" : [[0, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 0]],
        "C" : [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]],
        "D" : [[0, 0, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
        "E" : [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        "F" : [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 0, 0]],
        "G" : [[0, 0, 0, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
        "H" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
        "I" : [[0], [1], [1], [1], [1], [1]], 
        "J" : [[0, 0, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]], 
        "K" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]],
        "L" : [[0, 0, 0], [1, 0, 0], [1, 0 ,0], [1, 0, 0], [1, 0, 0], [1, 1, 1]],
        "M" : [[0, 0, 0], [1, 0, 0, 0, 1], [1, 1, 0, 1 ,1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]],
        "N" : [[0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1]],
        "O" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        "P" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 0], [1, 0, 0]],
        "Q" : [[0, 0, 0, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]],
        "R" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]],
        "S" : [[0, 0, 0], [0, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0]],
        "T" : [[0, 0, 0], [1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        "U" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        "V" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
        "W" : [[0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],
        "X" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]],
        "Y" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        "Z" : [[0, 0, 0], [1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
        "1" : [[0, 0, 0], [0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
        "2" : [[0, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        "3" : [[0, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        "4" : [[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        "5" : [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        "6" : [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        "7" : [[0, 0, 0], [1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        "8" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        "9" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        "0" : [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        " " : [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        ":" : [[0], [0], [1], [0], [1], [0]], 
        "." : [[0], [0], [0], [0], [0], [1]], 
        "!" : [[0], [1], [1], [1], [0], [1]], 
        "?" : [[0, 0, 0], [1, 1, 1], [0, 0, 1], [0, 1, 0], [0, 0, 0], [0, 1, 0]],
        "'" : [[0], [1], [1], [0], [0], [0]], 
        "+" : [[0, 0, 0], [0, 0, 0], [0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 0, 0]],
        "-" : [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0]],
        "_" : [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1]],
        "/" : [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0]],
        "|" : [[0], [1], [1], [1], [1], [1]], 
        "=" : [[0, 0, 0], [0, 0, 0], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]],
        "<" : [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
        ">" : [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]],
        "(" : [[0, 0], [0, 1], [1, 0], [1, 0], [1, 0], [0, 1]],
        ")" : [[0, 0], [1, 0], [0, 1], [0, 1], [0, 1], [1, 0]],
        "[" : [[0, 0], [1, 1], [1, 0], [1, 0], [1, 0], [1, 1]],
        "]" : [[0, 0], [1, 1], [0, 1], [0, 1], [0, 1], [1, 1]],
        "*" : [[0], [0], [0], [1], [0], [0]], 
        "~" : [[0], [0], [0], [0], [0], [0]] # 1px empty space
        }

def join(buf1, buf2):
    """ join two buffers """
    if not buf1:
        return buf2
    elif not buf2:
        return buf1
    else:
        length = min(len(buf1), len(buf2))
        buf = [[]]*length
        for i in range(length):
            buf[i] = buf1[i] + buf2[i]
        return buf

def cut(buf, start, end):
    """ return a slice of a buffer from index (x-coord) *start* to index *end* """
    end = min(end, len(buf[0]))
    return [line[start:end] for line in buf]

def render_image(path):
    """ render an image into a buffer (2D array) """
    buf = []
    im = Image.open(path)
    im.draft("RGB", (10, 6))
    im_data = im.getdata()
    line_nr = -1
    width = im.size[0]
    for i in range(len(im_data)):
        if i % width == 0:
            line_nr += 1
            buf.append([])
        buf[line_nr].append(im_data[i])
    return buf

def render_text(text, color=(255, 255, 255)):
    """ render a text into a buffer (2D array) """
    buf = []
    if len(text) == 0:
        return [[], [], [], [], [], []]
    elif len(text) == 1:
        return render_char(text, color)
    return join(join(render_char(text[0], color), render_char("~", color)), render_text(text[1:], color))

def render_char(c, color=(255, 255, 255)):
    """ render a single character
        '~' is a special char for a 1px empty space """
    c = c[0]
    buf = copy.deepcopy(FONT.get(c.upper(), [[], [], [], [], [], []]))
    if buf:
        for x in range(len(buf)):
            for y in range(len(buf[x])):
                if buf[x][y] > 0:
                    buf[x][y] = color;
                else:
                    buf[x][y] = (0, 0, 0);
    return buf

def pad_front(in_buf, padding):
    """ add padding to the front of a buffer """
    buf = []
    for i in range(len(in_buf)):
        buf.append([(0, 0, 0) for x in range(padding)] + in_buf[i])
    return buf

def draw_static(in_buf, sock):
    """ draw the buffer, but don't scroll if it is too long """
    buf = []
    reverse = True
    for line in in_buf:
        if len(line) < WIDTH:
            line += [(0, 0, 0)] * (WIDTH - len(line))
        elif len(line) > WIDTH:
            line = line[0:WIDTH]
        if reverse:
            line = list(reversed(line))
        for pixel in line: #TODO: ordentlich padding
            buf += [pixel[0], pixel[1], pixel[2]] # senden als GRB
        reverse = not reverse
    buf = [int(i/8) for i in buf]
    msg_b = bytes(buf)
    sock.sendto(msg_b, (IP, PORT))

def draw_scroll(in_buf, sock, step_time=1):
    """ draw the buffer and make it scroll, if it is too long """
    if len(in_buf[0]) <= WIDTH:
        draw_static(in_buf, sock)
    else:
        for i in range(len(in_buf[0])+1):
            buf = cut(in_buf, i, WIDTH+i)
            draw_static(buf, sock)
            time.sleep(step_time)

def draw_crawl(in_buf, sock, step_time=1):
    """ draw the buffer and make it scroll through the matrix """
    for i in range(WIDTH - 1):
        buf = pad_front(in_buf, WIDTH - i - 1)
        draw_static(buf, sock)
        time.sleep(step_time)
    for i in range(len(in_buf[0])+1):
        buf = cut(in_buf, i, WIDTH+i)
        draw_static(buf, sock)
        time.sleep(step_time)

def rainbow(sock):
    t = 0
    while 1:
        buf = []
        for y in range(HEIGHT):
            buf.append([])
            for x in range(WIDTH):
                buf[y].append(_wheel(8 * x + 8 * y + t))
        draw_static(buf, sock)
        time.sleep(0.02)
        t += 1

def _wheel(pos):
    pos = pos % 256
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def _usage():
    print("Usage: {} pic|text|statictext|clock|rainbow <path|text>", file=sys.stderr)



if __name__ == "__main__":
    if len(sys.argv) < 2 or (sys.argv[1] in ["pic", "text", "statictext"] and len(sys.argv) < 3):
        _usage()
        sys.exit(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if sys.argv[1] == "pic":
        msg = render_image(sys.argv[2])
        draw_scroll(msg, s)
    elif sys.argv[1] == "text":
        msg = render_text(' '.join(sys.argv[2:]), (0, 255, 255))
        draw_crawl(msg, s, 0.5)
    elif sys.argv[1] == "statictext":
        msg = render_text(' '.join(sys.argv[2:]), (0, 255, 255))
        draw_static(msg, s)
    elif sys.argv[1] == "rainbow":
        rainbow(s)
    elif sys.argv[1] == "clock":
        while 1:
            draw_crawl(render_text(time.strftime("%H:%M"), (255, 100, 0)), s, 0.5)
    s.close()
