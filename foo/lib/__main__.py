# coding: utf-8

import argparse
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_parser():
	
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--foo', help="this is something!"
    )
    return parser


def main():
    parser = init_parser()
    args = parser.parse_args()
    print("printer")
    logger.info("logger")
    print(args.foo)
    logger.info("Arguments: {}".format(args))
    print(args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
