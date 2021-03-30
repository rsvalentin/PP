class Macaitoare:
    def quack(self):
        pass

class Duck(Macaitoare):
    def quack(self):
        print("Duck: Quack quack")
    def __repr__(self):
        return "Duck"

class Goose(Macaitoare):
    def quack(self):
        print("Goose: Quack quack")
    def __repr__(self):
        return "Goose"

if __name__ == '__main__':
    duck: Macaitoare = Duck()
    goose: Macaitoare = Goose()
    for macmac in [duck, goose]:
        macmac.quack()
        print(macmac)