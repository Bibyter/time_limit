from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import socket
import traceback

def send_bonuscode():
    global e
    try:
        client = socket.socket()
        # подключаемся по адресу www.python.org и порту 80
        client.connect(('127.0.0.1', 49))
        # данные для отправки - стандартные заголовки протокола http
        message = 'activate_bonuscode {0}'.format(e.get())
        print("Connecting...")
        client.send(message.encode())       # отправляем данные серверу
        data = client.recv(1024).decode()          # получаем данные с сервера
        print("Server sent: ", data)    # выводим данные на консоль
        client.close()                      # закрываем подключение
    except Exception as ex:
        print(traceback.format_exc())
        showerror(title="Ошибка", message="Подключение не установлено")
        return
    
    datasplit = data.split(',')
    
    if datasplit[0] == 'success':
        bonustime = datasplit[1]
        showinfo(title="Информация", message='Код на {0} минут успешно активирован!'.format(bonustime))
    else:
        showerror(title="Ошибка", message="Бонус код не подходит!")
    


root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("300x100")    # устанавливаем размеры окна

label = ttk.Label(text='*Введите бонус код...') # создаем текстовую метку
label.pack(side=TOP)    # размещаем метку в окне

e = ttk.Entry(font='Consolas 20')
e.pack(side=TOP, padx=10, pady=5)
#e.entry1.bind('<KeyRelease>', self.datemask)

b = ttk.Button(text='Применить', command=send_bonuscode)
b.pack(side=TOP)


 
root.mainloop()