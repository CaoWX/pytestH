# coding:utf-8
# Author:窝里横
import allure
import pytest

from api.pack_api import PackApi
from base.api_client import Api_Client
from common.httpClient.doRequest import DoRequest
from common.readfile import ReadFileData, apidata


@allure.severity(allure.severity_level.NORMAL)
@allure.epic('针对单接口的测试')
@allure.feature('登录功能')
class TestUserLogin(object):

    def setup_class(self):
        self.init_client = Api_Client()
        self.test_path = 'login.do'

    @allure.story('登录-成功登录')
    @allure.description('单接口-该接口使用tom 的数据进行登录')
    @allure.title('测试数据:username = tome, password = 111111')
    @pytest.mark.parametrize('name,password,,status,msg', apidata['test_login_data'])
    def test_login(self,name,password,status,msg):
        httpresponse = PackApi().user_login_api_pack(name,password)
        # assert httpresponse.status_code == status
        assert msg in httpresponse.body
        # data = {
        #     'username': 'tom',
        #     'password': 111111
        # }
        # HttpResponse = self.init_client.doResquest.post_with_form(self.test_path,params=data)
        # print(HttpResponse.body)
        # assert '登录成功' in HttpResponse.body




