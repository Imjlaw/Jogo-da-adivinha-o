from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print('Tecla pressionada: {0}'.format(key.char))
    except AttributeError:
        print('Tecla especial pressionada: {0}'.format(key))

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:

    listener.join()