import json
import requests


class AbstractTest:

    def __init__(self, prefix, authorization, url='', headers=''):
        self.url = url + prefix
        headers.update(authorization)
        self.headers = headers

    def __curl__(self, route, data, method):
        curl_h = (((str(self.headers).replace('{', '')).replace('}', '')).replace(',', ' \\\n--header ')).replace("': '",': ')
        curl_d = (((str(data).replace("'", '"')).replace(',', ',\n   ')).replace('{', '{\n    ')).replace('}', '\n}')
        return "curl --location --request " + method + " '" + self.url + route + "' \\\n--header " + curl_h + " \\\n--data-raw '" + curl_d + "'"

    def get(self, route='', params=''):
        res = requests.get(
            url=self.url + route,
            params=params,
            headers=self.headers,
        )
        try:
            text = json.loads(res.text) if res.text else ''
        except Exception:
            text = res.text
        return {
            "status": res.status_code,
            "message": res.reason,
            "text": text,
            "route": self.__curl__(route, params, 'GET'),
        }

    def post(self, route='', data='', files=None):
        res = requests.post(
            url=self.url + route,
            json=data,
            headers=self.headers,
            files=files,
        )
        try:
            text = json.loads(res.text) if res.text else ''
        except Exception:
            text = res.text
        return {
            "status": res.status_code,
            "message": res.reason,
            "text": text,
            "route": self.__curl__(route, data, 'POST'),
        }

    def put(self, route='', data=''):
        res = requests.put(
            url=self.url + route,
            json=data,
            headers=self.headers
        )
        try:
            text = json.loads(res.text) if res.text else ''
        except Exception:
            text = res.text
        return {
            "status": res.status_code,
            "message": res.reason,
            "text": text,
            "route": self.__curl__(route, data, 'PUT')
        }

    def delete(self, route=''):
        curl_h = (((str(self.headers).replace('{', '')).replace('}', '')).replace(',', ' \\\n--header ')).replace("': '", ': ')
        res = requests.delete(url=self.url + route, headers=self.headers)
        try:
            text = json.loads(res.text) if res.text else ''
        except Exception:
            text = res.text
        return {
            "status": res.status_code,
            "message": res.reason,
            "text": text,
            "route": self.__curl__(route, '', 'DELETE'),
        }
