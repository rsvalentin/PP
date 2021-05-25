class A:
    pass


def custom_extension(self):
    print("whatever")


class int(int):
    def is_even(self):
        return self % 2 == 0


if __name__ == '__main__':
    # se pot crea extensii DOAR pe clase custom
    A.whatever = custom_extension
    a_instance = A()
    a_instance.whatever()

    print(int(6).is_even())
    print(int(5).is_even())