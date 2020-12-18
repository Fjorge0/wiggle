#!/usr/bin/env python3
import argparse
import re
import time

### adding arguments
## set parser
parser = argparse.ArgumentParser(description='Make a caterpillar.')
## arguments
# switches
parser.add_argument('--autobody', '-a', dest='autogenbody', action='store_const', const=True, default=False, help='automatically make a body segment by replacing characters inside parenthesis with squares')
parser.add_argument('--body', '-b', dest='body', help='the body segment of the centipede')
parser.add_argument('--delay', '-d', dest='delay', default=10, type=int, help='the delay between printing lines in millliseconds')
parser.add_argument('--length', '-l', dest='wavelength', default=0, type=int, help='the amount of body segments to print out (set to 0 for infinate)')
parser.add_argument('--max-width', '-m', dest='waveheight', default=3, type=int, help='the amount of spaces to fluctuate')
parser.add_argument('--waggle', '-w', dest='waggle', action='store_const', const=True, default=False, help='reverse the wiggle direction')
parser.add_argument('--separator', '-s', dest='sep', default=' ', help='the character to use to push the string futhur')
# input
parser.add_argument('head', metavar='H', help='the head segment of the centipede')

### parse args
args = parser.parse_args()

### declaring variables
## variables
separator = [f'{args.sep}']
bodyfiller = ['█']
segments = 0
## dependant variables
# generate body based on autobody flag
if args.autogenbody and not args.body:
    bodyregex = re.compile(r'\([^)]*\)')
    args.body = fr'{bodyregex.sub("".join(bodyfiller * len(bodyregex.search(args.head).group())), args.head)}'
elif not args.body:
    args.body = args.head
# determine the starting waveheight based on waggle flag
if args.waggle:
    current_waveheight = args.waveheight
else:
    current_waveheight = 0
## functions
def wiggle_right(body, delay, currentwiggle, maxwiggle):
    while currentwiggle < maxwiggle:
        currentwiggle += 1
        print(str(''.join(separator * currentwiggle)) + body)
        if currentwiggle >= maxwiggle:
            print(str(''.join(separator * currentwiggle)) + body)
        time.sleep(delay/1000)
    return currentwiggle
def wiggle_left(body, delay, currentwiggle, maxwiggle):
    while currentwiggle > 0:
        currentwiggle -= 1
        print(str(''.join(separator * currentwiggle)) + body)
        if currentwiggle <= 0:
            print(str(''.join(separator * currentwiggle)) + body)
        time.sleep(delay/1000)
    return currentwiggle

### centipede maker
## print centipede starting segment
print(str(''.join(separator * current_waveheight)) + args.head)
print(str(''.join(separator * current_waveheight)) + args.body)
## print centipede body
while segments < args.wavelength or args.wavelength <= 0:
    if args.waggle:
        current_waveheight = wiggle_left(args.body, args.delay, current_waveheight, args.waveheight)
        current_waveheight = wiggle_right(args.body, args.delay, current_waveheight, args.waveheight)
    else:
        current_waveheight = wiggle_right(args.body, args.delay, current_waveheight, args.waveheight)
        current_waveheight = wiggle_left(args.body, args.delay, current_waveheight, args.waveheight)
    segments += 1

### made in neovim
