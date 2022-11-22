class Test:
    def __init__(self, print):
        self.print = print

    def print_something(self):
        print(self.print)

if __name__ == '__main__':
    hello_world = "Hello World!"
    test = Test(hello_world)
    test.print_something()