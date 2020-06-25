"""
    syntax

    !command[ op1 op2 ... opN]

"""
import typing as t

from service.app.bot_options.love_calculator import love_calculator_handler
from service.app.bot_options.random_numbers import random_number
from service.app.exceptions import NotACommandError, CommandNotFoundError


commands_description = {
    'lc': (
        'usage !lc first_name second_name '
        'shows % of names compatibility'
    )
}


def commands_list(*args, **kwargs):
    return '\n'.join([
        f'command {command}\n{desc}' for command, desc in commands_description.items()
    ])


commands_handlers = {
    'lc': love_calculator_handler,
    'rnd': random_number
    # 'commands': commands_list
}


def parse_command(message_text: str):
    if not message_text.startswith('!'):
        raise NotACommandError(context='Not valid command notation')

    message_text = message_text.replace('!', '')

    command, *params = message_text.split()

    return command, params


def execute_command(message_text: str):
    command: str
    params: list
    command, params = parse_command(message_text)

    handler = commands_handlers.get(command)

    if not handler:
        raise CommandNotFoundError(context=f'Command {command} not found')

    return handler(params)
