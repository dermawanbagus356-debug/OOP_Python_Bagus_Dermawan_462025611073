class A:
    def __init__(self):
        print("Constructor Class A")

    def show(self):
        print("Method dari Class A")


class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor Class B")

    def show_b(self):
        print("Method dari Class B")


class C(A):
    def __init__(self):
        super().__init__()
        print("Constructor Class C")

    def show_c(self):
        print("Method dari Class C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("Constructor Class D")

    def show_d(self):
        print("Method dari Class D")


obj = D()

print("\nMenjalankan Method:")
obj.show()
obj.show_b()
obj.show_c()
obj.show_d()
