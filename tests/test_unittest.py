import unittest
from parameterized import parameterized
from main import YaDiskManager


TOKEN = ''

FIXTURE_POS = [
    'test_folder',
    'test_folder/new_folder',
    'test_folder/new_folder/inner_folder'
]

FIXTURE_NEG = [
    'notexist/new_folder',
]


class TestYandexApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.yandex_disc = YaDiskManager(TOKEN)
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.yandex_disc.delete_folder(FIXTURE_POS[0])
    
    @parameterized.expand(FIXTURE_POS)
    def test_create_folder(self, path):
        result = self.yandex_disc.create_folder(path)
        self.assertEqual(result, 201)
        above_path = 'disk:/'
        parts = path.split('/')[:-1]
        for part in parts:
            above_path += (part + '/')
        resource_list = self.yandex_disc.resource_list(above_path)
        added_folder_name = path.split('/')[-1]
        check_resource_dict = {'type': 'dir', 'name': added_folder_name}
        self.assertIn(check_resource_dict, resource_list)

    @parameterized.expand(FIXTURE_NEG)
    def test_create_folder_fail(self, path):
        result = self.yandex_disc.create_folder(path)
        self.assertNotEqual(result, 201)
