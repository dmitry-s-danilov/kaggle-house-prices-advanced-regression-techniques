#!/bin/python

from subprocess import run

interpreter = 'python'
# module = 'contest.exploration.summary.nulls.describe'
module = 'contest.exploration.summary.nulls'

args = [interpreter, '-m', module]

if __name__ == '__main__':
    run(args)
