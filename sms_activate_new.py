import httpx
from onlinesimru import GetNumbers

api_key = "71cc492d41aea50bc9d3578e15d8a6b3"
numbers = GetNumbers(api_key)


def get_number(attempt=0):
    try:
        response = httpx.post("http://onlinesim.ru/api/getNum.php",
                              params={
                                  "apikey": api_key,
                                  "service": 3223,
                                  "number": True,
                                  "country": 7,
                                  "extension": False
                              }).json()
        id = response["tzid"]
        phone = response["number"]
    except Exception as e:
        print(e)
        id = None
        phone = None

    return phone, id


def get_key(id, attempt=0):
    if attempt >= 20:
        return None
    code = None
    try:
        code = numbers.wait_code(id, timeout=1)
    except Exception as e:
        print(e)
        attempt = attempt + 1
        return get_key(id, attempt)
    completed_phone(id)
    return code


def completed_phone(id):
    try:
        numbers.close(id)
    except Exception:
        pass
