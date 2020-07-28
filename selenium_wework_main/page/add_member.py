from selenium.webdriver.common.by import By
from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.find(By.ID, 'username').send_keys("ddd")
        self.find(By.ID, 'memberAdd_acctid').send_keys("ddd")
        self.find(By.ID, 'memberAdd_phone').send_keys("13321111114")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def update_page(self):
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        # 切割1/10
        return [int(x) for x in content.split('/', 1)]

    def get_member(self, value):
        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        # elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(1)')

        cur_page, total_page = self.update_page()
        # list = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if value == element.get_attribute("title"):
                    return True
            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, '.js_next_page').click()
