from models.user_info import UserInfo

class UserTable:
    def __init__(self):
        self.data = {}

    def put_info(self, user_info: UserInfo):
        self.data[user_info.id] = user_info

    def get_all_info(self):
        return list(self.data.values())

    def get_info_by_id(self, user_id):
        return self.data.get(user_id)

    def remove_info_by_id(self, user_id):
        return self.data.pop(user_id, None)
