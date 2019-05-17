import os
import sys
import argparse
# __version__ = 'x.x.x'
from YOUR_PROJECT_NAME.version import __version__


def get_version():
    return "Package: {} | Version: {}".format(__package__,
                                              __version__)


def arguments_parser(argv):
    parser = argparse.ArgumentParser(
        description="Process arguments for project: '{}'.".format(__package__))

    parser.add_argument('--version',
                        '-v',
                        action='version',
                        version=get_version())

    args = parser.parse_args(argv)
    return args


def main():
    args = arguments_parser(sys.argv[1:])

    # continue with your application logic here


if __name__ == '__main__':
    main()
