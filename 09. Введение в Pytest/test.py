class TestExample:
    def test_pass(self):
        a = 4
        b = 3
        assert a + b == 7

    def test_fail(self):
        a = 4
        b = 10
        expected_sum = 0
        assert a + b == expected_sum, f'Sum of vars {a} and {b} not equal to {expected_sum}'
