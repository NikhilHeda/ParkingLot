from utilities.commands import CommandUtils


class InvalidInputException(Exception):
    """Exception raised when the command is valid, but the number of arguments don't match the required number
    """
    def __init__(self, command, params, message='Input is invalid'):
        self.command = command
        self.params = params
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        _expected = CommandUtils.VALIDATION_MAP[self.command] - 1
        _got = len(self.params) - 1
        return f'{self.message} for command "{self.command}", expected {_expected} arguments, got {_got}\n\t{self.params}'
