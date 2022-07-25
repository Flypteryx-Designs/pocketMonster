class Pokemon:
  """This is the docstring for the pokemon class"""
  def __init__(self, hitPoints, attack, defense, speed, special, types, moves):
    self.maxHitPoints = hitPoints
    self.curHitPoints = hitPoints
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.special = special
    self.types = types
    self.moves = moves
    self.status = []
    
  def increase_HP(self, delta):
    """This function increases the hitpoints no higher than max"""
    if (self.curHitPoints + delta) > self.maxHitPoints:
      self.curHitPoints = self.maxHitPoints
    else:
      self.curHitPoints += delta
  
  def decrease_HP(self, delta):
    """This function decreases the hitpoints no lower than zero"""
    if (self.curHitPoints - delta) <= 0:
      self.curHitPoints = 0
      self.status = ["fainted"]
    else:
      self.curHitPoints -= delta
  
  def add_status(self, condition):
    """This function checks to see if a condition is already applied and 
    if it is not, then it is applied. If it is, it does nothing."""
    if condition not in self.status:
      self.status.append(condition)
    
  def remove_status(self, condition):
    """This function checks to see if a condition is applied and then 
    removes it. If it is not, it does nothing"""
    if condition in self.status:
      self.status.remove(condition)
      
  def use_move(self, move):
    pass
  
  