import requests

class web_request:
    def __init__(self):
        # self.headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Accept-Language': 'ru-RU',
        #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        #     'Referer': 'https://google.com/?q=центр+банк'
        # }
        self.url = 'https://www.cbr.ru/currency_base/daily/'

    def get(self):
        self.r = requests.get(self.url)
        if self.get_status_code == 200:
            return True
        else:
            return False

    def html_text(self):
        return self.r.text

    def get_status_code(self):
        return int(self.r.status_code)