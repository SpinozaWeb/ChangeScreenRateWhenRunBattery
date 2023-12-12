import psutil
import win32api
import win32con
import time

def change_screen_refresh_rate():
    # Получаем текущую частоту обновления экрана
    current_refresh_rate = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS).DisplayFrequency

    if current_refresh_rate != 60:
        # Устанавливаем новую частоту обновления экрана (60 Гц)
        settings = win32api.EnumDisplaySettings(None, win32con.ENUM_REGISTRY_SETTINGS)
        settings.DisplayFrequency = 60
        win32api.ChangeDisplaySettings(settings, win32con.CDS_UPDATEREGISTRY)

def is_charging():
    battery = psutil.sensors_battery()
    # Проверяем состояние зарядки
    return battery is not None and battery.power_plugged

while True:
    # Если питание отключено, то снижаем частоту экрана
    if not is_charging():
        # Вызываем функцию для изменения частоты обновления экрана
        change_screen_refresh_rate()

    # Пауза на 10 секунд перед следующей проверкой
    time.sleep(10)
