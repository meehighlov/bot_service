from service.api.serializers.vk_user import VKUsersSchema

vk_user_data_standard = {
    'response': [
        {
            'id': 1,
            'first_name': 'Name',
            'last_name': 'Lname',
            'is_closed': False,
            'can_access_closed': True
        }
    ]
}


def test_vk_user_schema_standard_data():
    data = VKUsersSchema().load(vk_user_data_standard).data

    assert set(data) - set(vk_user_data_standard) == set()
