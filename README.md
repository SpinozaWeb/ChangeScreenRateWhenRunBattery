Что делает этот скрипт?
- Переклбчает частоту монитора ноутбука на 60Гц если на ноутбук не подаётся питание.
Для чего это было сделано?
- Компания Microsoft в Windows 11 не захотела реализовать экономию батареи путём снижения частоты экрана. Хотя в настройках пишет об этом при изменении частоты.


Скрипт работает на Windows. Делал тест на Windows 11
Для его работы понадобится установить python 3.10.6.
Потом установить дополнительные модули:
pip install psutil
pip install pywin32
Запуск "py BreadcrumbsChangeScreenRateWhenRunBattery.pyw".
Скрипт запустится в фоне и будет работать до перезагрузки ПК.

Чтобы скрипт работал и после перезгрузки ПК его нужно добавить в автозагрузку.
