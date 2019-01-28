# Інформація про наявні проекти і способи їх запуску.

Перші три програми створені за допомогою Python 3.6, а також GUI фреймворку kivy, тому використовують графічний інтерфейс.
Останні дві програми написані чисто для роботи в cmd.
Для запуску і тестування програм на комп'ютері повинні бути перечислені вище компоненти.

Для швидкої перевірки на наявність чи встановлення kivy запустіть cmd.exe(Windows) i введіть наступні команди.

pip install --upgrade kivy        # При наявному Python встановить, або оновить бібліотеку kivy

Якщо программи не запускаються (трохи довший варіант):
    
pip uninstall kivy

python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy.deps.angle
python -m pip install kivy

