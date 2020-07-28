from selenium.webdriver.common.by import By
from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        # 在首页点击添加成员
        # click add member
        # self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()

        # 通过通讯录添加成员
        self.find(By.ID, 'menu_contacts').click()

        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, "#username"))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements_len > 0
        self.wait_for_click(wait_add_member)
        # sleep(5)
        return AddMember(self._driver)

    def goto_tongxunlu(self):
        """
        通过通讯录添加成员
        :return:
        """
        self.find(By.ID, 'menu_contacts').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        self.wait_for_click(locator)
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # sleep(2)
        # self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        # sleep(5)
        return AddMember(self._driver)
