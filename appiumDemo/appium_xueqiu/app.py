from appium import webdriver
from appiumDemo.appium_xueqiu.base_page import BasePage
from appiumDemo.appium_xueqiu.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = True
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
