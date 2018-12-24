

class BaseAction: #类初始化的时候init就执行
    def __init__(self,driver):
        self.driver=driver

        #把要用的的函数定义出来
    def click_element(self,loction):   #点击
        self.find_element(loction).click()
    def input_content(self,loction,content): #输入
        self.find_element(loction).clear()
        self.find_element(loction).send_keys(content)


    def find_element(self,loction):   #loc代表一个元组,要把这个元组传进来,然后返回要被调用的元素
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loction[0],loction[1])
