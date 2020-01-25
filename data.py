from datetime import datetime
from uuid import uuid4

import settings


class Data:
    __followers = []
    __followings = []
    __broadcast_received = []
    __query_received = {}
    __waiting_for_answer = {}

    @classmethod
    def get_followers(cls):
        return cls.__followers

    @classmethod
    def add_follower(cls, follower):
        if follower not in cls.__followers:
            cls.__followers.append(follower)

    @classmethod
    def block(cls, follower):
        if follower in cls.__followers:
            cls.__followers.remove(follower)

    @classmethod
    def get_followings(cls):
        return cls.__followings

    @classmethod
    def add_following(cls, following):
        if following not in cls.__followings:
            cls.__followings.append(following)

    @classmethod
    def unfollow(cls, following):
        if following in cls.__followings:
            cls.__followings.remove(following)

    @classmethod
    def leave(cls, address: str):
        if address in cls.__followings:
            cls.__followings.remove(address)
        if address in cls.__followers:
            cls.__followers.remove(address)

    @classmethod
    def get_broadcast_received(cls):
        return cls.__broadcast_received

    @classmethod
    def add_broadcast_received(cls, broadcast_received_id):
        if broadcast_received_id not in cls.__broadcast_received:
            cls.__broadcast_received.append(broadcast_received_id)

    @classmethod
    def has_broadcast_received(cls, broadcast_received_id):
        return broadcast_received_id in cls.__broadcast_received

    @classmethod
    def get_query_received(cls):
        return cls.__query_received

    @classmethod
    def add_query_received(cls, query_received_id, ttl):
        k = query_received_id
        v = ttl
        if k not in cls.__query_received.keys():
            cls.__query_received[k] = v
        elif cls.__query_received[k] < v:
            cls.__query_received[k] = v

    @classmethod
    def is_greater_query_received(cls, query_received_id, ttl):
        k = query_received_id
        v = ttl
        return k in cls.__query_received.keys() and cls.__query_received[k] > v

    @classmethod
    def get_waiting(cls, uuid):
        try:
            return cls.__waiting_for_answer[uuid]
        except KeyError:
            return None

    @classmethod
    def add_waiting(cls, uuid, received_from, sent_to):
        if uuid not in cls.__waiting_for_answer.keys():
            value = dict(received_from=received_from, sent_to=sent_to, time=datetime.now())
            cls.__waiting_for_answer[uuid] = value
        elif cls.__waiting_for_answer[uuid] is True:
            pass
        else:
            cls.__waiting_for_answer[uuid]['received_from'] = received_from
            cls.__waiting_for_answer[uuid]['sent_to'].append(sent_to)
            cls.__waiting_for_answer[uuid]['time'] = datetime.now()

    @classmethod
    def set_waiting_as_answered(cls, uuid):
        cls.__waiting_for_answer[uuid] = True

    @classmethod
    def clean_waiting(cls):
        for k, v in cls.__waiting_for_answer.items():
            if v is not True:
                if datetime.now() - v.get('time') > settings.TTW:
                    cls.__waiting_for_answer.pop(k)

    @classmethod
    def is_waiting_answered(cls, uuid):
        return cls.__waiting_for_answer.get(uuid) is True


if __name__ == '__main__':
    print(Data.is_waiting_answered(str(uuid4())))
