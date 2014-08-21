Cкрипт для Conky замена http://freehabr.ru/blog/linux/1651.html, так как сервис rp5.ru перешел на платный вариант предоставления погоды в xml виде. Поэтому был написан новый парсер для погоды для gismeteo.ru с аналогичными ключами как в данной статье.

Для установки в системе должен быть установлен pip,если не установлен то для debian\ubuntu систем

# sudo apt-gt install pip

Далее нужно установить замечательную бибилиотеку https://github.com/PixxxeL/gismeteopy:

# sudo pip install gismeteopy

Далее надо поменять один параметр в библиотеке для этого найти ее путь

# pip show gismeteopy

Следует отредактировать файл parser.py (у меня путь /usr/local/lib/python2.7/dist-packages/gismeteo/parser.py) поменять параметр: TEMP_IS_AVERAGE = False на значение True

На этом все далее как в статье(использоваь надо только мой парсер погоды weather.py) прилагаю также мой конфиг conky.
