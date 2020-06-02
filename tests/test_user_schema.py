from service.api.serializers.vk_user import VKUserSchema


vk_user_data_standard = {
    'id': 1,
    'first_name': 'Ivan',
    'last_name': 'Mikhailov',
    'is_closed': False,
    'can_access_closed': True
}

vk_user_data_uncaught = {
    'id': 1,
    'first_name': 'Ivan',
    'last_name': 'Mikhailov',
    'is_closed': False,
    'can_access_closed': True
}


def test_vk_user_schema_standard_data():
    data = VKUserSchema().load(vk_user_data_standard).data

    assert set(data) - set(vk_user_data_standard) == set()


def test_vk_user_schema_uncaught_fields():
    data = VKUserSchema().load(vk_user_data_standard).data


