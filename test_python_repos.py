import unittest
import python_repos as pr

class PythonReposTestCase(unittest.TestCase):
    """
    Тест для проверки статус кода и количества возвращаемых
    элементов при выполнении запроса API
    """
    def setUp(self):
        self.r = pr.get_response()
        self.response_dict = self.r.json()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)


    def test_get_response(self):
        # Статус код
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        # Возвращаемые элементы
        self.assertEqual(len(self.repo_dicts), 30)
        # Словарь репозитория должен содержать следующие ключи
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

    def test_total_count(self):
        # Общее количество репозиториев должно быть больше определенного числа
        self.assertGreater(self.response_dict['total_count'], 3000000)

if __name__ == '__main__':
    unittest.main()