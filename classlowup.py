class String:

    def __init__(self, data):
        self.data = data

    def String(self):
      for i in self.data:
          j = ord(i)
          if j >= 65 and j <= 90:
              i = chr(j+32)
              self.data=self.data+i
              return 'String()' % (self.data)
    #x.display()

    def upper(self):
      for i in self.data:
          j = ord(i)
          if j >= 97 and j <= 122:
              i = chr(j-32)
              self.data=self.data+i
    #x.display()

    def display(self):
        print (self.data)

x = String("how r u")
x.display()
