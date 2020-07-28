import yaml
from selenium.webdriver.common.by import By

from appiumDemo.appium_xueqiu.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self._params["name"] = name
        self.steps("../appium_xueqiu/search.yaml")
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        # self.find(By.XPATH, "//*[@text='BABA']").click()
        # self.find(By.XPATH,
        #           f"//*[contains(@resource-id, 'll_stock_item_container')]//*[@text='{name}']/../..//*[@text='加自选']").click()

        # with open("../appium_xueqiu/search1.yaml", encoding="utf-8") as f:
        #     steps = yaml.safe_load(f)
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
        #             element.send_keys(step["value"])

    def add(self, name):
        self._params["name"] = name
        self.steps("../appium_xueqiu/search.yaml")

    def is_choose(self, name):
        # eles = self.finds(By.XPATH,
        #                   f"//*[contains(@resource-id, 'll_stock_item_container')]//*[@text='{name}']/../..//*[@text='已添加']")
        # return len(eles) > 0
        self._params["name"] = name
        self.steps("../appium_xueqiu/search.yaml")

    def reset(self, name):
        self._params["name"] = name
        self.steps("../appium_xueqiu/search.yaml")
