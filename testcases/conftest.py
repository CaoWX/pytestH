# coding:utf-8
# Author:窝里横
import pytest

from base.api_client import Api_Client


@pytest.fixture(scope="session")
def api_demo_client():
    init_client = Api_Client()
    test_path = 'login.do'
