import number

class TestPow:
    def test_pow_1_2(self):
        assert number.funk_add(2, 1) == 3
    def test_pow_10_20(self):
        assert number.funk_add(10, 20) == 30
class TestSub:
    def test_pow_2_3(self):
        assert number.funk_sub(2, 3) == -1
class TestMul:
    def test_pow_2_3(self):
        assert number.funk_mul(2, 3) == 6
class TestDel:
    def test_pow_2_0(self):
        assert number.funk_mul(2, 0) == 0