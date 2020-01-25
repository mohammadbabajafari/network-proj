import settings
from common_utils import send_flood
from data import Data
from db_utils import search_text_db
from send_utils import send_accept, send_query_answer


def handle_accept(json: dict, address: tuple, *args, **kwargs):
    from UI import openDialog
    Data.add_following(address[0])
    alert_message = f"user {address[0]} followed successfuly"
    openDialog(alert_message)


def handle_error(json: dict, address: tuple, *args, **kwargs):
    from UI import openDialog
    content = json.get('content')
    alert_message = content.get('text')
    openDialog(alert_message)


def handle_broadcast(json: dict, address: tuple, *args, **kwargs):
    from UI import openDialog
    if not Data.has_flood_received(json.get('id')):
        Data.add_floods_received(json.get('id'))
        openDialog(json['content'].get('text'), title=f'Broadcast: {address[0]}')
        send_flood(json.get('content'), json.get('type'), json.get('status'), json.get('id'),
                   black_list=[address[0], json['content'].get('src')])
    else:
        print('hbroadcast else')


def handle_query(json: dict, address: tuple, *args, **kwargs):
    if not Data.is_greater_query_received(json.get('id'), json['content']['TTL']):
        Data.add_query_received(json.get('id'), json['content']['TTL'])
        if Data.is_waiting_answered(json['id']):
            print(f'{json["id"]} has been answered')
            return

        res = search_text_db(json['content'].get('text'))
        content = json['content']
        if res:
            res_content = dict(data=res)
            res_content['src'] = settings.MY_IP_ADDRESS
            res_content['uuid'] = json.get('id')
            rcv_from = address[0]  # Data.get_waiting(json['id'])['received_from']
            Data.add_waiting(json['id'], address[0], [])
            send_query_answer(res_content, rcv_from)
        # elif content['TTL'] == 0:
        #     is_successful = False
        #     res_content = dict()

        else:
            content['TTL'] -= 1
            sent_to = send_flood(content, json.get('type'), json.get('status'), json.get('id'),
                                 black_list=[address[0], json['content'].get('src')])
            Data.add_waiting(json['id'], address[0], sent_to)
            return

    else:
        print('hquery else')


def handle_query_answer(json: dict, address: tuple, *args, **kwargs):
    from UI import openDialog
    content = json['content']
    waiting = Data.get_waiting(content['uuid'])
    if waiting is True:
        print(f'{content["content"]} has been answered before.')
    elif isinstance(waiting, dict):

        rcv_from = waiting['received_from']
        if rcv_from:
            send_query_answer(content, rcv_from)
        else:
            openDialog(str(content['data']), title=f'Query Answer: {content["src"]}')
    else:
        print('Query has been removed.')


def handle_follow(json: dict, address: tuple, *args, **kwargs):
    from UI import openDialog
    Data.add_follower(address[0])
    openDialog(f'{address[0]} followed you!')
    send_accept(address)


def handle_message(json: dict, address: tuple, *args, **kwargs):
    send_accept(address)


def handle_leave(json: dict, address: tuple, *args, **kwargs):
    from UI import openDialog
    Data.leave(address[0])
    openDialog(f'{address[0]} left the network!')

