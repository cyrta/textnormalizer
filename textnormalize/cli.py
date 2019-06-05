

#!/usr/bin/python
# coding=utf-8

__author__ = 'Pawel Cyrta'

import os
import sys
import codecs
import gzip
import re
import time

import logging
import argparse


def _init_args():
    parser = argparse.ArgumentParser(prog="textnormalizer",
               description="Change the raw text into normalized canonical form")
    parser.add_argument('infile', metavar='input', nargs='?',
               type=argparse.FileType('r'), default=sys.stdin,
               help='input text file')
    parser.add_argument('outfile', metavar='output', nargs='?',
               type=argparse.FileType('w'), default=sys.stdout,
               help='output text file')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
               dest='verbose', action='count', default=0)

    args = parser.parse_args()
    return args


def main():
    ARGS = _init_args()

    loglevel = logging.INFO
    if ARGS.verbose:
         loglevel = logging.DEBUG
         logging.basicConfig(level=loglevel, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    else:
        loglevel = logging.INFO
        logging.basicConfig(level=loglevel, format="%(asctime)s - %(levelname)s - %(message)s" )

    logging.debug("TextNormalizer - tool to change raw text into canonical form")
    logging.debug("  input file: {0}".format(ARGS.infile.name))
    logging.debug("  output file: {0}".format(ARGS.outfile.name))


