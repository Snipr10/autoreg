import json
import requests


def save_account(account_login, account_pass, proxy):
    try:
        res = requests.post(
            "http://194.50.24.4:7999/api/account/", json={
                "login": account_login,
                "password": account_pass,
                "available": False,
                "banned": True

            })
        return json.loads(res.text)["id"]
    except Exception as e:
        try:
            with open("account_new.txt", "a") as f:
                f.write("\n" + account_login + " " + account_pass)
        except Exception as e:
            pass
        try:
            with open("proxy_new.txt", "a") as f:
                f.write("\n" + " id: " + str(proxy))
        except Exception as e:
            pass
        return None


def save_creditional(account, proxy):
    try:
        res = requests.post(
            "http://194.50.24.4:7999/api/worker/", json={
                "account": account,
                "proxy": proxy
            })
        return json.loads(res.text)["id"]
    except Exception as e:
        try:
            with open("account_new.txt", "a") as f:
                f.write("\n" + " id: " + str(account))
        except Exception as e:
            pass
        try:
            with open("proxy_new.txt", "a") as f:
                f.write("\n" + " id: " + str(proxy))
        except Exception as e:
            pass
        pass
