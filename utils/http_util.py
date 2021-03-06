import requests
import json

__author__ = "zzh"


class Http(object):
    """
    对HTTP和HTTPS请求进行封装，方便调用
    HTTP响应：res属性值，直接使用res.text访问：
                cookies: cookies json
                content: "二进制字节"
                encoding: "响应值的编码"
                headers": 响应头 json
                reason: 响应状态 OK
                status_code: 响应状态码 200
                text: 字符串响应值

    """
    def __init__(self, headers=None):
        if not headers:
            self.headers = {
                "Content-Type": "application/json"
            }
        else:
            self.headers = headers
        pass

    def convert_to_json(self, s):
        """
        将输入值转换成json
        :param s:
        :return:
        """
        if type(s) != dict:
            try:
                s = json.loads(s)
            except Exception as e:
                print(e)
        return s

    def form_urlencode(self, body_json):
        """
        根据请求头格式form-data或x-www-form-urlencoded，先进行所有键值对的值转换，把所有非字符串类型转换成字符串
        :param body_json: json格式的body
        :return:
        """
        body = None
        if body_json and type(body_json) == dict:
            new_body = dict()
            for item in body_json:
                if type(body_json[item]) != str:
                    new_body[item] = json.dumps(body_json[item])
                else:
                    new_body[item] = body_json[item]
            body = new_body
        return body

    def request(self, method, url, headers=None, body=None, params=None):
        """
        传入方法的请求
        :param method:
        :param url:
        :param headers:
        :param body:
        :param json:
        :param params:
        :return:response 属性：ok=True；reason="Moved Temporarily";status_code=302;text=""
        """
        if headers:
            self.headers = headers
        self.headers = self.convert_to_json(self.headers)
        if params:
            params = self.convert_to_json(params)
        if body:
            body = self.convert_to_json(body)
        else:
            body = None
        res = None
        if self.headers.__contains__("content-type") and self.headers["content-type"] == "application/x-www-form-urlencoded":
            body = self.form_urlencode(body)
            res = requests.request(method=method, url=url, headers=self.headers, data=body, params=params)
        elif self.headers.__contains__("Content-Type") and self.headers["Content-Type"] == "application/x-www-form-urlencoded":
            body = self.form_urlencode(body)
            res = requests.request(method=method, url=url, headers=self.headers, data=body, params=params)
        elif self.headers.__contains__("Content-Type") and self.headers["Content-Type"] == "application/json":
            res = requests.request(method=method, url=url, headers=self.headers,     json=body, params=params)
        elif self.headers.__contains__("content-type") and self.headers["content-type"] == "application/json":
            res = requests.request(method=method, url=url, headers=self.headers, json=body, params=params)
        return res

    def get(self, url, headers=None, params=None):
        """
        get请求
        :param url: url
        :param headers: 请求头，json类型
        :param params: url参数, json类型
        :return:
        """
        if headers:
            self.headers = headers
        self.headers = self.convert_to_json(self.headers)
        if params:
            params = self.convert_to_json(params)
        res = requests.request(method="GET", url=url, headers=self.headers, params=params)
        return res

    def post(self, url, headers=None, body=None, params=None):
        """
        post请求
        :param url: url
        :param headers: 请求头，json类型
        :param body: 请求体,json格式字符串
        :return:
        """
        if headers:
            self.headers = headers
        self.headers = self.convert_to_json(self.headers)
        if params:
            params = self.convert_to_json(params)

        if body:
            body = self.convert_to_json(body)
        else:
            body = None
        res = None
        if self.headers.__contains__("content-type") and self.headers["content-type"] == "application/x-www-form-urlencoded":
            body = self.form_urlencode(body)
            res = requests.request(method="POST", url=url, headers=self.headers, data=body, params=params)
        elif self.headers.__contains__("Content-Type") and self.headers["Content-Type"] == "application/x-www-form-urlencoded":
            body = self.form_urlencode(body)
            res = requests.request(method="POST", url=url, headers=self.headers, data=body, params=params)
        elif self.headers.__contains__("Content-Type") and self.headers["Content-Type"] == "application/json":
            res = requests.request(method="POST", url=url, headers=self.headers, json=body, params=params)
        elif self.headers.__contains__("content-type") and self.headers["content-type"] == "application/json":
            res = requests.request(method="POST", url=url, headers=self.headers, json=body, params=params)
        return res

    def put(self, url, headers=None, body=None, params=None):
        """
        put请求
        :param url: url
        :param headers: 请求头，json类型
        :param body: 请求体,json格式字符串
        :return:
        """
        if headers:
            self.headers = headers
        self.headers = self.convert_to_json(self.headers)
        if params:
            params = self.convert_to_json(params)
        if body:
            body = self.convert_to_json(body)
        else:
            body = None
        res = None
        if self.headers.__contains__("content-type") and self.headers["content-type"] == "application/x-www-form-urlencoded":
            body = self.form_urlencode(body)
            res = requests.request(method="PUT", url=url, headers=self.headers, data=body, params=params)
        elif self.headers.__contains__("Content-Type") and self.headers["Content-Type"] == "application/x-www-form-urlencoded":
            body = self.form_urlencode(body)
            res = requests.request(method="PUT", url=url, headers=self.headers, data=body, params=params)
        elif self.headers.__contains__("Content-Type") and self.headers["Content-Type"] == "application/json":
            res = requests.request(method="PUT", url=url, headers=self.headers, json=body, params=params)
        elif self.headers.__contains__("content-type") and self.headers["content-type"] == "application/json":
            res = requests.request(method="PUT", url=url, headers=self.headers, json=body, params=params)
        return res

    def patch(self, url, headers=None, body=None, params=None):
        """
        patch请求
        :param url: url
        :param headers: 请求头，json类型
        :param body: 请求体,json格式字符串
        :return:
        """
        if headers:
            self.headers = headers
        self.headers = self.convert_to_json(self.headers)
        if params:
            params = self.convert_to_json(params)
        body = self.convert_to_json(body)
        res = requests.request(method="PATCH", url=url, headers=self.headers, data=body, params=params)
        return res

    def delete(self, url, headers=None, params=None):
        """
        delete请求
        :param url: url
        :param headers: 请求头，json类型
        :param body: 请求体,json格式字符串
        :return:
        """
        if headers:
            self.headers = headers
        self.headers = self.convert_to_json(self.headers)
        res = requests.request(method="DELETE", url=url, headers=self.headers, data=body, params=params)
        return res


if __name__ == '__main__':
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "8632E046C3E751A9C3A35849AD2A57E5ED76125A22752619B7068ECADE6A8A0B6AE0F1295B6235C550067AB29E630F25",
        "Cookie": "SESSION=YmFkZTBhNTQtY2Q3Yy00ZDMzLWI2MWQtZmRmYzhkOTZhNzRj; token=8632E046C3E751A9C3A35849AD2A57E5ED76125A22752619B7068ECADE6A8A0B6AE0F1295B6235C550067AB29E630F25",
        "dataType": "qy",
        "user_agent": "pc",
        "user_ip": "101.69.247.106"
    }
    #body = {'brandCode': '00011', 'receiveName': '收货人', 'lowestReOrderPeriodScore': 33, 'lowestPostSaleDefectiveScore': 33, 'createName': '张晓方', 'lowestVendorLevel': 'A', 'state': 1, 'lowestPreSaleDefectiveScore': 22, 'prefixEn': 'JK', 'createBy': '325', 'receiveTel': '11122334455', 'lowestPerformanceScore': 22, 'brandType': '1', 'brandName': '接口自动化品牌', 'receiveAddress': '地址', 'magnification': '1.1', 'customerName': '杭州宸帆电子商务有限责任公司', 'lowestOnTimeReachScore': 11, 'customerId': 19}
    body = {'lowestVendorLevel': 'A', 'lowestReOrderPeriodScore': 33, 'lowestPreSaleDefectiveScore': 22, 'lowestPostSaleDefectiveScore': 33, 'lowestPerformanceScore': 22, 'lowestOnTimeReachScore': 11, 'state': 1, 'receiveTel': '11122334455', 'receiveName': '收货人', 'receiveAddress': '地址', 'prefixEn': 'JKZA', 'magnification': '1.1', 'customerName': '杭州宸帆电子商务有限责任公司', 'customerId': 19, 'brandType': '1', 'brandName': '接口自动化品牌2', 'brandCode': '00013'}
    print(type(body))
    http = Http()
    res = http.post(url="http://10.228.88.254:8080/brand/add", headers=headers, body=body)
    pass
