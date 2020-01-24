class Data:
    __followers = []
    __followings = []
    __floods_received = []

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
    def get_floods_received(cls):
        return cls.__floods_received

    @classmethod
    def add_floods_received(cls, flood_received_id):
        if flood_received_id not in cls.__floods_received:
            cls.__floods_received.append(flood_received_id)

    @classmethod
    def has_flood_received(cls, flood_received_id):
        return flood_received_id in cls.__floods_received
