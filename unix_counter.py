import time
import argparse
import unix_period as up


#For the help file:
#go to the command-line,
#change directory (cd) to the folder where this file is located,
#type the letters
#'python' unix_counter.py -h
#or
#'python' unix_counter.py --help

parser=argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
    description='''

This Python script contains a function called unix_countup(), which counts up to a unix timestamp.
Unix time (also known as POSIX time or epoch time) is a system for describing instants in time, defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, minus the number of leap seconds that have taken place since then.


COMMAND-LINE EXAMPLE (1):
 F:
 cd F:\\Python\\Projects\\Epoch
 python unix_counter.py 1500000000


COMMAND-LINE EXAMPLE (2):
 F:
 cd F:\\Python\\Projects\\Epoch
 python unix_counter.py -p 1500000000


COMMAND-LINE EXAMPLE (3):
 F:
 cd F:\\Python\\Projects\\Epoch
 python unix_counter.py --party 1500000000
---------------------''',
    epilog="""
---------------------
DETAILS ABOUT AUTHOR:
https://www.JoshingAroundBlog.WordPress.com/
https://www.LinkedIn.com/in/Josh-Voss
https://www.Twitter.com/VossDataScience
""")
#NOTE (fix): dashes make the argument optional, not required


import sys

counter = up.unix_countup(float(sys.argv[1]))
counter

while True:
    try:
        counter = up.unix_countup(int(sys.argv[1]), sys.argv[2])
        counter
    except:
        parser.add_argument('-p', '--party', nargs='*', type=float, default=0.0, help='The unix time for the party!  Default:[party=0.0]')
        parser.add_argument('-m', '--message', nargs='*', type=str, help='The message displayed when the counter reaches given time.')
        #parser.add_argument('-o','--offset', nargs='*', type=float, default=0, help='The place out of line from the actual time.  Default:[offset=0]')
        args=parser.parse_args()
        
        if args.party:
		    #  !! ARGS.MESSAGE  NOT WORKING  !!
            counter = up.unix_countup(args.party)
            counter
        else:
            if __name__ == '__main__':
                up.unix_countup(1500000000)

        #If you want to exit the counter, then press ctrl c

