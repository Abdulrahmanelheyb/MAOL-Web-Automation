# Copyright(c) 2017 Arjun Singh Yadav

RESET = '\033[0m'

ATTR = { 'bold' : '\033[1m',
         'underline' : '\033[4m',
         'strike' : '\033[9m' 
         }

def color_front(text, red, green, blue):
    """
    wraps the text in appropriate ANSI escape code for foreground color
    param text: text to be colored
    param red: R of RGB value
    param green: G of RGB value
    param blue: B of RGB value

    return: text wrapped in ANSI escape code
    """
    foreground = '\033[38;2;{r};{g};{b}m'.format(r=red, g=green, b=blue)
    text = foreground + text + RESET
    return text

def color_back(text, red, green, blue):
    """
    param text: text for which background is to be set
    param red: R of RGB value
    param green: G of RGB value
    param blue: B of RGB value
    
    return: text wrapped in ANSI escape code for background
    """
    background = '\033[48;2;{r};{g};{b}m'.format(r=red, g=green, b=blue)
    text = background + text + RESET
    return text

def bold(msg):
    """
    param msg: text to be made bold

    return: text wrapped in ANSI escape code for bold
    """
    return ATTR['bold'] + msg + RESET

def under(msg):
    """
    param msg: text to be underlined

    return: text wrapped in ANSI escape code for underline
    """
    return ATTR['underline'] + msg + RESET

def strike(msg):
    """
    param msg: text to be strikethrough

    return: text wrapped in ANSI escape code for strikethrough
    """
    return ATTR['strike'] + msg + RESET
