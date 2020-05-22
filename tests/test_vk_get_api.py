from unittest import mock

from vk_api import VkApi

from service.app.vk.auth import get_api


@mock.patch.object(VkApi, 'auth')
@mock.patch.object(VkApi, 'get_api', return_value='vk_api_object')
def test_auth_vk(
        api_mock,
        auth_mock
):

    vk_api = get_api()

    assert auth_mock.call_count == 1
    assert api_mock.call_count == 1
    assert vk_api == 'vk_api_object'
