#!/bin/python

from subprocess import run

interpreter = 'python'
# module = 'contest.data.load'
module = 'contest.data'

args = [interpreter, '-m', module]

if __name__ == '__main__':
    run(args)
