import argparse

from {{cookiecutter.package_name}}.version import __version__

def main():
    parser = argparse.ArgumentParser(
            description='{{cookiecutter.package_description}}')
    parser.add_argument('-v',
            '--version',
            action='version',
            version=__version__,
            help='Print the version')

    args = parser.parse_args()

    # TODO(lgulich): Do something with the args
