class Foo:
    def __init__(self):
        self.total = 0

    def add_to_total(self, n):
        self.total = self.total + n
        return self
    
    def get_total(self):
        return self.total

def main():
    foo = Foo()
    print(foo.add_to_total(3).add_to_total(2).get_total())

if __name__ == "__main__":
    main()
