import pytest
from APItest.common.ReadExcelData import Readexceldata
from APItest.request_method.requesttest import RequestMethod






class TestInteerface:
    da = Readexceldata().paramsexpectdata()
    def setup_class(self):
        self.res = RequestMethod()

    @pytest.mark.parametrize("row,expect", da)
    def test_01(self, row, expect):
        print(expect)
        if expect:
            actual = self.res.get_regular_actual(row)
            print(actual)
            assert expect == actual
        else:
            self.res.get_response(row)