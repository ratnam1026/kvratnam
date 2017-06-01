class Employee:
  name = ""
  position = ""
  salary = 0.0

  def __init__ (self, name = "Empty", position ="None", salary = "0.0"):
    self.name = name
    self.position = position
    self.salary = salary

  def display(self):
    print (self.name)
    print (self.position)
    print (self.salary)

y = Employee("Jack", "CEO", 5000)
y.display()
