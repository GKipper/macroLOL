from pynput.keyboard import Listener, Key, Controller
from pynput import keyboard as kbd
import keyboard as kbd2

keyb = Controller()
K = Key

#keyb.type("It's impossible to think of flamingos without picturing a bright splash of pink. But where do they get their signature color? The answer lies in their diet. The flamingo feeds mainly on shrimps and insects, scraping them from the mud with its hook-shaped beak. These can contain a pigment that gives its feathers that particular shade of pink. Their shade changes depending on what they feed on, with the American flamingo being one of brightest and flashiest.")

def press(Key):
    print(Key)
    #with keyb.pressed(K.shift):
    #    keyb.press('a')
    #    keyb.release('a')
    
    try:
        key = Key.char
        if key == 'r':
            #keyb.press(K.ctrl_l)
            keyb.press('t')
            #keyb.release(K.ctrl_l)
            keyb.release('t')
    except:
        pass

def release(Key):
    pass

with Listener(on_press=press, on_realease=release) as listener:
    listener.join()
