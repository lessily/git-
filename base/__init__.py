"""应用的包名和启动名"""
#这里的desired_caps['appPackage'] = apppackage  # 应用的包名;desired_caps['appActivity'] = appactivity  # 代表启动的activity
#短信的启动名和包名
#  appPackage='com.android.mms'
# appActivity='.ui.ConversationList'
#设置的启动名和包名
appPackage='com.android.settings'
appActivity='.Settings'


#短信新增
# from selenium.webdriver.common.by import By
# sms_add=By.ID,"com.android.mms:id/action_compose_new"  #新建信息
# sms_input_phone_number=By.ID,"com.android.mms:id/recipients_editor"  #定位到电话输入框
# sms_input_content=By.ID,"com.android.mms:id/embedded_text_editor"   #定位到信息输入框
# sms_send_button=By.ID,"com.android.mms:id/send_button_sms" #点击发送按钮

#设置搜索框
from selenium.webdriver.common.by import By
setting_search=By.ID,'com.android.settings:id/search'
setting_input_content=By.ID,'android:id/search_src_text'
setting_back=By.CLASS_NAME,'android.widget.ImageButton'
# import yaml
# data={ 'value1': 1, 'value2': 2, 'value3': 3}
# with open ('./test.yaml', 'w',encoding='utf-8')as f:
#     yaml.dump(data,f)
