class Reverse:

    def __init__(self, data):
        self.data = data

    def display(self):
        print (self.data[::-1])

y = Reverse("how r u")
y.display()
