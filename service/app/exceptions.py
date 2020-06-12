class BaseError(Exception):
    message = 'Unknown error'
    code = 1

    def __str__(self):
        return f'message --{self.message}-- code {self.code}'


class WrongParametersFormatError(BaseError):
    message = 'Wrong parameters'
    code = 2


class ContextError(BaseError):
    message = 'Context error'
    code = 3
