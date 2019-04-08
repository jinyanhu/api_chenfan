__author__ = 'Administrator'

"""
存货调价单
"""
import json
from utils.http_util import Http
from utils.database_util import Database
from api_call.chenfan.base import BaseHttp
from api_call.chenfan.login.api_login import ApiLogin


class ApiPriceJust(BaseHttp):
    def __init__(self):
        """
        存货调价单创建接口
        """
        BaseHttp.__init__(self)                 # 父类初始化
        self.database = Database("pymysql")
        self.api_login = ApiLogin()
        self.api_login.set_admin_login_header(self.header)  # 加登录header
        self.http = Http(self.header)  # http对象

    # ####################### 以下的每个方法，对应封装一个接口的调用过程 ################### #

    def post_add_price(self, body_data=None):
        """
        新增供应商
        """
        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/priceJust/add"
        response = self.http.post(url=url, body=body_data, headers=self.header)       # post方法

        # 返回响应数据
        return response

    def get_price_just_code(self, body_data=None):
        """
        获取存货调价单号
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/numberGenerator/getNumber/QTJ"
        response = self.http.get(url, params=body_data)  # get方法
        # 返回响应数据,把返回的数据做json处理
        json_str = response.json()
        json_left = dict(json_str)
        # 获取到json中obj(调价单号)的值
        price_code = json_left['obj']
        print(price_code)
        return price_code

    def get_list(self, body_data=None):
        """
        获取供应商列表
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/getList"
        response = self.http.get(url, params=body_data)  # get方法
        # 返回响应数据

        return response

    def get_list_export(self, body_data=None):
        """
        导出供应商列表
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/export"
        response = self.http.get(url, params=body_data)  # get方法

        # 返回响应数据
        return response

    def put(self, body_data=None):
        """
        获取供应商禁用启用状态
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/switchBanVendor"
        response = self.http.put(url, body=body_data, headers=self.header)  # put方法

        # 返回响应数据
        return response

    def get_vendor_details(self, body_data=None):
        """
        获取供应商详情
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/getInfo"
        response = self.http.get(url, params=body_data)  # get方法

        # 返回响应数据
        return response

    def delete_vendor(self, sql):
        """
        :param sql: sql语句
        :return:
        """
        self.database.update(sql=sql)

    def put_update_vendor(self, body_data=None):
        """
        获取供应商禁用启用状态
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/update"
        response = self.http.put(url, body=body_data, headers=self.header)  # put方法

        # 返回响应数据
        return response


if __name__ == "__main__":
    # 该区域的代码只在run当前文件时执行
    # 可以在此简单测试下封装的接口调用方法
    pass


