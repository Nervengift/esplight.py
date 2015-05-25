ESPLight.py
===========
A script controlling the [ESPLight](https://github.com/ChaosDarmstadt/esp8266), an ESP8266 and WS2812 based, wifi enabled LED matrix.

Dependencies
============
python3, PIL (python-pillow)

Configuration
=============
* flash [nodemcu](https://github.com/nodemcu/nodemcu-firmware) to your ESP (The firmware needs the WS2812 module enabled, but this is the default as of version 0.9.6-dev)
* configure your wifi settings in *init.lua*
* if you want to get notifications for button presses as UDP packages, configure your IP in line 7 of *init.lua* (else you can delete everything from line 6 down)
* push *init.lua* to your ESP (e.g. using [nodemcu-uploader](https://github.com/kmpm/nodemcu-uploader))
* set your ESP's IP in esplightctl (I'll create commandline flags for that soon)

Usage
=====
```
esplightctl text <text>        # draw a scrolling text
esplightctl statictext <text>  # draw a static text, truncated if too long
esplightctl pic </path/to/pic> # draw a picture, truncated if > 10x6 pixels

esplightctl rainbow            # draw an animated rainbow pattern
esplightctl clock              # draw a scrolling clock
```
