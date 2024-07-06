<h1>Automation Scripts</h1>
A simple set of scripts that can be used Used to automate simple keyboard and mouse event based tasks.
Scripts are written in a pseudo programming language, specified below
<h3>Usage</h3>


Most scripts will wait until you press ctrl+shift+b to begin execution. This is to give you time to load up
audacity

Keyboards and mouse events are controlled by a text encoded script file. To execute a script either:

Run Main.py with the script file path passed as a parameter. This path can be relative to Main.py or absolute.
So, for example:

    python Main.py RunConfigurations/LowPassFilter.txt
and

    python Main.py C:\Users\USER123\AudacityAutomator\RunConfigurations\LowPassFilter.txt
are both valid ways of referencing a script file.

**OR**

Do not pass any parameters and you will then be prompted to enter a file path
in the console. This path may be relative to Main.py or absolute.

## API

- **TYPE** *text*
- **PRESS** *hotkey*
- **WAIT** *millis*
- **WAITFOR** *hotkey*
- **PRESSSCAN** *scanCode*
- **PRESSEDTYPE** *text*
- **CLICK** *x y*

**NOTE:** It is good practice to place a WAITFOR, with the shortcut ctrl+alt+b to give the user time to
load up audacity and then use the shortcut to begin execution


---

### TYPE *text*

*Specified by*: [Keyboard](https://github.com/boppreh/keyboard).write(text) 

Simulates key events as if typing on the keyboard

`text`: Text to type

Example:

    TYPE Hello!
will type 'Hello!'

---

### TYPEPATH *path*

*Specified by*: [Keyboard](https://github.com/boppreh/keyboard).write(text) 

Allows use of typing absolute paths into applications without needing to specify an
absolute path in the script. The script must enter a path relative to Main.py. TYPEPATH
will convert the relative path to absolute.

`path`: Path of a file relative to Main.py

Example:

    TYPEPATH Audios/Default.mp3
Given that Main.py is located at 'C:\Users\USER123\Example\AudacityAutomator':
'C:\Users\USER123\Example\AudacityAutomator\Audios\Default.mp3' will be typed

---

### PRESS *hotkey*

*Specified by*: [Keyboard](https://github.com/boppreh/keyboard).send(hotkey)

Presses hotkeys down together and then releases them. This is generally used for shortcuts

`hotkey`: key combination to press

Example:

    PRESS ctrl+shift+s
will trigger ctrl+shift+s

---

### PRESSSCAN *scanCode*

*Specified by*: [Keyboard](https://github.com/boppreh/keyboard).send(hotkey)

Presses the key that is relevant to the provided scan code. This
is helpful for when pressing a key with no textual representation EG: arrow keys.

**Note**: Scan key mappings are system dependant

`hotkey`: key combination to press

Example:

    PRESSSCAN 77
will press the right arrow key.

---

### PRESSEDTYPE *text*

*Specified by*: [Keyboard](https://github.com/boppreh/keyboard).send(hotkey)

An alternative to the TYPE operation for cases where an application does not
accept keys pressed through the TYPE operation.

`text`: the keys to press.

Example:

    PRESSSEDTYPE hello
will type 'hello'.

---

### WAITFOR *hotkey*

*Specified by*: [Keyboard](https://github.com/boppreh/keyboard).wait(hotkey)

Holds execution until the provided hotkey is pressed. It is highly recommended that you 
place one of these at the start of a script to only execute when you are ready by pressing 
the hotkey

`hotkey`: the hotkey required to resume execution

Example:

    WAITFOR ctrl+shift+b
will wait until ctrl+shift+b is pressed

---

### CLICK *x y*

*Specified by*: [Mouse](https://github.com/boppreh/mouse).click(button)
*and*  [Mouse](https://github.com/boppreh/mouse).move(x,y)

Moves the mouse to the specified position and left clicks.
**WARNING**: Using this function is highly discouraged and should only be used where keyboard based events cannot complete the operation. This is because
very small changes such as screen size can cause the mouse to click in the wrong area!

`x`: the x position to click on
`y`: the y position to click on

Example:

    CLICK 27 103
will left click at x:27 y:103


---

### WAIT *millis*

Holds operations for the specified time in milliseconds

`millis`: Time to hold program in seconds 

Example:

    WAIT 1000
will pause execution for 1 seconds



### Comment
Comments are marked by a '//' at the start of a line. All text on that line will be discarded during execution.
There must be a space between '//' and the comment.
Comments may not start halfway through the line.

### Attribution
This project includes the [Mouse](https://github.com/boppreh/mouse) and
[Keyboard](https://github.com/boppreh/keyboard) libraries 
Licenced under the [MIT LICENCE](https://mit-license.org/)
