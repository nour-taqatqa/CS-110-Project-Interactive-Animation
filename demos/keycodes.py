# Mac Key Codes
key_codes = {
    'mac': {
        'up': 8320768,
        'down': 8255233,
        'left': 8124162,
        'right': 8189699
    },
    'windows': {
        'up': 38,
        'down': 40,
        'left': 37,
        'right': 39
    }
}

def get_os(): 
    import platform
    if platform.system() == 'Darwin':
        return 'mac'
    else:
        return 'windows'

def get_up_keycode():
    return key_codes[get_os()]['up']

def get_down_keycode():
    return key_codes[get_os()]['down']

def get_left_keycode():
    return key_codes[get_os()]['left']

def get_right_keycode():
    return key_codes[get_os()]['right']