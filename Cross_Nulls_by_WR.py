from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label

Config.set("graphics","resizable","0")                    # Задаємо параметри вікна
Config.set("graphics","width","444")
Config.set("graphics","height","444")

choice = ['X', 'O']; switch = 0                           # Глобальні змінні для почергової ходи

class The_Cross_and_Nulls_App(App):
    def start_game(self, args):
        global switch
        args.disabled = True
        args.text = choice[switch]
        if not switch: switch = 1
        else: switch = 0
        coordinate = (                                    # Створюємо матрицю з кортежів для визначення умови виграшу обох сторін
            (0,1,2),(3,4,5),(6,7,8), # X
            (0,3,6),(1,4,7),(2,5,8), # Y
            (0,4,8),(2,4,6),         # D
        )
        vector = (                                
            [self.button[x].text for x in (0,1,2)],
            [self.button[x].text for x in (3,4,5)],
            [self.button[x].text for x in (6,7,8)],
            [self.button[y].text for y in (0,3,6)],
            [self.button[y].text for y in (1,4,7)],
            [self.button[y].text for y in (2,5,8)],
            [self.button[d].text for d in (0,4,8)],
            [self.button[d].text for d in (2,4,6)],
        )
        win = False
        color = [0,1,0,1] # Green
        for i in range(8):                              # Перевірка умови виграшу після кожного ходу
            if vector[i].count('X') == 3\
            or vector[i].count('O') == 3:
                win = True
                for i in coordinate[i]:
                    self.button[i].color = color
                break
        if win:
            for i in range(9):
                self.button[i].disabled = True
    def restart(self, args):                            # Кнопка для перезапуску гри
        global switch; switch = 0
        for i in range(9):
            self.button[i].color = [0,0,0,1]
            self.button[i].text = ""
            self.button[i].disabled = False
    def build(self):                                    # Задаємо параметри, змінні і структуру програми
        self.title = "Cross-Nulls by W.R."
        bl = BoxLayout(orientation = "vertical", padding = 8, spacing = 5)
        gl = GridLayout(cols=3, spacing=1)
        self.button = [0 for _ in range(9)]
        for i in range(9):
            self.button[i]=Button(
                    color=[0,0,0,1],
                    font_size=24,
                    disabled=False,
                    on_press=self.start_game
                )
            gl.add_widget(self.button[i])
        bl.add_widget(gl)

        bl.add_widget(
            Button(
                text="Спробувати ще раз",
                size_hint=[1,.1],
                on_press=self.restart
            )
        )
        bl.add_widget(Label(
                text="Розроблено Владиславом Рудиком",
                size_hint=[1,.05]))
        return bl

if __name__ == "__main__":
    The_Cross_and_Nulls_App().run()
