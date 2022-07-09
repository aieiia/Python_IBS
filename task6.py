# Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
# Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:
  def voice(self): pass

# Класс наследник 1
class Cat(Animal):
  # Своя реализация метода voice()
  def voice(self): return "meow"

# Экземпляр наследника 1
Vasya_the_cat = Cat()
# Вызов переопределенного метода voice()
print(Vasya_the_cat.voice())

# Класс наследник 2
class Pig(Animal):
  # Своя реализация метода voice()
  def voice(self): return "oink"

# Экземпляр наследника 2
Xrusha_the_pig = Pig()
# Вызов переопределенного метода voice()
print(Xrusha_the_pig.voice())

# Класс наследник 3
class Cow(Animal):
  # Своя реализация метода voice()
  def voice(self): return "moo"

# Экземпляр наследника 3
Masha_the_cow = Cow()
# Вызов переопределенного метода voice()
print(Masha_the_cow.voice())