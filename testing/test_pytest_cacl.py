import pytest
import allure
from pythonDemo.calc import Calc


class TestCalc:
    @pytest.fixture()
    @allure.step('实例化Calc')
    def setup(self):
        self.calc = Calc()

    @allure.story('加法测试')
    @pytest.mark.parametrize('a, b, result', [(1, 2, 3), (-1, -2, -3), (0, 0, 0), (0.15, 0.01, 0.16)])
    def test_add_1(self, setup, a, b, result):
        sum = self.calc.add(a, b)
        print(result)
        assert sum == result

    @allure.story('除法测试')
    @pytest.mark.parametrize('a, b, result', [(1, 1, 1), (-2, -2, 1), (0.1, 0.2, 0.5), (0, 0, 0)])
    def test_div(self, setup, a, b, result):
        try:
            quotient = self.calc.div(a, b)
            print(quotient)
            assert quotient == result
        except ZeroDivisionError as e:
            print(e.message)


if __name__ == "__main__":
    pytest.main(['-vs', 'test_pytest_cacl.py::TestCalc'])
