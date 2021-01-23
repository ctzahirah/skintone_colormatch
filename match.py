from pandas import read_csv
from colormap import hex2rgb
from math import sqrt

def tone_match(color, color_ref='tones.csv', index_name='color_name', color_col='rgb_hex'):
    color_ref = read_csv(color_ref, index_col=index_name)
    
    try:
        rgb_hex = hex2rgb('#'+color if not '#' in color else color) #change hex to decimal for input from user
    except ValueError:
        raise ValueError(f"{color} is not valid hexadecimal color.")

    color_ref[color_col] = color_ref[color_col].apply(hex2rgb) #change hex to decimal in dataframe
    for color_name, color_diff in color_ref[color_col].apply(compare_color, color = rgb_hex).argsort().items():
        if color_diff == 0:
            return color_name

def compare_color(color_ref, color):
    return sqrt((color[0]-color_ref[0])**2 + (color[1]-color_ref[1])**2 + (color[2]-color_ref[2])**2)