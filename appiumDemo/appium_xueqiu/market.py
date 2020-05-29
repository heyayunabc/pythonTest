from appiumDemo.appium_xueqiu.base_page import BasePage
from appiumDemo.appium_xueqiu.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)
