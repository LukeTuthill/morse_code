import keyboard
import sys

if len(sys.argv) != 2:
    print("One argument for file name!")
    sys.exit(1)

content = ""

with open(sys.argv[1], 'r') as f:
    content = f.read()

index = 0

def print_key(key):
    global index

    if key.name == 'backspace':
        keyboard.send('backspace')
        index = index - 1
        return
    
    if key.name == 'esc':
        keyboard.unhook_all()
        sys.exit(0)
    
    keyboard.write(content[index])
    index = index + 1
    if index == len(content):
        keyboard.unhook_all()
        sys.exit(0)

keyboard.on_press(print_key, suppress=True)

keyboard.wait()