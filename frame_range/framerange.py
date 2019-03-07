import logging
import sys
import argparse
import os

from fileseq import filesequence
from fileseq.filesequence import FileSequence

logging.basicConfig(level=logging.INFO)


def print_sequences_frame_range(path):
    ''' Prints the frame ranges of animated sequences in given directory.

    @param path: path to the directory. Has been canonicalised and decoded (utf-8).
    '''

    # the canonical path is deprived of the last "/" compared to the path given by user
    # so need to add '/' to the pattern
    # *.@@@@.* will match the animated sequence format: name.####.ext
    pattern = path.encode('utf-8') + '/' + '*.@@@@.*'
    seq_list = FileSequence.findSequencesOnDisk(pattern)

    for seq in seq_list:

        # examples have shown that invalid sequences were considered:
        # - for sequence which name contains the character '.'
        # - for sequence for which the start frame is 0001
        if '.' not in seq.basename()[:-1] and seq.start() == 1001:
            logging.info("%s: %s"%(seq.basename()[:-1], seq.frameSet()))
        else:
            logging.debug("Invalid sequence name and/or frame range for found sequence %s"%str(seq).split('/')[-1])

    return


def main(args):
    ''' Parses arguments (path to the directory that should be considered) and verify they are valid. '''

    parser = argparse.ArgumentParser(description="Finds all animated sequences in a given directory \
        and prints their frame ranges.")
    parser.add_argument("path", help="path to directory")
    args = parser.parse_args()

    path = args.path
    # clean path and make sure it is valid
    path = path.decode('utf-8')
    path = os.path.realpath(path) # canonical path
    assert os.path.exists(path) == 1, "given path %s does not exist"%path

    print_sequences_frame_range(path)

    return


if __name__ == "__main__":
    main(sys.argv)
