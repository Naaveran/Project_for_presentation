from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from random import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.clock import Clock
from kivy.uix.label import Label

Config.set("graphics", "resizable", False)      # Задаємо параметри для вікна програми
Config.set("graphics", "height", "480")
Config.set("graphics", "width", "480")

class The_Clicker_Program_App(App):
    def do_the_update(self, args):             # Активує виконання функції self.to_add_every_second раз в одну секундку
        Clock.schedule_interval(self.to_add_every_second, 1)

    def to_add_every_second(self, args):       # Активує додавання очок кожної секунди
        self.button1.text = str("%.2f" % (float(self.button1.text) + float(self.every_second_income)))

    def to_click(self, args):           # Добавляє очки до головного показника при кліку на першу кнопку
        self.x = str(float(self.button1.text) + self.adder)
        self.button1.text = str("%.2f" % float(self.x))
        self.button1.background_color = [
            random(),
            random(),
            random(),
            1
        ]

    def upgrade_second(self, args):     # Збільшує прирість очок на 0.05 за кожну секунду.
        if float(self.button1.text) >= self.every_second_income*100:
            self.button1.text = str("%.2f" % (float(self.button1.text) - float(self.every_second_income)*100))
            self.button3.text = "add every second:\n" + str("%.2f" % self.every_second_income)
            self.every_second_income += 0.05

    def to_upgrade(self, args):         # Збільшую кількість очок за один клік на 10%
        if float(self.button1.text) >= self.adder*10:
            self.button1.text = str("%.2f" % (float(self.button1.text) - self.adder*10))
            self.adder *= 1.1
            self.button2.text = "Upgrade to 10%\nYour adder is:\n" + str("%.2f" % self.adder)

    def build(self):                    # Задаємо всі параметри і змінні, а також структуру і розміщення елементів
        self.title = "Clicker by W.R."
        self.x = 0
        self.adder = 1
        self.upgrade_result ="<--Click here*\n\n\nUpgrade to 10%!\nYour adder is:\n" + str(self.adder)
        self.every_second_income = 0.05
        self.button3_text = "add every second:\n" + str(self.every_second_income)
        self.gl = GridLayout(cols=2, padding=8)
        self.button1 = Button(                              # Чотири основні кнопки для взаємодії
            text = "0",
            font_size = 30,
            on_press = self.to_click,
            background_color = [1, 1, 1, 1]
        )

        self.button2 = Button(
            text = self.upgrade_result,
            font_size = 20,
            on_press = self.to_upgrade,
            background_color = [.88, .19, .77, 1]
        )
        self.button3 = Button(
            text = self.button3_text,
            font_size = 20,
            on_press = self.do_the_update,
            background_color = [.15, .88, .7, 1]
        )
        self.button4 = Button(
            text = "upgrade time adder\n + 0.05 every second",
            font_size = 20,
            on_press = self.upgrade_second,
            background_color = [.88, .19, .77, 1]
        )
        self.gl.add_widget(self.button1)
        self.gl.add_widget(self.button2)
        self.gl.add_widget(self.button3)
        self.gl.add_widget(self.button4)
        self.bl = BoxLayout(orientation="vertical")
        self.bl.add_widget(self.gl)
        self.bl.add_widget(Label(
            text="Розроблено Владиславом Рудиком",
            size_hint=[1,.05],
            font_size=18
        ))
        return self.bl

if __name__ == "__main__":                # Запускаємо програму, якщо вона відкрита, як самомтійний файл,
    The_Clicker_Program_App().run()       # а не імпортована, як бібліотека
