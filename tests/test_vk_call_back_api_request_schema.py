from service.api.serializers.vk_call_back_event import VKCallBackAPIEvent


call_back_api_event_data = {
    'type': 'message_new',
    'object': {
        'message': {
            'date': 1,
            'from_id': 1,
            'id': 10,
            'out': 0,
            'peer_id': 1,
            'text': 'hey',
            'conversation_message_id': 9,
            'fwd_messages': [],
            'important': False,
            'random_id': 0,
            'attachments': [],
            'is_hidden': False
        },
        'client_info': {
            'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
            'keyboard': True,
            'inline_keyboard': True, 'lang_id': 0
        }
    },
    'group_id': 1,
    'event_id': 'ei',
    'secret': 'secret'
}


def test_vk_api_call_back_request():
    data = VKCallBackAPIEvent().load(call_back_api_event_data)

    assert data == call_back_api_event_data
