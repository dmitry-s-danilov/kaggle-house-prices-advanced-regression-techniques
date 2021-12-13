#!/bin/python

from subprocess import run

interpreter = 'python'
module = 'contest.data.load'

args = [interpreter, '-m', module]

if __name__ == '__main__':
    run(args)
