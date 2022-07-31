class Pokemon:
  """This is the docstring for the pokemon class"""
  def __init__(self, breed, hitPoints, attack, defense, speed, special, types, moves, name = None):
    if name is not None:
      self._name = name
    else:
      self._name = breed
    self._breed = breed
    self._maxHitPoints = hitPoints
    self._curHitPoints = hitPoints
    self._attack = attack
    self._defense = defense
    self._speed = speed
    self._special = special
    self._types = types
    self._moves = moves
    self._status = []
  
  def __repr__(self):
    return f"{self._name.capitalize() if self._name == self._breed else self._name}{' (a ' + self._breed.capitalize() + ')' if self._name != self._breed else ''} currently has {self._curHitPoints} HP."
  
  def get_types(self):
    return self._types
  
  def get_breed(self):
    return self._breed
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    self._name = new_name
  
  @property
  def hitPoints(self):
    return self._curHitPoints
  
  @hitPoints.setter
  def hitPoints(self, delta):
    self._curHitPoints += delta
    
  @property
  def attack(self):
    return self._attack
  
  @attack.setter
  def attack(self, num):
    if num > 0:
      self._attack += num
  
  @property
  def defense(self):
    return self._defense
  
  @defense.setter
  def defense(self, num):
    if num > 0:
      self._defense += num
      
  @property
  def speed(self):
    return self._speed
  
  @speed.setter
  def speed(self, num):
    if num > 0:
      self._speed += num
      
  @property
  def special(self):
    return self._attack
  
  @special.setter
  def special(self, num):
    if num > 0:
      self._special += num

charmander = Pokemon('charmander', 39, 52, 43, 65, 50, ["fire", None], ["Scratch", "Growl"])

print(charmander.name)
print(charmander.get_breed())
print(charmander.get_types())
print(charmander.hitPoints)
print(charmander.attack)
print(charmander.defense)
print(charmander.speed)
print(charmander.special)
print(charmander)
charmander.name = "Steve"
print(charmander)