import telebot
import const
import os
import random
bot=telebot.TeleBot(const.token)
# процес при команді go_game
#zs = f.readlines()# відкриваємо файл з містами і записуємо в список
#f.close()
fs=[] #створили пустий список
index=0
vuvt = "К"
@bot.message_handler(commands=['start'])
def handle_text(message):
    f = open('mista.txt')
    fname = message.from_user.first_name  # взнаємо імя користувача
    lname = message.from_user.last_name  # взнаємо прізвище користувача
    uname = message.from_user.username
    try:
        nic = fname + lname + uname  # нік користувача
    except TypeError:
        try:
            nic = fname + lname + "Uname"
        except TypeError:
            nic = fname + "lname" + "Uname"
    nametf = "spusok" + nic + ".txt"
    # Відкриваємо загальний файл і записуємо з загального в особистий
    spusoktf = open(nametf, "w")  # відкриваємо файл списку для користувача
    for line in f:
        spusoktf.write(line + '\n')  # заповнюємо файл список користувача
    f.close()
    spusoktf.close()
    # створюємо і заповнюємо файл остайньої літери
    ntf = nic + ".txt"
    tf = open(ntf, "w")  # відкриваємо файл для користувача
    tf.write(vuvt)  # заповнюємо файл користувача
    tf.close()


@bot.message_handler(commands=['go_game'])
def handle_text(message):
    global index
    f = open('mista.txt')
    bot.send_message(message.chat.id, "Я починатиму першим! І пам`ятай назви міст пишуться з великої літери 😉")
    bot.send_message(message.chat.id, "Івано-Франківськ")
    index=0
    fname = message.from_user.first_name  # взнаємо імя користувача
    lname = message.from_user.last_name  # взнаємо прізвище користувача
    uname = message.from_user.username
    try:
        nic = fname + lname + uname  # нік користувача
    except TypeError:
        try:
            nic = fname + lname + "Uname"
        except TypeError:
            nic = fname + "lname" + "Uname"
    nametf="spusok"+nic+".txt"
    #Відкриваємо загальний файл і записуємо з загального в особистий
    spusoktf = open(nametf, "w")  # відкриваємо файл списку для користувача
    for line in f:
        spusoktf.write(line + '\n')  # заповнюємо файл список користувача
    f.close()
    spusoktf.close()
    #створюємо і заповнюємо файл остайньої літери
    ntf = nic + ".txt"
    tf = open(ntf, "w")  # відкриваємо файл для користувача
    tf.write(vuvt)  # заповнюємо файл користувача
    tf.close()

    #перший варіант взаємодії з гравцем
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        fname = message.from_user.first_name  # взнаємо імя користувача
        lname = message.from_user.last_name  # взнаємо прізвище користувача
        uname = message.from_user.username
        try:
            nic = fname + lname + uname  # нік користувача
        except TypeError:
            try:
                nic = fname + lname + "Uname"
            except TypeError:
                nic = fname + "lname" + "Uname"

        global index
        global vuvt
        # Записуємо в список
        nametf = "spusok" + nic + ".txt"
        spusoktfo = open(nametf)
        zs = spusoktfo.readlines()
        fs.extend(zs)
        #print(fs)
        spusoktfo.close()
        mt = message.text
        print(nic)
        print(mt)

        ntf = nic + ".txt"
        tfo = open(ntf)  # відкриваємо файл для користувача
        stfo = tfo.readlines()
        tfo.close()

        vuvtup = stfo[0]

        if fs.__len__()!=0 and vuvtup == mt[0]:
            i=0
            #при умові що користувач закінчив буквою и або ь
            if mt[-1]!= 'и' and mt[-1]!= 'ь':
                ostlit = mt[-1]
            else:
                ostlit = mt[-2]
            ostlitup = ostlit.upper()
            #пошук на наявність слова в списку
            try:
                fs.remove(mt + "\n")
                while i < 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
                    try:
                        g = fs[i]
                        d = g[0:-1]
                        k = d[0]
                        #виконання при умові що слова ще є в запасі
                        if ostlitup == k:
                            bot.send_message(message.chat.id, d)
                            vuvt = d
                            index=3
                            fs.remove(d+"\n")
                            if vuvt[-1] != 'и' and vuvt[-1] != 'ь':
                                vuvostlit = vuvt[-1]
                            else:
                                vuvostlit = vuvt[-2]
                            vuvtup = vuvostlit.upper()
                            tf = open(ntf, "w")  # відкриваємо файл для користувача
                            tf.write(vuvtup)  # заповнюємо файл користувача
                            tf.close()
                            #Записуємо список в файл
                            spusoktf = open(nametf, "w")  #відкриваємо файл список для користувача
                            for index in fs:
                                spusoktf.write(index+"\n")
                            spusoktf.close()
                            fs.clear()
                            print(vuvt)
                            break
                            i=i+1
                        else:
                            i=i+1
                    except IndexError:
                        i=i+1
                #умова що закінчились слова
                if  ostlitup != k:
                    bot.send_message(message.chat.id, "твоя взяла 😒")
                    bot.send_message(message.chat.id, "Щоб зіграти щераз натисни /go_game")
                    print("твоя взяла")
                    fs.clear()
                    vuvt = "К"
            except ValueError:
                #при введені не міста
                bot.send_message(message.chat.id, "Ти програв! Такого міста немає або вже було 😝")
                bot.send_message(message.chat.id, "Щоб зіграти щераз натисни /go_game")
                print("Ти програв! Такого міста немає або вже було")
                fs.clear()
                vuvt = "К"
        elif fs.__len__()!=0 and vuvtup != mt[0]:
            # при виклику команди 'stop'
            if mt == '/stop':
                bot.send_message(message.chat.id, "вже йдеш? 😢")
                print("вже йдеш?")
                fs.clear()
                vuvt = "К"
                # при введені не міста
            else:
                bot.send_message(message.chat.id, "Я закінчив не на цю літеру 😔 Ти програв")
                bot.send_message(message.chat.id, "Щоб зіграти щераз натисни /go_game")
                print("Я закінчив не на цю літеру")
                fs.clear()
                vuvt = "К"

bot.polling(none_stop=True, interval=0)