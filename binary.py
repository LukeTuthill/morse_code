import keyboard

zero_key = '0'
one_key = '1'

count = 0
curr_char = 0

#Value is either 0 or 1
def key_press(value):
    print(value)
    global count, curr_char
    count += 1
    curr_char = (curr_char << 1) + value
    print(curr_char)
    if count == 8:
        print(f"key written: {chr(curr_char)}")
        keyboard.write(chr(curr_char))
        count = 0
        curr_char = 0

keyboard.add_hotkey(zero_key, key_press, args=[0], suppress=True)
keyboard.add_hotkey(one_key, key_press, args=[1], suppress=True)

keyboard.wait()