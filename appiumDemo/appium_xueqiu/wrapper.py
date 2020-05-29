from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']")
        ]
        _max_num = 3
        _error_num = 0
        from appiumDemo.appium_xueqiu.base_page import BasePage
        instance: BasePage = args[0]

        try:
            element = func(*args, **kwargs)
            _error_num = 0
            # 隐式等待恢复原来的等待
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 出现异常，将隐式等待设置小一点，快速的处理弹窗
            instance._driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹窗
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹窗，再去查找目标元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
