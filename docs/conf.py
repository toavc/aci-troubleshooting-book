# conf.py
import os
import sys
# Если _html_files лежит рядом с docs/, то путь будет '../_html_files'
# Если _html_files лежит в корне, а docs/ тоже в корне, путь будет '../_html_files'
# Возвращаем html_extra_path к копированию всей директории _html_files.
# Идея в том, что index.html из этой директории перезапишет тот, что сгенерирован из index.rst.
html_extra_path = ['../_html_files']

# Убираем html_additional_pages, чтобы избежать конфликтов.

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