import random
import string
import time

import pywinauto
from pywinauto import application

import sms_activate_new
import sms_active
from account import save_account, save_creditional
from change_proxy import update_proxy, save_proxy

number = {1: (450, 540),
          2: (550, 540),
          3: (670, 540),
          4: (450, 590),
          5: (550, 590),
          6: (670, 590),
          7: (450, 640),
          8: (550, 640),
          9: (670, 640),
          0: (550, 680)
          }

sex = {
    "w": (705, 200),
    "m": (705, 232)
}

names = [("Александр", "m"),
         ("Михаил", "m"),
         ("Максим", "m"),
         ("Артем", "m"),
         ("Даниил", "m"),
         ("Марк", "m"),
         ("Иван", "m"),
         ("Лев", "m"),
         ("Дмитрий", "m"),
         ("Матвей", "m"),
         ("Роман", "m"),
         ("Тимофей", "m"),
         ("Кирилл", "m"),
         ("Илья", "m"),
         ("Никита", "m"),
         ("Андрей", "m"),
         ("Федор", "m"),
         ("Егор", "m"),
         ("Алексей", "m"),
         ("Константин", "m"),
         ("Владимир", "m"),
         ("Ярослав", "m"),
         ("Мухаммад", "m"),
         ("София", "m"),
         ("Мария", "w"),
         ("Анна", "w"),
         ("Алиса", "w"),
         ("Виктория", "w"),
         ("Полина", "w"),
         ("Ева", "w"),
         ("Елизавета", "w"),
         ("Александра", "w"),
         ("Анастасия", "w"),
         ("Варвара", "w"),
         ("Дарья", "w"),
         ("Ксения", "w"),
         ("Вероника", "w"),
         ("Василиса", "w"),
         ("Арина", "w"),
         ("Екатерина", "w"),
         ("Милана", "w"),
         ("Екатерина", "w"),
         ("Кира", "w"),
         ("Валерия", "w"),
         ("Мирослава", "w"),
         ("Ульяна", "w"),
         ("Вера", "w"),
         ("Амина", "w"),
         ("Таисия", "w"),
         ]
last_names = ["Гусь", "Лось", "Крот", "Холод", "Царь", "Князь", "Шабан", "Юсуп", "Бык"]

autoreg_phone = 0


def get_number():
    if autoreg_phone == 1:
        return sms_active.get_number()
    else:
        return sms_activate_new.get_number()


def get_key(id):
    if autoreg_phone == 1:
        return sms_active.get_key(id)
    else:
        return sms_activate_new.get_key(id)


def get_pass(length):
    password = ''.join(random.choice(string.ascii_uppercase) for i in range(int(length / 2)))
    return password.join(random.choice(string.ascii_lowercase) for i in range(int(length / 2)))


def open_fb():
    pywinauto.mouse.click(coords=(410, 250))
    time.sleep(2)
    pywinauto.mouse.click(coords=(270, 350))
    time.sleep(2)


def open_nox():
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\MultiPlayerManager.exe")
    time.sleep(5)
    pywinauto.mouse.click(coords=(860, 240))
    return app


def restart():
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\MultiPlayerManager.exe")
    time.sleep(35)
    pywinauto.mouse.click(coords=(1030, 240))
    time.sleep(2)
    pywinauto.mouse.click(coords=(730, 460))
    print("delete cash")
    time.sleep(300)
    print("next")

    pywinauto.mouse.move(coords=(870, 420))
    time.sleep(2)

    pywinauto.mouse.click(coords=(1060, 240))
    time.sleep(2)
    pywinauto.mouse.click(coords=(760, 430))
    time.sleep(2)
    app.kill()
    time.sleep(10)
    app = open_nox()
    time.sleep(60)
    app.kill()
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\MultiPlayerManager.exe")
    time.sleep(2)
    pywinauto.mouse.click(coords=(860, 240))
    time.sleep(2)
    pywinauto.mouse.click(coords=(750, 420))
    app.kill()
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")
    time.sleep(60)
    open_fb()
    app.kill()


def start(proxy):
    print("start")
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")

    try:
        time.sleep(45)
        # pywinauto.mouse.move(coords=(640, 3proxy
        # 40))
        open_fb()

        time.sleep(55)
        # delete_user_from_phone()

        pywinauto.mouse.click(coords=(550, 320))
        time.sleep(2)
        pywinauto.mouse.click(coords=(613, 330))
        time.sleep(2)
        # Name
        name = random.choice(names)
        last_name = random.choice(last_names)
        pywinauto.keyboard.send_keys(str((name[0])))
        time.sleep(2)
        pywinauto.mouse.click(coords=(622, 198))
        pywinauto.mouse.click(coords=(624, 198))

        time.sleep(3)
        pywinauto.keyboard.send_keys(str((last_name)))
        time.sleep(2)
        pywinauto.mouse.click(coords=(620, 230))
        time.sleep(5)
        # Phone
        pywinauto.mouse.click(coords=(550, 250))
        for i in range(15):
            time.sleep(0.01)
            pywinauto.keyboard.send_keys('{BACKSPACE}')

        time.sleep(1.5)
        phone_number, id = get_number()
        if phone_number is None:
            time.sleep(5)
            app.kill()
            time.sleep(5)
            return False, None, None
        print(phone_number)
        time.sleep(1.5)
        pywinauto.keyboard.send_keys(str(phone_number).replace("+", ""))
        time.sleep(1.5)
        pywinauto.mouse.click(coords=(513, 288))
        # DO&B
        # day

        time.sleep(1.5)
        first_day_n = random.randint(1, 2)
        pywinauto.mouse.click(coords=(number.get(first_day_n)[0], number.get(first_day_n)[1]))
        time.sleep(1.5)
        first_day_n = random.randint(0, 9)
        pywinauto.mouse.click(coords=(number.get(first_day_n)[0], number.get(first_day_n)[1]))

        # month
        time.sleep(1.5)
        pywinauto.mouse.click(coords=(number.get(1)[0], number.get(1)[1]))
        time.sleep(1.5)
        first_month_n = random.randint(0, 2)
        pywinauto.mouse.click(coords=(number.get(first_month_n)[0], number.get(first_month_n)[1]))

        # year
        time.sleep(1.5)
        pywinauto.mouse.click(coords=(number.get(1)[0], number.get(1)[1]))
        time.sleep(1.5)
        pywinauto.mouse.click(coords=(number.get(9)[0], number.get(9)[1]))
        time.sleep(1.5)
        first_year_n = random.randint(5, 9)
        pywinauto.mouse.click(coords=(number.get(first_year_n)[0], number.get(first_year_n)[1]))
        time.sleep(1.5)
        first_year_n = random.randint(0, 9)
        pywinauto.mouse.click(coords=(number.get(first_year_n)[0], number.get(first_year_n)[1]))
        time.sleep(1.5)
        pywinauto.mouse.click(coords=(603, 245))

        # sex
        time.sleep(1.5)
        user_sex = sex.get(name[1])
        pywinauto.mouse.click(coords=(user_sex[0], user_sex[1]))

        # password
        time.sleep(1.5)
        password = get_pass(random.randint(3, 7))
        pywinauto.keyboard.send_keys(password)
        passwordn = get_pass(random.randint(3, 7))
        time.sleep(0.7)
        pywinauto.keyboard.send_keys(passwordn)
        password += passwordn
        passwordn = str(random.randint(400, 90907))
        time.sleep(0.5)
        pywinauto.keyboard.send_keys(passwordn)
        password += passwordn
        print(password)

        time.sleep(1.8)
        pywinauto.mouse.click(coords=(583, 250))

        # reg
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(583, 250))
        time.sleep(25)

        # save data
        time.sleep(0.9)
        pywinauto.mouse.click(coords=(480, 680))

        # get sms_code
        code = get_key(id)
        if code is None:
            pywinauto.mouse.click(coords=(480, 680))
            time.sleep(2)
            pywinauto.mouse.click(coords=(580, 400))
            delete_user_from_phone()
            time.sleep(5)
            app.kill()
            time.sleep(5)
            return False, None, None
        else:
            try:
                file2write = open(phone_number, 'w')
                file2write.write(phone_number + " " + password + " " + proxy)
                file2write.close()
            except Exception:
                pass
            print(code)
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(520, 200))
            time.sleep(0.5)
            pywinauto.keyboard.send_keys(str(code))
            time.sleep(0.5)
            pywinauto.mouse.click(coords=(520, 235))
            time.sleep(20)

            # log settings
            time.sleep(7)
            pywinauto.mouse.click(coords=(390, 480))
            time.sleep(3)
            pywinauto.mouse.click(coords=(695, 70))
            time.sleep(18)
            pywinauto.mouse.click(coords=(695, 70))
            time.sleep(15)
            pywinauto.mouse.click(coords=(490, 680))
            time.sleep(35)
            pywinauto.mouse.click(coords=(360, 70))
            time.sleep(1)
            pywinauto.mouse.click(coords=(670, 70))
            time.sleep(7.3)
            pywinauto.mouse.click(coords=(650, 680))
            time.sleep(9.4)
            pywinauto.mouse.click(coords=(647, 682))
            time.sleep(3)
            pywinauto.mouse.click(coords=(447, 642))
            time.sleep(4)
            pywinauto.mouse.click(coords=(460, 430))
            time.sleep(5)
            pywinauto.mouse.click(coords=(580, 680))
            time.sleep(4.4)
            pywinauto.mouse.click(coords=(450, 630))
            time.sleep(4)
            pywinauto.mouse.click(coords=(221, 123))
            time.sleep(2)
            pywinauto.mouse.click(coords=(544, 468))
            time.sleep(2)
            pywinauto.mouse.click(coords=(544, 670))
            time.sleep(30)
            pywinauto.mouse.click(coords=(544, 675))
            time.sleep(4)
            pywinauto.mouse.click(coords=(544, 390))
            time.sleep(3)
            pywinauto.mouse.click(coords=(544, 110))
            time.sleep(1.5)
            pywinauto.keyboard.send_keys("Москва")
            pywinauto.mouse.click(coords=(444, 139))
            time.sleep(1.5)
            pywinauto.mouse.click(coords=(444, 139))
            time.sleep(4.5)
            pywinauto.mouse.click(coords=(449, 680))
            time.sleep(4.5)
            pywinauto.mouse.click(coords=(449, 680))
            time.sleep(5.5)
            pywinauto.mouse.click(coords=(449, 680))
            time.sleep(6.8)
            # pywinauto.mouse.click(coords=(449, 680))
            # time.sleep(4.8)
            # pywinauto.mouse.click(coords=(449, 480))
            # time.sleep(2.8)
            pywinauto.mouse.click(coords=(449, 680))
            # pywinauto.mouse.click(coords=(449, 680))
            time.sleep(8.3)
            pywinauto.mouse.click(coords=(649, 680))
            time.sleep(5.3)
            pywinauto.mouse.click(coords=(449, 480))
            time.sleep(2.8)
            pywinauto.mouse.click(coords=(649, 680))
            # pywinauto.mouse.click(coords=(449, 680))
            time.sleep(10.5)
            pywinauto.mouse.click(coords=(649, 680))
            time.sleep(5.1)
            pywinauto.mouse.click(coords=(449, 680))
            time.sleep(5.1)
            pywinauto.mouse.click(coords=(449, 680))
            time.sleep(5.1)
            pywinauto.mouse.click(coords=(449, 680))
            time.sleep(4.1)
            pywinauto.mouse.click(coords=(430, 70))
            time.sleep(10)
            pywinauto.mouse.click(coords=(775, 68))
            time.sleep(3)
            pywinauto.mouse.press(coords=(650, 170))
            time.sleep(2)
            pywinauto.mouse.scroll(coords=(650, 170), wheel_dist=-1)
            time.sleep(1)
            pywinauto.mouse.release(coords=(650, 170))
            time.sleep(1)
            pywinauto.mouse.press(coords=(650, 170))
            time.sleep(1)
            pywinauto.mouse.scroll(coords=(650, 170), wheel_dist=-1)
            time.sleep(1)
            pywinauto.mouse.release(coords=(650, 170))
            pywinauto.mouse.click(coords=(450, 690))
            time.sleep(1)
            pywinauto.mouse.click(coords=(550, 350))
            print("ok")
            delete_user_from_phone()
            pywinauto.mouse.click(coords=(360, 70))
            app.kill()
        return True, phone_number, password
    except Exception:
        app.kill()
        return False, None, None


def delete_user_from_phone():
    time.sleep(5)
    pywinauto.mouse.click(coords=(700, 145))
    time.sleep(1)
    pywinauto.mouse.click(coords=(600, 240))
    time.sleep(1)
    pywinauto.mouse.click(coords=(600, 430))
    time.sleep(1)


def delete_nox_phone(clean=True):
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\MultiPlayerManager.exe")
    time.sleep(25)
    if clean:
        pywinauto.mouse.click(coords=(1030, 240))
        time.sleep(2)
        pywinauto.mouse.click(coords=(730, 460))
        time.sleep(300)
        pywinauto.mouse.click(coords=(835, 430))
        time.sleep(2)
    pywinauto.mouse.click(coords=(1055, 240))
    time.sleep(2)
    pywinauto.mouse.click(coords=(750, 420))
    time.sleep(2)
    app.kill()
    time.sleep(5)

    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")
    time.sleep(30)
    app.kill()
    time.sleep(10)
    app = application.Application().start("D:\\Program Files\\Nox\\bin\\Nox.exe")
    time.sleep(50)
    open_fb()
    time.sleep(10)
    app.kill()


if __name__ == '__main__':
    proxy = update_proxy()
    delete_nox_phone()
    mistake = 0
    while True:
        try:
            status, account_login, account_pass = start(proxy)
            if status:
                proxy_id = save_proxy(proxy)
                if proxy_id is not None:
                    account_id = save_account(account_login, account_pass, proxy_id)
                    if account_id is not None:
                        res_id = save_creditional(account_id, proxy_id)
                        print("res id " + str(res_id))
                proxy = update_proxy()
                mistake = 0
            else:
                mistake += 1
            if mistake >= 5:
                mistake = 0
                proxy = update_proxy()
            time.sleep(3)
            delete_nox_phone()
        except Exception:
            mistake += 1

