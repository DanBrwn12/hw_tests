import requests

from ydx_token import ydx_token as token


class YandexDisk:
    YDX_FOLDER_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self, folder_name, ydx_token):
        self.folder_name = folder_name
        self.ydx_token = ydx_token
        self.params = {
            "path": f"/{self.folder_name}",
            "overwrite": "true"
        }
        self.headers = {
            "Authorization": f"OAuth {self.ydx_token}",
            "Content-Type": "application/json"
        }

    def create_ydx_folder(self):
        """Создание папки в Я.диске"""
        response = requests.put(self.YDX_FOLDER_URL, headers=self.headers, params=self.params)
        return response.status_code

    def delete_ydx_folder(self):
        """Удаление папки с Я.диска"""
        response = requests.delete(self.YDX_FOLDER_URL, headers=self.headers, params=self.params)
        return response.status_code



if __name__ == '__main__':
    yd = YandexDisk(folder_name='Тест', ydx_token=token)
    yd.create_ydx_folder()
    yd.delete_ydx_folder()
