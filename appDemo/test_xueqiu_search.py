# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

"""
step1: 改造pytest模式
step2: 改造成可维护的代码形态，不允许有绝对路径的出现
step3: 将自动生成的find_element_by_**改造成find_element(MobileBy.*)
step4: 添加断言
step5: 合理使用setup_class, setup方法
"""


class TestXueQiu:
    def setup_class(self):
        caps = {}
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps['noReset'] = "true"
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print("teardown_class")
        self.driver.quit()

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize("keyword, searchResult", [
        ("alibaba", "阿里巴巴"),
        ("jd", "京东"),
        ('xiaomi', "小米集团-W")
    ])
    def test_search(self, keyword, searchResult):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(keyword)
        sleep(2)
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{searchResult}']").click()
        el4 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{searchResult}']/../..//*[@text='加自选']")
        if len(el4) > 0:
            el4[0].click()
            self.driver.find_element(MobileBy.XPATH, f"//*[@text='{searchResult}']/../..//*[@text='已添加']")
        else:
            print("已加自选")
        result = self.driver.find_element(By.ID, "followed_btn").text
        print(result)
        assert result == '已添加'
