import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def get_response():
    """Создание вызова API и сохранение ответа"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    print("Status code: ", r.status_code)
    return r

#
def get_repo_dicts(response):
    """Сохранение ответа API в переменной и Анализ информации о репозиториях"""
    response_dict = response.json()
    print("Total repositories: ", response_dict['total_count'])
    repo_dicts = response_dict['items']
    print("Number of items: ", len(repo_dicts))
    return repo_dicts

def get_names_plot_dicts(repo_dicts):
    """Сбор данных о репозиториях в отдельный словарь"""
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        # Извлечение описания проекта, если таковое имеется в полученных данных
        description = repo_dict['description']
        if not description:
            description = 'No description provided'
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)
    return names, plot_dicts


def make_visualization(names, plot_dicts):
    # Построение визуализации
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')


r = get_response()
repo_dicts = get_repo_dicts(r)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)
