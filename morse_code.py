import keyboard
import time

morse_key = 'a'
hold_delay = 200000000

start_time = 0
key_being_pressed = False

dot = '.'
dash = '-'
dots_and_dashes = str("")

morse_map = {
    ".-" : 'a',
    "-..." : 'b',
    "-.-." : 'c',
    "-.." : 'd',
    "." : 'e',
    "..-." : 'f',
    "--." : 'g',
    "...." : 'h',
    ".." : 'i',
    ".---" : 'j',
    "-.-" : 'k',
    ".-.." : 'l',
    "--" : 'm',
    "-." : 'n',
    "---" : 'o',
    ".--." : 'p',
    "--.-" : 'q',
    ".-." : 'r',
    "..." : 's',
    "-" : 't',
    "..-" : 'u',
    "...-" : 'v',
    ".--" : 'w',
    "-..-" : 'x',
    "-.--" : 'y',
    "--.." : 'z',
    ".----" : '1',
    "..---" : '2',
    "...--" : '3',
    "....-" : '4',
    "....." : '5',
    "-...." : '6',
    "--..." : '7',
    "---.." : '8',
    "----." : '9',
    "-----" : '0',
    ".-.-.-" : '.',
    "--..--" : ',',
    "..--.." : '?',
    "-..-." : '/',
    ".--.-." : '@'
}

#Function is called after a delay
#Only prints key if the array hasn't been updated since
#it was called, meaning no more key strokes have been done
def print_key(num_strokes: int):
    global dots_and_dashes
    if len(dots_and_dashes) != num_strokes:
        return
    keyboard.write(morse_map.get(dots_and_dashes, ''))
    print(dots_and_dashes)
    dots_and_dashes = ""
    
def key_pressed(key=None):
    global start_time, key_being_pressed
    if key_being_pressed:
        return

    start_time = time.perf_counter_ns()
    key_being_pressed = True

def key_released(key=None):
    global key_being_pressed, dots_and_dashes
    key_being_pressed = False

    end_time = time.perf_counter_ns()
    if end_time - start_time > hold_delay:
        print("Held")
        dots_and_dashes += dash
    else:
        print("Tap")
        dots_and_dashes += dot
    keyboard.call_later(print_key, 
        args = ([len(dots_and_dashes)]), delay = 1)

keyboard.add_hotkey(morse_key, key_pressed, suppress=True)
keyboard.on_release_key(morse_key, key_released)

keyboard.wait('esc')