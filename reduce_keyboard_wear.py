import keyboard

count = [0] * 256
presses = 0

def check_and_update_count(key: keyboard.KeyboardEvent):
    val = key.scan_code
    global count, presses
    if count[val] == 5:
        return
    
    if keyboard.is_pressed('shift') and key.name.isalpha():
        keyboard.send(key.name.upper())
    else:
        keyboard.send(keyboard.normalize_name(key.name))

    count[val] = count[val] + 1
    presses = presses + 1

    if presses == 50:
        presses = 0
        count = [0] * 256

keyboard.on_press(check_and_update_count, suppress=True)
keyboard.wait('esc')