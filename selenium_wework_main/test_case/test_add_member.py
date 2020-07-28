from time import sleep

from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    # 测试通过首页点击"添加成员"按钮添加成员
    def test_add_member(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        sleep(2)
        assert "abcddddd" in add_member.add_member()
        # return True

    # 测试通过通讯录添加成员
    def test_add_member_by_tongxunlu(self):
        add_member = self.main.goto_tongxunlu()
        add_member.add_member()
        assert "abcddddd" in add_member.add_member()
