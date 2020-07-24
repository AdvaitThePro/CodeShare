class BigSur():
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(self.name)
BigSur = BigSur("macOS")
BigSur.name = "macOS"
BigSur.say_hello()