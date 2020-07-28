import yaml
from selenium.webdriver.common.by import By
from appiumDemo.appium_xueqiu.base_page import BasePage
from appiumDemo.appium_xueqiu.market import Market


class Main(BasePage):
    def goto_market(self):
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # with open("../appium_xueqiu/main.yaml", encoding="utf-8") as f:
        #    steps = yaml.safe_load(f)
        # print(steps)
        # for step in steps:
        #     element = None
        #     if "by" in step.keys():
        #         element = self.find(step["by"], step["locator"])
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if "click" == action:
        #             element.click()
        #         if "send" == action:
        #             value = step["value"]
        #             print(f"send({value})")
        self.set_implicitly(10)
        self.steps("../appium_xueqiu/main.yaml")
        self.set_implicitly(3)
        return Market(self._driver)
