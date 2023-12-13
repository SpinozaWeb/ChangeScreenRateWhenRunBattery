Что делает этот скрипт?
- Переключает частоту монитора ноутбука на 60Гц если на ноутбук не подаётся питание.
  
Для чего это было сделано?
- Компания Microsoft в Windows 11 не захотела реализовать экономию батареи путём снижения частоты экрана. Хотя в настройках пишет об этом при изменении частоты.


Скрипт работает на Windows. Делал тест на Windows 11

Для его работы понадобится установить python 3.10.6.

Потом установить дополнительные модули:
pip install psutil
pip install pywin32

Запуск "py BreadcrumbsChangeScreenRateWhenRunBattery.pyw".

Скрипт запустится в фоне и будет работать до перезагрузки ПК.

Чтобы скрипт работал и после перезагрузки ПК его нужно добавить в автозагрузку.

Для этого нужно сделать ярлык скрипта. А затем перенести ярлык в папку автозагрузки.

Чтобы найти папку автозагрузки нужно нажать WIN+R и ввести shell:startup

Также я добавил exe файл если кто-то не хочет устанавливать себе python.

Для exe файла добавление в автозагрузку аналогично скрипту.
