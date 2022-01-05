import requests
from decouple import config


class Dao:
    def __init__(self):
        self.default_url = config("URL_FIREBASE")
    def get(self):
        re_get = requests.get(self.default_url.format("products/"))
        return re_get.json()
    def post(self, data):
        re_post = requests.post(self.default_url.format("products/"), data = data)
        return re_post.json()
    def put(self, data):
        re_put = requests.put(self.default_url.format("products/-Msg8Rk7u9LALyRWGPm-"), data = data)
    def delete(self, data):
        re_delete = requests.delete(self.default_url.format("products/" + data))