from utilities.commands import CommandUtils


class CommandNotFoundException(Exception):
    """Exception raised when the user command is invalid.
    """
    def __init__(self, command):
        self.command = command
        super().__init__()

    def __str__(self):
        return f'{self.command} not found in {CommandUtils.COMMAND_LIST}\n'
