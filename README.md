# Інформація про наявні проекти і способи їх запуску.

Перші три програми створені за допомогою Python 3.6, а також GUI фреймворку kivy, тому використовують графічний інтерфейс.
- Clicker (Невелика міні гра, основана на необхідності кліків для збsльшення кількості очок і розвитку способів їх збільшення)
- Caesar Shiffer (Шифрувальник повідомлень, оснований на шифрі Цезаря, але модифікований)
- Cross_Nulls (Хрестики-Нулики у приємноиу графічному інтерфейсі.)                                                               

Останні дві програми написані чисто для роботи в cmd.
- Хрестики-нулики для командної строки(дешевий і сердитий аналог)
- Программа, яка робить лінію з квадрата введеного числа і закручує її всередину.
Для запуску і тестування програм на комп'ютері повинні бути встановлені Python i kivy.

Для швидкої перевірки на наявність чи встановлення kivy запустіть cmd.exe(Windows) i введіть наступні команди.

pip install --upgrade kivy        # При наявному Python встановить, або оновить бібліотеку kivy

Якщо программи не запускаються (трохи довший варіант):
    
pip uninstall kivy                                                                                 
python -m pip install --upgrade pip wheel setuptools                                                            
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew                                  
python -m pip install kivy.deps.gstreamer                                                                   
python -m pip install kivy.deps.angle                                                               
python -m pip install kivy                                                                                      

більш детальна інструкція для Linux: https://kivy.org/doc/stable/installation/installation.html#installation-devel
