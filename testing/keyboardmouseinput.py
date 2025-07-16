from pynput import keyboard
from pynput import mouse

# file to log too love logs
LOG_FILE = "testing/input_log.txt"

# clear txt file (testing)
with open(LOG_FILE, "w") as f:
    pass

# keyboard 
def KeyboardInput(key):
    with open(LOG_FILE, "a") as f:
            f.write(f"[{key}]\n")
            print(f"[{key}]")

# mouse
def MouseInput(x, y, button, pressed):
    if pressed:
        with open(LOG_FILE, "a") as f:
            f.write(f"{button.name}\n")
            print(f"{button.name}")

if __name__ == "__main__":
    
    # call keyboard and mouse input functions on press
    keyboard_listener = keyboard.Listener(on_press=KeyboardInput)
    mouse_listener = mouse.Listener(on_click=MouseInput)

    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()