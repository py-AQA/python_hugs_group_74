class Test:
    n = 1

    def assert_equals(self, ar, er, msg=''):
        print(f"Test {self.n}: {msg}", 'OK' if ar == er else 'FAILED')
        self.n += 1


test = Test()