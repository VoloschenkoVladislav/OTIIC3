import tkinter
import re
from encoder import GilbertMoureEncode
from even_encoder import EvenEncode
from hemming_encoder import HemmingEncoder

window = tkinter.Tk()
window.title('Помехоустойчивое кодирование')

window.columnconfigure([0, 1, 2], weight=1, minsize=50)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight=1, minsize=50)

frm_title1 = tkinter.Frame(master=window)
frm_title1.grid(row=0, column=0)
frm_input1 = tkinter.Frame(master=window)
frm_input1.grid(row=1, column=0)
frm_output1 = tkinter.Frame(master=window)
frm_output1.grid(row=1, column=1)
frm_controller1 = tkinter.Frame(master=window)
frm_controller1.grid(row=2, column=0)

lbl_title1 = tkinter.Label(master=frm_title1, text='Кодирование с обнаружением ошибок')
lbl_title1.pack(padx=50, pady=50)
lbl_input1 = tkinter.Label(master=frm_input1, text='Введите строку')
lbl_output1 = tkinter.Label(master=frm_output1, text='Результат')
lbl_input1.pack(padx=5, pady=5)
lbl_output1.pack(padx=5, pady=5)
ent_input1 = tkinter.Entry(master=frm_input1, width=50)
ent_output1 = tkinter.Entry(master=frm_output1, width=50)
ent_input1.pack(padx=5, pady=5)
ent_output1.pack(padx=5, pady=5)

def appEncode(event):
    message = ent_input1.get()
    output = ent_output1
    if not re.fullmatch(r'[\+\*/=-]*', r'%s' % message):
        output.delete(0, tkinter.END)
        output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
    else:
        encoder = EvenEncode()
        outText = encoder.encode(message)
        output.delete(0, tkinter.END)
        output.insert(0, outText)

btn_encode1 = tkinter.Button(text='Закодировать', master=frm_controller1)
btn_encode1.bind('<Button-1>', appEncode)
btn_encode1.pack()


frm_input2 = tkinter.Frame(master=window)
frm_input2.grid(row=3, column=0)
frm_output2 = tkinter.Frame(master=window)
frm_output2.grid(row=3, column=1)
frm_controller2 = tkinter.Frame(master=window)
frm_controller2.grid(row=4, column=0)
frm_error1 = tkinter.Frame(master=window)
frm_error1.grid(row=4, column=1)

lbl_input2 = tkinter.Label(master=frm_input2, text='Введите строку')
lbl_output2 = tkinter.Label(master=frm_output2, text='Результат')
lbl_input2.pack(padx=5, pady=5)
lbl_output2.pack(padx=5, pady=5)
ent_input2 = tkinter.Entry(master=frm_input2, width=50)
ent_output2 = tkinter.Entry(master=frm_output2, width=50)
ent_input2.pack(padx=5, pady=5)
ent_output2.pack(padx=5, pady=5)
lbl_error1 = tkinter.Label(master=frm_error1, text='Ошибки')
ent_error1 = tkinter.Entry(master=frm_error1, width=50)
lbl_error1.pack(padx=5, pady=5)
ent_error1.pack(padx=5, pady=5)

def appDecode(event):
    message = ent_input2.get()
    output = ent_output2
    error = ent_error1
    if not re.fullmatch(r'[10]*', r'%s' % message):
        output.delete(0, tkinter.END)
        output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
    else:
        encoder = EvenEncode()
        outText = encoder.decode(message)
        if not outText:
            output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
        else:
            output.delete(0, tkinter.END)
            output.insert(0, outText[0])
            error.delete(0, tkinter.END)
            e = ''
            if outText[1]:
                e = 'Обнаружены ошибки на позициях: '
                for i in outText[1]:
                    e += str(i + 1) + ', '
                e = e[:-2]
            else:
                e = 'Ошибок не обнаружено'
            error.insert(0, e)

btn_decode1 = tkinter.Button(text='Раскодировать', master=frm_controller2)
btn_decode1.bind('<Button-1>', appDecode)
btn_decode1.pack()







frm_title2 = tkinter.Frame(master=window)
frm_title2.grid(row=5, column=0)
frm_input3 = tkinter.Frame(master=window)
frm_input3.grid(row=6, column=0)
frm_output3 = tkinter.Frame(master=window)
frm_output3.grid(row=6, column=1)
frm_controller3 = tkinter.Frame(master=window)
frm_controller3.grid(row=7, column=0)

lbl_title2 = tkinter.Label(master=frm_title2, text='Кодирование с исправлением ошибок')
lbl_title2.pack(padx=50, pady=50)
lbl_input3 = tkinter.Label(master=frm_input3, text='Введите строку')
lbl_output3 = tkinter.Label(master=frm_output3, text='Результат')
lbl_input3.pack(padx=5, pady=5)
lbl_output3.pack(padx=5, pady=5)
ent_input3 = tkinter.Entry(master=frm_input3, width=50)
ent_output3 = tkinter.Entry(master=frm_output3, width=50)
ent_input3.pack(padx=5, pady=5)
ent_output3.pack(padx=5, pady=5)

def appEncodeHemming(event):
    print(1)
    message = ent_input3.get()
    output = ent_output3
    if not re.fullmatch(r'[01]*', r'%s' % message):
        output.delete(0, tkinter.END)
        output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
    else:
        encoder = HemmingEncoder()
        outText = encoder.encode(message)
        print(outText)
        output.delete(0, tkinter.END)
        output.insert(0, outText)

btn_encode2 = tkinter.Button(text='Закодировать', master=frm_controller3)
btn_encode2.bind('<Button-1>', appEncodeHemming)
btn_encode2.pack()











frm_input4 = tkinter.Frame(master=window)
frm_input4.grid(row=8, column=0)
frm_output4 = tkinter.Frame(master=window)
frm_output4.grid(row=8, column=1)
frm_controller4 = tkinter.Frame(master=window)
frm_controller4.grid(row=9, column=0)
frm_error2 = tkinter.Frame(master=window)
frm_error2.grid(row=9, column=1)

lbl_input4 = tkinter.Label(master=frm_input4, text='Введите строку')
lbl_output4 = tkinter.Label(master=frm_output4, text='Результат')
lbl_input4.pack(padx=5, pady=5)
lbl_output4.pack(padx=5, pady=5)
ent_input4 = tkinter.Entry(master=frm_input4, width=50)
ent_output4 = tkinter.Entry(master=frm_output4, width=50)
ent_input4.pack(padx=5, pady=5)
ent_output4.pack(padx=5, pady=5)
lbl_error2 = tkinter.Label(master=frm_error2, text='Ошибки')
ent_error2 = tkinter.Entry(master=frm_error2, width=100)
lbl_error2.pack(padx=5, pady=5)
ent_error2.pack(padx=5, pady=5)

def appDecodeHemming(event):
    message = ent_input4.get()
    output = ent_output4
    error = ent_error2
    if not re.fullmatch(r'[10]*', r'%s' % message):
        output.delete(0, tkinter.END)
        output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
    else:
        encoder = HemmingEncoder()
        outText = encoder.decode(message)
        if not outText:
            output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
        else:
            output.delete(0, tkinter.END)
            output.insert(0, outText[0])
            error.delete(0, tkinter.END)
            if outText[1]:
                e = 'Обнаружены ошибки (слово, индекс ошибки): '
                for i in outText[1]:
                    e += '(' + str(i[0] + 1) + ', ' + str(i[1] + 1) + '), '
                e = e[:-2]
            else:
                e = 'Ошибок не обнаружено'
            error.insert(0, e)


btn_decode2 = tkinter.Button(text='Раскодировать', master=frm_controller4)
btn_decode2.bind('<Button-1>', appDecodeHemming)
btn_decode2.pack()






# frm_craft1 = tkinter.Frame(master=window)
# frm_craft1.grid(row=6, column=0)
# lbl_craft1 = tkinter.Label(master=frm_craft1, text='Неравенство Крафта:')
# lbl_craft1.pack(padx=5, pady=5)
# frm_craft2 = tkinter.Frame(master=window)
# frm_craft2.grid(row=6, column=1)
# lbl_craft2 = tkinter.Label(master=frm_craft2, text= 'Соблюдается' if craft_num <= 1 else 'Не соблюдается')
# lbl_craft2.pack(padx=5, pady=5)

window.mainloop()