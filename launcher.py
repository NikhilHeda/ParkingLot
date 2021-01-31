import argparse

from exceptions.command_not_found_exception import CommandNotFoundException
from exceptions.invalid_input_exception import InvalidInputException
from services.parser import RequestParser


class Launcher:
    """Launcher class to read from file for user commands

    Attributes:
        filename (str): Contains the file path for user commands
        parser (RequestParser): RequestParser instance for parsing and executing user commands
    """

    def __init__(self, filename=''):
        self.filename = filename
        self.parser = RequestParser()

    def process(self):
        """Function to read user commands from file
        """
        with open(self.filename, 'r') as fp:
            for line in fp:
                input_command = line.strip().split()
                if input_command:
                    try:
                        self.parser.parse(input_command)
                    except CommandNotFoundException as e:
                        print(f'Command is Invalid! : {e}')
                    except InvalidInputException as e:
                        print(f'Input arguments are wrong! : {e}')


def main():
    """Main driver function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input_file', help='Input command file for processing')
    args = parser.parse_args()

    launcher = Launcher(filename=args.input_file)
    launcher.process()


if __name__ == '__main__':
    main()
