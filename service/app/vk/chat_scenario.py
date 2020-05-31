from service.app.config import config


class BaseChatScenario:

    def answer(self, message_from_user: str) -> str:
        return 'Обратитесь к администратору сообщества'

    def keyboard(self):
        pass


class MeScenario(BaseChatScenario):

    def answer(self, message_from_user: str) -> str:
        pass


def get_scenario_by_user_id(user_id: str):
    return {
        config.MY_VK_ID: MeScenario
    }.get(user_id)
