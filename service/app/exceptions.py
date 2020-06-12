class BaseError(Exception):
    message = 'Unknown error'
    context = 'main'
    code = 1

    def __init__(self, **kwargs):
        self.message = kwargs.get('message') or self.message
        self.code = kwargs.get('code') or self.code
        self.context = kwargs.get('context') or self.context

    def __str__(self):
        return f'message --{self.message}-- context --{self.context}-- code --{self.code}--'


class ContextError(BaseError):
    message = 'Context error'
    code = 3


class CommandError(BaseError):
    message = 'Command error'
    code = 4


class ParseCommandParamsError(CommandError):
    pass


class CommandNotFoundError(CommandError):
    pass


class ParseCommandError(CommandError):
    pass


class NotACommandError(CommandError):
    pass


class ExternalServiceCallError(BaseError):
    message = 'External service call error'
    code = 6
