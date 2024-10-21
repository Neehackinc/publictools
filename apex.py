/*
  Disclaimer: The tool below is for educational and practice purposes only, we are not responsible for any harm caused.
  Author: Neehack, Abdul
*/

from pynput import mouse, keyboard
import time
import threading

# Initialize the Controller object for keyboard
keyboard_controller = keyboard.Controller()

f_pressed = 0
cancel_reset = 0
counter = 0
event_time = 0

# Define a function to be called when the mouse wheel is scrolled
def on_scroll(x, y, dx, dy):
    global f_pressed
    global cancel_reset
    global counter
    global event_time
    try:
        if dy < 0 and f_pressed == 1:  # dy < 0 indicates scrolling downwards
            #print("Gliding #"+str(counter))
            # Press and release the space bar instantly
            keyboard_controller.press(keyboard.Key.space)
            keyboard_controller.release(keyboard.Key.space)
            
            # Wait for 3 milliseconds (adjust timing as needed)
            time.sleep(0.0042)
            
            # Press and release the left Ctrl key
            keyboard_controller.press(keyboard.Key.ctrl_l)
            keyboard_controller.release(keyboard.Key.ctrl_l)
            counter += 1
    except AttributeError:
        pass

def on_press(key):
    global f_pressed
    global cancel_reset
    global event_time
    try:
        if key.char == 'f':
            keyboard_controller.press(keyboard.Key.space)
            keyboard_controller.release(keyboard.Key.space)
            if (f_pressed == 0):
                f_pressed = 1
            else:
                cancel_reset == 1
            
            
            event_time = time.time()
    except AttributeError:
        pass

def reset_f_pressed():
    global f_pressed
    global cancel_reset
    global event_time
    while True:
        time.sleep(3)  # Wait for 5 seconds
        elapsed_time = time.time() - event_time
        #print(f"{elapsed_time:.2f} seconds elapsed")
        if (elapsed_time < 3 and elapsed_time != None):
            time.sleep(3 - elapsed_time)
        #print(f_pressed, cancel_reset)
        if (cancel_reset == 1):
            cancel_reset = 0
            continue
        else:
            f_pressed = 0

# Create and start a thread that runs the reset_variable function
reset_thread = threading.Thread(target=reset_f_pressed)
reset_thread.daemon = True  # Set the thread as a daemon so it will be killed when the main thread is killed
reset_thread.start()
1+1
1+1
1+1
1+1
1+1
1+3
1+65
# Create an instance of the mouse.Listener
mouse_listener = mouse.Listener(on_scroll=on_scroll)

# Start the mouse listener
mouse_listener.start()


# Create an instance of the keyboard.Listener
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start the keyboard listener
keyboard_listener.start()

# Keep the script running
print("Listening for keyboard")
keyboard_listener.join()
