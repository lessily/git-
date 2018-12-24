
import sys,os, base
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.sms_page import SmsPage



class TestSms():
    def setup(self):
        # 这里的driver是调用base_driver中的init_driver.在__init__.py中,给appPackage包名,appActivity启动名赋值.调用base是因为init为初始化,首先调用init中的内容
        self.driver=init_driver(base.appPackage,base.appActivity)
        self.sms_page=SmsPage(self.driver)     #调用sms_page中SmsPage的类
    def teardown(self):

        self.driver.close_app()
    def test_sms(self):
        # self.sms_page.click_add_sms()
        # self.sms_page.input_phone_content()
        # self.sms_page.send_sms()
        self.sms_page.click_searchID()
        self.sms_page.input_content_number()
