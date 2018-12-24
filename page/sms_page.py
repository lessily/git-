import sys, os, base

import pytest

sys.path.append(os.getcwd())
from base.base_action import BaseAction

class SmsPage(BaseAction):  #继承父类
    def __init__(self,driver):   #这个方法自动调用BaseAction中的元素
        BaseAction.__init__(self,driver)
    #点击搜索按钮
    def click_searchID(self):
        self.click_element(base.setting_search)
    #向搜索输入框输入内容
    @pytest.mark.parametrize("a", [3, 6])
    def input_content_number(self):
        self.input_content(base.setting_input_content)
        # input_list=[1,2,3]
        # input_content=self.find_element(base.setting_input_content)
        # for i in input_list:
        #     input_content.clear()
        #     input_content.send_keys(i)
    def click_back(self):
        self.click_element(base.setting_back)

    #发送短信
    # def click_add_sms(self):   #点击新增按钮
    #     # self.click_element(base.sms_add)
    # def input_phone_content(self):   #在电话输入框输入号码'10086'
        # self.input_content(base.sms_input_phone_number,'10086')
    #模拟三条信息,键入信息输入框,并点击发送按钮
    # def send_sms(self):
    #     send_list=[111,'aaa','bbbb']
    #     input_content=self.find_element(base.sms_input_content)
    #     send_button=self.find_element(base.sms_send_button)
    #     for i in send_list:
    #         input_content.clear()
    #         input_content.send_keys(i)
    #         send_button.click()



