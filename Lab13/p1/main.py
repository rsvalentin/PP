class A:
    pass

def custom_extension(self):
     print("whatever")

class str(str):
    def pascalCode(self):
        parts = self.split(" ")
        res= ""
        for part in parts:
            res += part.capitalize()
        return res



if __name__ == '__main__':
    A.whatever = custom_extension
    a_instance = A()
    a_instance.whatever() # afiseaza whatever
    print(str("sirul meu de caractere").pascalCode())