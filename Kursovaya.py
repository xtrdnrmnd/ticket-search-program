import datetime
from random import randint

import Table
from PIL import ImageTk
import requests
import tkinter as tk
import json
import urllib
from tkcalendar import Calendar
import LinkedLists
from tkinter import messagebox as mb


class Interface(tk.Frame):

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.set_mainWindow()
        self.init_buttons()
        self.init_vars()
        self.init_labels()

    def set_mainWindow(self):
        # Создание поля баннера приложения
        self.canvas = tk.Canvas(self.main, width=1400, height=170, bg='#B0BF1A', highlightthickness=0, bd=0)
        #self.image = ImageTk.PhotoImage(file='/Users/pollinbrice/Documents/3 семестр/ АОД/Kursovaya_logo.jpg')
        #self.canvas.logo = self.canvas.create_image(700, 90, image=self.image)
        #self.canvas.pack()

        self.canvas4 = tk.Canvas(self.main, width=1400, height=170, bg='#B0BF1A', highlightthickness=0, bd=0)
        #self.image4 = ImageTk.PhotoImage(
            #file='/Users/pollinbrice/Downloads/Всякие штуки для курсача/Курсовая_лого_2.jpg')
        self.canvas4.logo = self.canvas4.create_image(700, 90, image=self.image4)
        self.canvas4.pack(side=tk.BOTTOM)

        self.canvas3 = tk.Canvas(root, width=1400, height=570, bg='#B0BF1A', highlightthickness=0, bd=0)
        self.canvas5 = tk.Canvas(root, bg='#B0BF1A')

        self.arrivDate = tk.StringVar
        self.departDate = tk.StringVar

    # Календарь 1
    def application1(self):
        def print_sel():
            self.departDate = cal.selection_get()
            cal.pack_forget()
            top.destroy()

        top = tk.Toplevel(root)

        now = datetime.datetime.now()

        cal = Calendar(top,
                       font="Arial 14", headersforeground='#B0BF1A', selectbackground='black', selectmode='day',
                       cursor="hand1", year=now.year, month=now.month)
        cal.pack(fill="both", expand=True)
        tk.Button(top, text="ok", command=print_sel).pack()

    # Календарь 2
    def application2(self):
        def print_sel():
            self.arrivDate = cal.selection_get()
            cal.pack_forget()
            top.destroy()

        top = tk.Toplevel(root)

        now = datetime.datetime.now()

        cal = Calendar(top,
                       font="Arial 14", headersforeground='#B0BF1A', selectbackground='black', selectmode='day',
                       cursor="hand1", year=now.year, month=now.month, day=5)
        cal.pack(fill="both", expand=True)
        tk.Button(top, text="ok", command=print_sel).pack()

    # Работа кнопки "Мой аккаунт"
    def my_account(self):
        canvas6 = tk.Canvas(root, bg='#B0BF1A', highlightthickness=0, bd=0)
        LB = tk.Label(canvas6, bg='#B0BF1A', text=("Всего заказанных билетов", dataBase.length))
        t = Table.SimpleTable(canvas6, dataBase.length, 2)

        def history():
            def back2():
                canvas6.pack_forget()
                self.check_info.config(state=tk.NORMAL)

            canvas6.pack(side=tk.RIGHT)

            self.order_history.config(state=tk.DISABLED)
            if dataBase.length != 0:
                LB.pack()
                t.pack()
                t.set(0, 0, "Номер")
                t.set(0, 1, "Билет")
                i = 0
                for f in range(0, cities.length):
                    t.set(f, 0, i)
                    t.set(f, 1, cities.__getitem__(f))
                    i += 1
                back = tk.Button(canvas6, text="Вернуться в главное меню", command=back2)
                back.pack()
            else:
                mb.showerror("Ошибка", "История заказов пуста")

        def bback():
            canvas6.pack_forget()

        def info():
            def look_up():
                LB.pack_forget()
                t.pack_forget()
                if info_num.get().isalpha():
                    mb.showerror("Ошибка", "Проверьте правильность ввода")
                    getinfo.delete(0, tk.END)
                for f in range(1, dataBase.length + 1):
                    if int(info_num.get()) == f:
                        canvas6.pack_forget()
                        fr = tk.Frame(root, bg='#B0BF1A')
                        fr.pack(side=tk.RIGHT)
                        string = (dataBase.__getitem__(f - 1))
                        kkk = tk.Label(fr, bg='#B0BF1A', font='Arial 20', text=("Данные по билету:\nимя:", string[0],
                                                                                "\nфамилия:", string[2], "\nотчество",
                                                                                string[4], "\nпаспорт:", string[6],
                                                                                "\nмэйл:", string[8], "\nстоимость:",
                                                                                string[10], "номер-", string[12]),
                                       wraplength=400)
                        kkk.pack()
                        backkk = tk.Button(fr, text="Назад", command=bback)
                        backkk.pack()
                        self.check_info.config(state=tk.NORMAL)
                    else:
                        break
                if int(info_num.get()) > dataBase.length + 1:
                    mb.showerror("Ошибка", "Проверьте правильность ввода")
                    getinfo.delete(0, tk.END)

            self.check_info.config(state=tk.DISABLED)
            if dataBase.length != 0:
                canvas6.pack(side=tk.RIGHT)
                info_lb = tk.Label(canvas6, bg='#B0BF1A', text="Введите номер заказа:")
                info_lb.pack()
                info_num = tk.StringVar()
                getinfo = tk.Entry(canvas6, textvariable=info_num)
                getinfo.pack()
                getinfo2 = tk.Button(canvas6, text="Найти", command=look_up)
                getinfo2.pack()
                back = tk.Button(canvas6, text="Вернуться в главное меню", command=bback)
                back.pack()
            else:
                mb.showerror("Ошибка", "История заказов пуста")

        self.entryDepart.place_forget()
        self.entryArriv.place_forget()
        self.theDepartDateLabel.place_forget()
        self.searchButton.place_forget()
        self.theArrivQuestLabel.place_forget()
        self.theArrivDateLabel.place_forget()
        self.theDepartQuestLabel.place_forget()
        self.DepartDatePicker.place_forget()
        self.ArrivDatePicker.place_forget()

        self.canvas5.pack(side=tk.LEFT)

        self.order_history = tk.Button(self.canvas5, width=90, height=3, text="ПОСМОТРЕТЬ ИСТОРИЮ ЗАКАЗОВ",
                                       command=history)
        self.order_history.grid(column=0, row=0)
        self.check_info = tk.Button(self.canvas5, width=90, height=3, text="ПОСМОТРЕТЬ ИНФОРМАЦИЮ ПО ЗАКАЗАННЫМ "
                                                                           "АВИАБИЛЕТАМ", command=info)
        self.check_info.grid(column=0, row=1)

    # Работа кнопки "карта низких цен"
    def picture(self):
        self.image3 = ImageTk.PhotoImage(file='/Users/pollinbrice/Downloads/maxresdefault.jpg')
        self.canvas3.logo = self.canvas3.create_image(400, 300, image=self.image3)
        self.canvas3.pack(side=tk.BOTTOM)

        Nadpis = tk.Label(self.canvas3, bg='#B0BF1A',
                          text="Данное окно находится в разработке, пока можете полюбоваться на "
                               "картинку из интернета:)))", font='Arial 30', wraplength=500)
        Nadpis.place(x=700, y=300)
        self.canvas4.pack_forget()
        self.canvas.pack_forget()

    def search_button_init(self):
        global DurationLL
        self.entryDepart.place_forget()
        self.entryArriv.place_forget()

        self.theDepartDateLabel.place_forget()
        self.searchButton.place_forget()
        self.theArrivQuestLabel.place_forget()
        self.theArrivDateLabel.place_forget()
        self.theDepartQuestLabel.place_forget()

        self.DepartDatePicker.place_forget()
        self.ArrivDatePicker.place_forget()

        self.depart_city = self.departCity.get()
        self.arriv_city = self.arrivCity.get()
        self.depart_date = self.departDate
        self.arriv_date = self.arrivDate

        if self.departCity.get() is '' or self.arriv_city is '':
            mb.showerror("Ошибка", "Проверьте заполнение полей откуда и куда!")
        else:
            # При помощи парсировки файла, содержащего данные, получаем данные о международных аббревиатурах для городов
            with urllib.request.urlopen("http://api.travelpayouts.com/data/ru/cities.json") as url:
                parsed_data = json.loads(url.read().decode())
            # Присваеваем значения аббревиатур переменным
            for i in parsed_data:
                if i['name'] == self.depart_city:
                    self.depart_city = i['code']
            for i in parsed_data:
                if i['name'] == self.arriv_city:
                    self.arriv_city = i['code']

            # Используем API для получения динамичных данных о существующих рейсах
            url = "http://api.travelpayouts.com/v2/prices/latest"
            parameters = {"origin": self.depart_city, "destination": self.arriv_city, "depart_date": self.depart_date,
                          "return_date": self.arriv_date}
            headers = {'x-access-token': ''}
            response = requests.request("GET", url, headers=headers, params=parameters)
            d = response.json()
            ld = d["data"]
            if d['success'] == "false":
                mb.showerror("Ошибка", "Проверьте введнные данные")
            else:
                cities.add(("Откуда:", self.depart_city, "Куда:", self.arriv_city))
                PriceLL = LinkedLists.LinkedList()
                for i in range(len(ld)):
                    PriceLL.add(d['data'][i]['value'])
                ChangesLL = LinkedLists.LinkedList()
                for i in range(len(ld)):
                    ChangesLL.add(d['data'][i]['number_of_changes'])
                DurationLL = LinkedLists.LinkedList()
                for i in range(len(ld)):
                    DurationLL.add(d['data'][i]['duration'])
                SitesLL = LinkedLists.LinkedList()
                for i in range(len(ld)):
                    SitesLL.add(d['data'][i]['gate'])

                def on_configure(event):
                    canvas2.configure(scrollregion=canvas2.bbox('all'))

                canvas2 = tk.Canvas(root, width=1380, height=700, bg='#B0BF1A')
                canvas2.pack(side=tk.LEFT)

                scrollbar = tk.Scrollbar(root, command=canvas2.yview)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                canvas2.configure(yscrollcommand=scrollbar.set)
                canvas2.bind('<Configure>', on_configure)

                def order():
                    def ticket_ordered():
                        if client_name.get().isalpha():
                            if client_lastname.get().isalpha():
                                if client_middlename.get().isalpha():
                                    if passport.get().isalnum():
                                        if email.get().__contains__("@"):
                                            if email.get().__contains__(".ru") or email.get().__contains__(".com"):
                                                yy = randint(10000, 99999)
                                                mb.showinfo("Билет успешно оформлен", ("Номер вашего билета:", yy))
                                                dataBase.add(
                                                    (client_name.get(), ",", client_lastname.get(), ",",
                                                     client_middlename.get(), ",",
                                                     passport.get(), ",", email.get(), ",", PriceLL.__getitem__(f), ","
                                                     , yy))
                                                canvas2.destroy()
                                            else:
                                                mb.showerror("Ошибка", "Почта указана неверно")
                                        else:
                                            mb.showerror("Ошибка", "Почта указана неверно")
                                    else:
                                        mb.showerror("Ошибка",
                                                     "Номер российского паспорта должен содержать только числа")
                                else:
                                    mb.showerror("Ошибка", "Отчество не может содержать числа")
                                    entr3.delete(0, tk.END)
                            else:
                                mb.showerror("Ошибка", "Фамилия не может содержать числа")
                                entr2.delete(0, tk.END)
                        else:
                            mb.showerror("Ошибка", "Имя не может содержать числа")
                            entr1.delete(0, tk.END)

                    def go_to_main_frame():
                        canvas2.destroy()

                    lbl1 = tk.Label(frame, text="Введите ваши данные:", font="Arial 14", bg='#B0BF1A')
                    lbl1.grid(column=1, row=1)
                    lbl2 = tk.Label(frame, text="Имя:", font="Arial 12", bg='#B0BF1A')
                    lbl2.grid(column=1, row=2, sticky=tk.E)
                    client_name = tk.StringVar()
                    entr1 = tk.Entry(frame, textvariable=client_name, font="Arial 14")
                    entr1.grid(column=2, row=2)
                    lbl3 = tk.Label(frame, text="Фамилия:", font="Arial 12", bg='#B0BF1A')
                    lbl3.grid(column=1, row=3, sticky=tk.E)
                    client_lastname = tk.StringVar()
                    entr2 = tk.Entry(frame, textvariable=client_lastname, font="Arial 14")
                    entr2.grid(column=2, row=3)
                    lbl4 = tk.Label(frame, text="Отчество:", font="Arial 12", bg='#B0BF1A')
                    lbl4.grid(column=1, row=4, sticky=tk.E)
                    client_middlename = tk.StringVar()
                    entr3 = tk.Entry(frame, textvariable=client_middlename, font="Arial 14")
                    entr3.grid(column=2, row=4, rowspan=1)
                    lbl5 = tk.Label(frame, text="Паспорт:", font="Arial 12", bg='#B0BF1A')
                    lbl5.grid(column=1, row=5, sticky=tk.E)
                    passport = tk.StringVar()
                    entr4 = tk.Entry(frame, textvariable=passport, font="Arial 14")
                    entr4.grid(column=2, row=5, rowspan=1)
                    lbl6 = tk.Label(frame, text="Адрес электронной почты:", font="Arial 12", bg='#B0BF1A')
                    lbl6.grid(column=1, row=6, sticky=tk.E)
                    email = tk.StringVar()
                    entr5 = tk.Entry(frame, textvariable=email, font="Arial 14")
                    entr5.grid(column=2, row=6, rowspan=1)
                    btn1 = tk.Button(frame, text="Заказать билет", font="Arial 20", command=ticket_ordered)
                    btn1.grid(column=1, row=7)
                    btn1 = tk.Button(frame, text="Отменить заказ", font="Arial 20", command=go_to_main_frame)
                    btn1.grid(column=2, row=7)

            frame = tk.Frame(canvas2, bg='#B0BF1A')
            canvas2.create_window((0, 0), window=frame, anchor='nw')
            button = []
            for f in range(len(ld)):
                button.append(
                    tk.Button(frame, bg='#B0BF1A', font="Arial 16", text=("Стоимость:", PriceLL.__getitem__(f),
                                                                          "\nКоличество пересадок:",
                                                                          ChangesLL.__getitem__(f),
                                                                          "\nДлительность:",
                                                                          DurationLL.__getitem__(f)),
                              command=order))

            for i, x in enumerate(button):
                x.grid(column=0, row=i + 1, sticky=tk.W)

    def search_init(self):
        self.canvas3.pack_forget()

        self.entryDepart.place(x=200, y=230)
        self.entryArriv.place(x=810, y=230)
        self.theDepartDateLabel.place(x=100, y=370)
        self.searchButton.place(x=960, y=500)
        self.theArrivQuestLabel.place(x=730, y=230)
        self.theArrivDateLabel.place(x=730, y=370)
        self.theDepartQuestLabel.place(x=100, y=230)
        self.DepartDatePicker.place(x=330, y=370)
        self.ArrivDatePicker.place(x=970, y=370)

        self.canvas4.pack(side=tk.BOTTOM)
        self.canvas5.pack_forget()

    def init_vars(self):
        # Создание полей ввода и присвоение переменных
        self.departCity = tk.StringVar()
        self.entryDepart = tk.Entry(textvariable=self.departCity, width=50)
        self.entryDepart.place(x=200, y=230)

        self.arrivCity = tk.StringVar()
        self.entryArriv = tk.Entry(textvariable=self.arrivCity, width=50)
        self.entryArriv.place(x=810, y=230)

    def init_buttons(self):
        # Инициализация кнопок
        self.theSearchButton = tk.Button(height=2, width=50, text='ПОИСК', command=self.search_init)
        self.theSearchButton.place(x=0, y=172)

        self.theLowPriceMapButton = tk.Button(height=2, width=50, text='КАРТА НИЗКИХ ЦЕН', command=self.picture)
        self.theLowPriceMapButton.place(x=480, y=172)

        self.theAccountButton = tk.Button(height=2, width=50, text='ЛИЧНЫЙ КАБИНЕТ', command=self.my_account)
        self.theAccountButton.place(x=960, y=172)

        self.searchButton = tk.Button(height=3, width=30, text="ИСКАТЬ", font='Arial 20',
                                      command=self.search_button_init)
        self.searchButton.place(x=960, y=500)

        self.DepartDatePicker = tk.Button(root, text="Выберите дату", font='Arial 20', command=self.application1)
        self.DepartDatePicker.place(x=330, y=370)

        self.ArrivDatePicker = tk.Button(root, text="Выберите дату", font='Arial 20', command=self.application2)
        self.ArrivDatePicker.place(x=970, y=370)

    def init_labels(self):
        self.theDepartQuestLabel = tk.Label(text='ОТКУДА:', font='Arial 20', bg='#B0BF1A')
        self.theDepartQuestLabel.place(x=100, y=230)

        self.theArrivQuestLabel = tk.Label(text='КУДА:', font='Arial 20', bg='#B0BF1A')
        self.theArrivQuestLabel.place(x=730, y=230)

        self.theDepartDateLabel = tk.Label(text='ДАТА ОТПРАВЛЕНИЯ: ', bg='#B0BF1A', font='Arial 20')
        self.theDepartDateLabel.place(x=100, y=370)

        self.theArrivDateLabel = tk.Label(text='ДАТА ВОЗВРАЩЕНИЯ: ', bg='#B0BF1A', font='Arial 20')
        self.theArrivDateLabel.place(x=730, y=370)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("AviaGo")
    root['bg'] = '#B0BF1A'
    # Задание размера окна
    root.geometry("1400x900+0+0")
    cities = LinkedLists.LinkedList()
    dataBase = LinkedLists.LinkedList()
    app_main = Interface(root)

    root.mainloop()
