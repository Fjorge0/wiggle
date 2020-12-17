#!/usr/bin/env python3
import argparse
import re
import time

#adding arguments
parser = argparse.ArgumentParser(description='Make a caterpillar.')
parser.add_argument('--delay', '-d', dest='delay', default=10, type=int, help='the delay between printing lines in millliseconds')
parser.add_argument('--wiggle', '-w', dest='waveheight', default=3, type=int, help='the amount of spaces to fluctuate')
parser.add_argument('--separator', '-s', dest='sep', default=' ', help='the character to use to push the string futhur')
parser.add_argument('--length', '-l', dest='wavelength', default=0, type=int, help='the amount of body segments to print out (set to 0 for infinate)')
parser.add_argument('--body', '-b', dest='body', help='the body segment of the centipede')
parser.add_argument('--autobody', '-a', dest='autogenbody', action='store_const', const=True, default=False, help='use regex to replace chars inbetween parenthesis to make a body segment out of the head')
parser.add_argument('head', metavar='H', help='the head segment of the centipede')

#parse args
args = parser.parse_args()

#setting variables
separator = [f'{args.sep}']
bodyfiller = ['█']
if args.autogenbody and not args.body:
    bodyregex = re.compile(r'\([^)]*\)')
    args.body = fr'{bodyregex.sub("".join(bodyfiller * len(bodyregex.search(args.head).group())), args.head)}'
elif not args.body:
    args.body = args.head
current_waveheight = 0
segments = 0

#print centipede head
print(args.head)
print(args.body)
#print centipede body
while segments < args.wavelength or args.wavelength <= 0:
    #ascending body
    while current_waveheight < args.waveheight:
        current_waveheight += 1
        print(str(''.join(separator * current_waveheight)) + args.body)
        if current_waveheight >= args.waveheight:
            print(str(''.join(separator * current_waveheight)) + args.body)
        time.sleep(args.delay/1000)
    while current_waveheight > 0:
        #descending body
        current_waveheight -= 1
        print(str(''.join(separator * current_waveheight)) + args.body)
        if current_waveheight <= 0:
            print(str(''.join(separator * current_waveheight)) + args.body)
        time.sleep(args.delay/1000)
    segments += 1

#made in neovim
