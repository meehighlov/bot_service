from random import randint


def random_number(a: int, b: int) -> int:
    return randint(a, b)


def all_commands_descriptions():
    return {
        ':commands': 'list of commands',
        ':random': '1 5 - random integer between 1 and 5'
    }


def exec_command(message_text: str):
    if not message_text.startswith(':'):
        return 'not_a_command'

    """
        WORKS ONLY FOR RANDOM COMMAND!
    """
    # TODO make it more abstract!

    command = message_text[1:]
    command = command.strip().split()
    handler = commands_handlers(command[0])
    result = 'no results'
    if handler is not None:
        a, b = int(command[1]), int(command[2])
        result = handler(a, b)
    return f'{result}'


def commands_handlers(command):
    return {
        'commands': all_commands_descriptions,
        'random': random_number
    }.get(command)
