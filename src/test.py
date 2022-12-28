from colorama import Fore, Back
import random


def random_foreground( ) :
    return random.choice( [
        Fore.MAGENTA,
        Fore.RED,
        Fore.BLACK
    ] )


def random_background( ) :
    return random.choice( [
        Back.WHITE,
    ] )


colors = dict( Fore.__dict__.items( ) )
colored_text = 'Jason, We have Successfully docked with one another!'
for character in colored_text :
    print( random_foreground( ) + random_background( ) + character, end = '' )
    # print(colors[random.choice(list(colors.keys()))] + character, end='')
