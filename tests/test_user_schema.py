from service.api.serializers.vk_user import VKUsersSchema

vk_user_data_standard = {
    'response': [
        {
            'id_': 1,
            'first_name': 'Name',
            'last_name': 'Lname',
            'is_closed': False,
            'can_access_closed': True
        }, {
            'id_': 2,
            'first_name': 'Name',
            'last_name': 'Lname',
            'is_closed': False,
            'can_access_closed': True
        },
    ]
}


def test_vk_user_schema_standard_data():
    data = VKUsersSchema().load(vk_user_data_standard)

    assert data['response'] == vk_user_data_standard['response']
