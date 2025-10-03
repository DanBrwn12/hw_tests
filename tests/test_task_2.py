import unittest

import requests

from Task_2 import YandexDisk
from ydx_token import ydx_token

class TestTask2(unittest.TestCase):
    def setUp(self):
        self.folder_name = "test_folder"
        self.ydx = YandexDisk(self.folder_name, ydx_token)

    def test_initialization(self):
        """Тестирование, что класс инициализируется корректно"""
        self.assertEqual(self.ydx.folder_name, self.folder_name)
        self.assertEqual(self.ydx.ydx_token, ydx_token)
        self.assertEqual(self.ydx.params["path"], f"/{self.folder_name}")
        self.assertEqual(self.ydx.params["overwrite"], "true")
        self.assertEqual(self.ydx.headers["Authorization"], f"OAuth {ydx_token}")
        self.assertEqual(self.ydx.headers["Content-Type"], "application/json")

    def test_status_connect(self):
        params = {
            "path": "/"
        }
        response = requests.get(self.ydx.YDX_FOLDER_URL, headers=self.ydx.headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_status_create_folder(self):
        """Тест создания папки"""
        self.assertEqual(self.ydx.create_ydx_folder(), 201)

    def test_status_folder_exist(self):
        """Тест на то, что папка уже существует"""
        self.ydx.create_ydx_folder()
        exist = self.ydx.create_ydx_folder()
        self.assertEqual(exist, 409)

    def test_status_delete_folder(self):
        self.assertEqual(self.ydx.delete_ydx_folder(), 204)











