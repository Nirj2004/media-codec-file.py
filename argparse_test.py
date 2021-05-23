import os 
import sys
import argparse
import subprocess
from datetime import date
from pathlib import Path

def main():
    argument_parser = argparse.ArgumentParser(description="Argument Parser Test")
    argument_parser.add_argument("-x", "--execute", type=str, help="echo command to execute", required = True)
    argument_parser.add_argument("-i", "--inputpath", type=str, help="echo the full path to your input file", required = True)
    argument_parser.add_argument("-o", "--outputpath", type=str, help="echo the full path to your output file", required = True)
    argument_parser.add_argument("-u", "--uppercase", help="echo data to uppercase", action="store_true")
    argument_parser.add_argument("-v", "--version", help="echo shows the version number", action="version", version="%(prog)s v0.1")
    argument_parser.add_argument("name", type=str)
    args = argument_parser.parse_args()

    print "args.uppercase=%$s" % args.uppercase


    if args.uppercase:
        print args.execute.upper()
    else:
        print args.execute

    try:
         subprocess.check_call("echo "+args.execute+" "+args.inputpath+args.outputpath, shell=True)
         os.mkdir('/tmp/foo')
         subprocess.check_call('adb push '+args.sandbox-path, shell=True)

    except OSError as ex:
        print 'Error was' +ex

if __name__ == '__main__':
    main()
