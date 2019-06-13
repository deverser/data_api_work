import unittest
from python_repos import r, repo_dicts, response_dict

class PythonReposTestCase(unittest.TestCase):
    """
    Тест для проверки статус кода и количества возвращаемых
    элементов при выполнении запроса API
    """
    def test_status_code(self):
        # Статус код
        test_code = r.status_code
        self.assertEqual(test_code, 200)

    def test_repodicts(self):
        # Возвращаемые элементы
        test_repos = len(repo_dicts)
        self.assertEqual(test_repos, 30)

    def test_total_count(self):
        test_count = response_dict['total_count']
        self.assertGreater(test_count, 3000000)

if __name__ == '__main__':
    unittest.main()