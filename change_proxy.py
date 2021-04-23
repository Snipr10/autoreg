# Trial
import json
import time

import pywinauto
import requests

is_create_new = False
def update_proxy():
    if is_create_new:
        return buy_new_proxy()
    else:
        return update_proxy_from_text()


def buy_new_proxy():
    print("a")

def update_proxy_from_text():
    try:
        with open("proxy.txt", 'r') as f:
            lines = f.readlines()
        with open("proxy.txt", 'w') as f:
            f.writelines(lines[1:])
        new_proxy = lines[0].strip()

        if new_proxy is None:
            raise Exception("Proxy")
        change_proxy(new_proxy)

        return new_proxy
    except Exception:
        return None


def change_proxy(proxy):
    app_proxier_trial = pywinauto.application.Application().start(
        "C:\\Program Files (x86)\\Proxifier\\Proxifier.exe"
    )
    try:
        time.sleep(3)
        w_handle = pywinauto.findwindows.find_windows(title=u'Proxifier Trial', class_name='#32770')[0]
        window = app_proxier_trial.window_(handle=w_handle)
        ctrl = window['Button']
        ctrl.ClickInput()
    except Exception:
        pass
    time.sleep(3)

    app_proxier = pywinauto.application.Application().start(
        "C:\\Program Files (x86)\\Proxifier\\Proxifier.exe"
    )

    time.sleep(3)
    pywinauto.mouse.click(coords=(801, 150))
    time.sleep(3)

    w_handle = pywinauto.findwindows.find_windows(title=u'Proxy Servers', class_name='#32770')[0]
    window_servers = app_proxier.window_(handle=w_handle)
    ctrl_server = window_servers['Button2']
    ctrl_server.Click()
    # time.sleep(2)
    # ctrl = window['Edit']
    # ctrl.Click()
    w_handle = pywinauto.findwindows.find_windows(title=u'Proxy Server', class_name='#32770')[0]
    window_server = app_proxier.window_(handle=w_handle)
    ctrl_server = window_server['Edit']
    ctrl_server.Click()
    time.sleep(1.2)
    ctrl_server.set_text(proxy.split(':')[0])
    ctrl_server = window_server['OK']
    ctrl_server.Click()
    time.sleep(1.2)

    ctrl_servers = window_servers['OK']
    ctrl_servers.Click()
    app_proxier.kill()


def get_expirationDate():
    import datetime
    (datetime.datetime.utcnow() + datetime.timedelta(days=5)).isoformat() + "Z"
    return "2021-04-25T08:26:32"


def save_proxy(proxy):
    try:
        split_proxy = proxy.split(":")
        res = requests.post(
            'http://194.50.24.4:7999/api/proxy/', json={
                "host": split_proxy[0],
                "port": int(split_proxy[1]),
                "login": split_proxy[2],
                "password": split_proxy[3],
                "expirationDate": get_expirationDate(),
                "available": False
            })
        return json.loads(res.text)['id']
    except Exception as e:
        try:
            with open("proxy_new.txt", "a") as f:
                f.write("\n" + str(proxy))
        except Exception as e:
            pass
        return None
