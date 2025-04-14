# conf.py
import os
import sys
# Если _html_files лежит рядом с docs/, то путь будет '../_html_files'
# Если _html_files лежит в корне, а docs/ тоже в корне, путь будет '../_html_files'
html_extra_path = ['../_html_files'] # <-- Оставляем это, чтобы копировались CSS и другие ресурсы.

# Указываем Sphinx использовать наши HTML-файлы для конкретных страниц
# Ключ - имя страницы без .html (как оно будет в URL), значение - путь к исходному HTML-файлу относительно conf.py
html_additional_pages = {
    'index': '../_html_files/index.html',  # Говорим использовать наш index.html для корневой страницы
    # Добавьте сюда другие ваши HTML-страницы по аналогии:
    # 'имя_вашей_страницы': '../_html_files/имя_вашего_файла.html',
}

# Минимальные обязательные настройки Sphinx
project = 'ACI Troubleshooting Book' # Можно любое название
copyright = '2025,  Andres Vega'
author = ' Andres Vega'

# Необходимые заглушки
extensions = []
master_doc = 'index' # Должен указывать на файл index.rst
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Тема не важна, так как мы ее не используем для наших файлов, но Sphinx требует ее указать
html_theme = 'alabaster'