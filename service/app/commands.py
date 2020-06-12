"""
    syntax

    :comand [op1 op2 ... opN]

"""
from service.app.bot_options import commands_handlers
from service.app.exceptions import NotACommandError, CommandNotFoundError


def parse_command(message_text: str):
    if not message_text.startswith(':'):
        raise NotACommandError(context='Not valid command notation')

    message_text = message_text.replace(':', '')

    command, *params = message_text.split()

    return command, params


def execute_command(message_text):
    command, params = parse_command(message_text)

    handler = commands_handlers.get(command)

    if not handler:
        raise CommandNotFoundError(context=f'Command {command} not found')

    return handler(params)
