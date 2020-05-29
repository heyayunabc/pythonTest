from selenium.webdriver.common.by import By
from appiumDemo.appium_xueqiu.base_page import BasePage
from appiumDemo.appium_xueqiu.market import Market


class Main(BasePage):
    def goto_market(self):
        # click
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return Market(self._driver)
