import random


from service.app.exceptions import ParseCommandParamsError


def random_number(params):
    try:
        a, b = params
    except ValueError:
        raise ParseCommandParamsError(context='Random number: pars params error')

    try:
        a, b = float(a), float(b)
    except ValueError:
        raise ParseCommandParamsError(context=f'Random number: only numbers allowed')

    return random.uniform(a, b)
