from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

Config.set("graphics", "resizable", False)                    # Задаємо параметри вікна
Config.set("graphics", "height", "480")
Config.set("graphics", "width", "720")

class Caesar_App(App):
    def encrypt(self, args):                                    # Зашифровує повідомлення за допомогою індивідуального ключа
        if not self.text_field2.text:                           # і виводить результат в останнє поле
            self.text_field3.text = "Повідомлення не знайдено"
        else:
            if not self.text_field1.text:
                self.text_field3.text = "Ключ не вказаний"
            else:
                key = self.text_field1.text
                message = self.text_field2.text
                res1, res2 = 0, ""
                for i in key:
                    res1 += ord(i)
                    x = str(res1)[0:2]
                for i in message:
                    res2 += self.basement[self.basement.index(i)- int(x)]
                self.text_field3.text = res2

    def decrypt(self, args):                                    # Розшивровує повідомлення при наявному ключі і показує оригінал
        if not self.text_field2.text:                           # повідомлення в останньому полі
            self.text_field3.text = "Повідомлення не знайдено"
        else:
            if not self.text_field1.text:
                self.text_field3.text = "Ключ не вказаний"
            else:
                key = self.text_field1.text
                message = self.text_field2.text
                res1, res2 = 0, ""
                for i in key:
                    res1 += ord(i)
                    x = str(res1)[0:2]
                n = self.basement
                self.basement += self.basement
                for i in message:
                    res2 += self.basement[self.basement.index(i)+ int(x)]
                self.text_field3.text = res2
    def build(self):                                            # Задаємо структуру, параметри та змінні для програми
        self.title = "Caesar Cryptographer by W.R."
        self.basement = "1qazгоьблш3l./;p0-[\]=!Q#EDCVed)_{\"}йфячыcvfr45Y^&AZXS2UJM<KI*(OL>?:Pцувс макзхэъієїtgbnhxswтрнy67ujm,ki89епиW@щдюжoFR$%TGBNH"
        bl = BoxLayout(orientation="vertical",)
        gl = GridLayout(cols=2, padding=[3, 3, 3, 5])
        button_encrypt = Button(text="Зашифрувати", id="E", on_press=self.encrypt, background_color=[.100, .50, .700, 1])
        button_decrypt = Button(text="Розшифрувати", id="D", on_press=self.decrypt, background_color=[.100, .50, .700, 1])
        self.text_field1 = TextInput(hint_text="Ключ, напр. G$h83@D* ", size_hint_x=None, width=500, font_size=24)
        self.text_field2 = TextInput(hint_text="Повідомлення", font_size=24)
        self.text_field3 = TextInput(hint_text="Результат", font_size=24)

        gl.add_widget(Label(text="Дана програма допоможе зашифрувати повідомлення і відкри-\nти його вміст лише за допомогою ключа(набір символів \nі цифр). Робота програми базується на шифрі Цезаря.", size_hint_x=None, width=500, color=[.25, .25, .75, 1]))
        gl.add_widget(button_encrypt)
        gl.add_widget(self.text_field1)
        gl.add_widget(button_decrypt)
        bl.add_widget(gl)
        bl.add_widget(self.text_field2)
        bl.add_widget(self.text_field3)
        bl.add_widget(Label(text="Розроблено Владиславом Рудиком", size_hint=[1,.1]))
        return bl
if __name__ == "__main__":
    Caesar_App().run()
