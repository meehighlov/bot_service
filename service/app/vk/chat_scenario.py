from service.app.config import config
from service.app.vk.commands import exec_command
from service.app.vk.users import get_user_by_id


class BaseChatScenario:

    name = 'юзер'

    def answer(self, data: dict) -> str:
        pass

    def keyboard(self):
        pass


class MeScenario(BaseChatScenario):

    name = 'Ваня'

    def answer(self, data: dict) -> str:
        text = data['object']['message']['text']
        return exec_command(text)


def get_scenario_by_user_id(user_id: str):
    return {
        config.MY_VK_ID: MeScenario
    }.get(user_id)


def get_answer(request_data: dict):
    user_sender_id = request_data['object']['message']['from_id']
    scenario = get_scenario_by_user_id(f'{user_sender_id}')

    answer = scenario().answer(request_data)

    # user_sender_data = get_user_by_id(user_sender_id)

    return answer
