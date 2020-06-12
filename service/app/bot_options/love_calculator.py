import requests

from service.app.config import config
from service.app.exceptions import ParseCommandParamsError, ExternalServiceCallError


def love_calculator(fname, sname):

    params = {
        'fname': fname,
        'sname': sname
    }

    headers = {
        'x-rapidapi-host': config.X_RAPIDAPI_HOST,
        'x-rapidapi-key': config.X_RAPIDAPI_KEY
    }

    try:
        r = requests.get(
            'https://love-calculator.p.rapidapi.com/getPercentage',
            params=params,
            headers=headers
        )
    except Exception as e:
        print(e)
        raise ExternalServiceCallError(context=e)

    data = r.json()

    message = (
        f'% for {data["fname"]} and {data["sname"]} is {data["percentage"]}, {data["result"]}'
    )

    return message


def love_calculator_handler(params: list) -> str:
    """
    :param params: list of params, expect: ['fname', 'sname']
    :return: response message
    """

    try:
        fname, sname = params
    except ValueError:
        raise ParseCommandParamsError(context='Love calculator')

    return love_calculator(fname, sname)
