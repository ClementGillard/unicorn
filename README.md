# unicorn
Scripts done for the Raspberry Pi Unicorn Hat

hour.py
-------
Uses `scrolldisp.py` to display the time, with rainbows.

rainbow.py
----------
Continuously displays a scrolling rainbow generated using HSV, moving from top
to bottom.

rainbow_appear.py
-----------------
Draws a single rainbow, scrolling from top to bottom, using cosine waves.

clock.py
--------
Displays a clock

cpu.py
------
A system stats tool, similar to `htop`. Displays CPU usage, RAM usage, load, and
CPU temperature. Refreshes every 2 seconds.

* The top 4 lines are for CPU usage. The display will work on 1 to 4 CPUs, 1
line per CPU. Usage grows from left to right. Below 50%, LEDs are green. After
the 50% mark (4 LEDs) they are orange. After the 75% mark (6 LEDs) they are red.
* The 4th line from the bottom is for RAM usage. Usage grows from left to right.
Mapped memory is shown in green, actually used memory is shown in orange.
* In the bottom right hand corner, a 3 high times 4 wide display is used for
load. Lines from bottom to top correspond to load average over 1, 5, and 15
minutes. Lines grow from right to left. They are green when load is below half
the number of CPUs, orange when below the number of CPUs, red when above.
* In the bottom left hand corner, a 2 by 2 square is used to display
temperature. Color is solid over the square. The color is in HSV, with hue being
240 - 3 * temperature in Celsius, which gives:
  * 0°C => blue
  * 20°C => cyan
  * 40°C => green
  * 60°C => yellow
  * 80°C => red
  * above 80° => magenta, then blue, then cycles back...but your Raspberry Pi
will probably be dead by then!

scrolldisp.py
-------------
A library to make text scroll on the Unicorn. Due to the way I implemented it,
`unicorn.rotation(0)` makes display upside down, USB and Ethernet port pointing 
upwards. But, as I do not override it, you can choose the rotation of display
however you want.

Contains a class, ScrollDisp, and a function, Display. Use

    import scrolldisp
    disp = scrolldisp.ScrollDisp()
    scrolldisp.Display("some text")

or

    from scrolldisp import *
    disp = ScrollDisp()
    Display("some text")

You could also call it form the command line, it would feed the arguments to
Display.

**Functions**

    disp = ScrollDisp(text)
  
Creates a new `ScrollDisp` object and sets its buffer to `text` (optional).

    disp.set_text(text, color)

Clears and sets the buffer for `disp` to `text`. `color` is a standard unicorn
RGB tuple, default is (255,255,255) (white).

    disp.start(delay)
  
Makes the buffer for `disp` scroll on unicorn. `time.sleep(delay)` is called
between each frame. Default delay is 0.1 and scrolls text smoothly.

    Display(text, color, delay)

Executes all the above, with the default values if omitted, without having to
instanciate a ScrollDisp.

**Supported characters**

* Uppercase and lowercase letters
* All digits
* Special characters: `!'(),-.:[]_` and space
* Escape sequences: Implementation allows for escape sequences starting with `~`
(tilde). Currently, the only escape sequence implemented is:
  * `~R`: Draws a rainbow generated using cosine waves (see `rainbow_appear.py`) 

**Special Notes:** all characters will append a 1-led wide gap before them.
However, the ~R rainbow will not, so that you can append multiple rainbows
continuously.  If you plan on putting a rainbow after a character, explicitely
put a space before the ~R (example: `~Ra ~R` will display a rainbow, a 1 wide
gap, an 'a', a 1 wide gap, and a rainbow).

Any unknown character will be displayed as a white vertical line and print an
error message in the console.  You can add your own characters by editing
`scrolldisp.py`.
