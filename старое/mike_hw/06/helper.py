class Test:
    n = 1

    def assert_equals(self, ar, er, msg=''):
        print(f"Test {self.n}: {msg}", 'OK' if ar == er else 'FAILED')
        self.n += 1

    def expect(self, bool_expression, msg=''):
        print(f"Test {self.n}: {msg}", 'OK' if bool_expression else 'FAILED')
        self.n += 1

    # def it(self, s):
    #     def dec(function):
    #         def wr(*args):
    #             self.m = s
    #             function(*args)
    #             pass
    #         return wr
    #     return dec
    #
    # def run(self, dct):
    #     [dct[k]() for k, v in dct.items() if "test_" in k]


test = Test()
