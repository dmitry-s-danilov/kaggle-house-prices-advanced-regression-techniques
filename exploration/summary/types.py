#!/bin/python

from subprocess import run

interpreter = 'python'
# module = 'contest.exploration.summary.types.describe'
module = 'contest.exploration.summary.types'

args = [interpreter, '-m', module]

if __name__ == '__main__':
    run(args)
