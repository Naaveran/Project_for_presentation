import json
import os
from kivy.app import App
from kivy.config import Config

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Config.set("graphics", "resizable", False)
Config.set("graphics", "width", "640")
Config.set("graphics", "height", "480")


class Simple_Base_Date_App(App):
	def check_db(self, args):
		if self.input_db_name.text + ".json" in os.listdir():
			self.result_info.text = "Успішно завантажено!"
			self.active_db = self.input_db_name.text
		else:
			self.result_info.text = "Нажаль, така база даних відсутня."

	def create_db(self, args):
		if len(self.input_db_name.text) > 0:
			if self.input_db_name.text + ".json" in os.listdir():
				self.result_info.text = "Така б.д. вже існує"
			else:
				with open(self.input_db_name.text+".json", "w") as basement:
					json.dump({}, basement)
					self.result_info.text = "Успішно створено б.д. за шляхом:\n" + os.getcwd()
		else:
			self.result_info.text = "Ви не вказали ім\'я для б.д."

	def set_name(self, args):
		if len(self.worker_name.text.split()) in [2, 3]:
			self.worker = self.worker_name.text
			self.result_info.text = "Працюємо з \"" + self.worker + "\""
		else:
			self.result_info.text = "Невірно введений формат імені\n(Прізвище  Ім\'я (+ додатк. По-батькові))"

	def add_worker_to_db(self, args):
		if len(self.worker.split()) in [2, 3] and self.active_db != "None":
			with open(self.active_db + ".json") as basement:
				z = json.load(basement)
			person = {
				"Ім'я" : self.worker,
				"День народження" : "Не зазначено",
				"Зарплатня" : 0,
				"Посада" : "Не зазначено"
			}
			with open(self.active_db + ".json", "w", encoding="utf-8") as basement:
				if self.worker in z:
					self.result_info.text = "Такий співробітник вже є у б.д."
				else:
					z[self.worker] = person
					self.result_info.text = "Успішно добавлено працівника \"" + self.worker + "\"\nдо бази даних \"" + self.active_db + "\""
				json.dump(z, basement)
		else:
			self.result_info.text = "Не завантажена б.д., або невірно введений\nформат імені(Прізвище  Ім\'я (+ додатк. По-батькові))"

	def get_some_information(self, args):
		with open(self.active_db + ".json", "r") as basement:
			z = json.load(basement)
			if len(self.worker.split()) in [2, 3] and self.active_db != "None" and self.worker in z:
				self.result_info.text = ""
				for i, j in z[self.worker].items():
					self.result_info.text += str(i) + " => " + str(j) + "\n"
			else:
				self.result_info.text = "Такого співробітника немає у базі даних."

	def delete_worker_from_db(self, args):
		if len(self.worker.split()) in [2, 3] and self.active_db != "None":
			with open(self.active_db + ".json") as basement:
				z = json.load(basement)
			with open(self.active_db + ".json", "w") as basement:
				if self.worker in z:
					del z[self.worker]
					self.result_info.text = "Інформацію про працівника\nуспішно видалено."
				else:
					self.result_info.text = "Такого працівника немає у б.д."
				json.dump(z, basement)

	def new_salary(self, args):
		if len(self.worker) > 0 and len(self.active_db) > 0:
			with open(self.active_db + ".json") as basement:
				z = json.load(basement)
			with open(self.active_db + ".json", "w") as basement:
				if self.worker in z:
					if self.next_salary.text.isdigit():
						z[self.worker]["Зарплатня"] = int(self.next_salary.text)
						self.result_info.text = "Співробітник " + self.worker + "тепер має зарплатню:\n" + str(z[self.worker]["Зарплатня"])
					else:
						self.result_info.text = "Введіть число"
				else:
					self.result_info.text = "Такого працівника немає у б.д."
				json.dump(z, basement)

	def new_birthday(self, args):
		if len(self.worker) > 0 and len(self.active_db) > 0:
			with open(self.active_db + ".json") as basement:
				z = json.load(basement)
			with open(self.active_db + ".json", "w") as basement:
				k = self.next_age.text.split(".")
				if self.worker in z:
					if self.next_age.text == z[self.worker]["День народження"]:
						self.result_info.text = "Ця дата вже є датою народження співробітника " + self.worker
					else:
						if len(k) == 3 and k[0].isdigit() and k[1].isdigit() and k[2].isdigit() and int(k[0]) in range(32) and int(k[1]) in range(13) and 0 < int(k[2]) < 2100:
							z[self.worker]["День народження"] = self.next_age.text
							self.result_info.text = "Дату народження " + self.worker + " успішно змінено на " + z[self.worker]["День народження"]
						else:
							self.result_info.text = "Невірний формат дати народження"
				json.dump(z, basement)

	def new_job(self, args):
		if len(self.worker) > 0 and len(self.active_db) > 0:
			with open(self.active_db + ".json") as basement:
				z = json.load(basement)
			with open(self.active_db + ".json", "w") as basement:
				if self.worker in z:
					if self.next_titul.text == z[self.worker]["Посада"]:
						self.result_info.text = "Співробітник вже займає\nцю посаду."
					else:
						z[self.worker]["Посада"] = self.next_titul.text
						self.result_info.text = "Тепер співробітник " + self.worker + " \nзаймає посаду " + z[self.worker]["Посада"]
				else:
					self.result_info.text = "Такого співробітника немає у б.д."
				json.dump(z, basement)
	def build(self):
		self.worker = "None"
		self.active_db = "None"

		self.button_create_db = Button(text="Створити базу даних", size_hint_x = None, width=200, background_color=[.100,.50,.700,.8], on_press=self.create_db)
		self.button_load_db = Button(text="Завантажити базу даних", size_hint_x = None, width=200, background_color=[.49,.94,.99,.8], on_press=self.check_db)


		self.input_db_name = TextInput(text="", hint_text="Назва бази даних", size_hint=[1, 0.05])
		self.result_info = Label(text="result", size_hint=[1, 0.2], color=[0,1,1,1], font_size=20)

		self.label_work = Label(text="Доступні дії:", color=[0, 1, 0, 1], size_hint=[1, 0.05])
		self.button_get_information = Button(text="Отримати інформацію.", background_color=[1,1,0,1], on_press=self.get_some_information)

		self.worker_name = TextInput(hint_text="Введіть імя співробітника", size_hint=[0.8, 1])
		self.button_add_worker = Button(text="Працюємо з ним.", size_hint=[0.2, 1], background_color=[.100,.50,.700, 1], on_press=self.set_name)

		self.button_add_to_db = Button(text="Додати працівника до бази даних.", background_color=[0,1,0,1], on_press=self.add_worker_to_db)
		self.delete_worker = Button(text="Видалити з бази данних.", background_color=[1,0,0,1], on_press=self.delete_worker_from_db)

		self.next_salary = TextInput(hint_text="Нова зарплатня:")
		self.confirm_salary = Button(text="Задати нову зарплатню.", background_color=[.100,.50,.700, 1], on_press=self.new_salary)

		self.next_age = TextInput(hint_text="Дата народження співробітника:")
		self.confirm_age = Button(text="Змінити.", background_color=[.100,.50,.700, 1], on_press=self.new_birthday)

		self.next_titul = TextInput(hint_text="Нова посада")
		self.confirm_titul = Button(text="Підвищити.", background_color=[.100,.50,.700, 1], on_press=self.new_job)


		bl1 = BoxLayout(orientation="vertical")

		gl1 = GridLayout(cols=2, size_hint=[1, 0.2])

		gl2 = GridLayout(cols=2, size_hint=[1, 0.3])

		gl2.add_widget(self.worker_name)
		gl2.add_widget(self.button_add_worker)
		gl2.add_widget(self.label_work)
		gl2.add_widget(self.button_get_information)
		gl2.add_widget(self.button_add_to_db)
		gl2.add_widget(self.delete_worker)
		gl2.add_widget(self.next_salary)
		gl2.add_widget(self.confirm_salary)
		gl2.add_widget(self.next_age)
		gl2.add_widget(self.confirm_age)
		gl2.add_widget(self.next_titul)
		gl2.add_widget(self.confirm_titul)


		gl4 = GridLayout(cols=2, size_hint=[1, 0.2])
		gl4.add_widget(self.result_info)

		gl5 = GridLayout(cols=2)

		gl1.add_widget(Label(text="Для початку роботи, введіть назву бази даних і створіть її,\n або завантажте, натиснувши відповідну кнопку.", size_hint_x = None, width=440, color=[0,1,0,1]))
		gl1.add_widget(self.button_create_db)
		gl1.add_widget(Label(text="Після цього введіть Ім\'я та Прізвище працівника і натисніть\n \"Працювати з ним\". Тепер можете змінювати параметри", size_hint_x=None, width=440, color=[0,1,0,1]))
		gl1.add_widget(self.button_load_db)

		bl1.add_widget(gl1)
		bl1.add_widget(self.input_db_name)
		bl1.add_widget(gl2)
		bl1.add_widget(gl4)
		bl1.add_widget(Label(text="Розроблено Владиславом Рудиком.", size_hint=[1, 0.05]))
		return bl1

if __name__ == "__main__":
	Simple_Base_Date_App().run()
