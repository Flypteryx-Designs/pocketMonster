def PocketMonster(pyType, name=""):
  def __init__(self):
    self.__PYMONID = pyType.pyMonID
    self.name = name if name != "" else pyType.name
    self.types = pyType.types
    self.max_hit_points = pyType.HP
    self.current_HP = pyType.HP
    self.attack = pyType.attack
    self.defense = pyType.defense
    self.special = pyType.special
    self.speed = pyType.speed
    self.moves = pyType.moves
    
  
  def get_name(self):
    return self.name
  
  def set_name(self, new_name):
    self.name = new_name
  
  def get_HP(self):
    return self.current_HP
  
  def get_move(self, move):
    return self.moves[move]
  
  def update_HP(self, deltaHP):
    new_HP = self.current_HP + deltaHP
    if new_HP < 0:
      self.current_HP = 0
    elif new_HP > self.max_hit_points:
      self.current_HP = self.max_hit_points
    else:
      self.current_HP = new_HP
      
  def update_move(self, move, deltaMP):
    new_move_count = self.moves[move] + deltaMP
    if new_move_count < 0:
      self.moves[move].currentMP = 0
    elif new_move_count > self.moves[move].maxMP:
      self.moves[move].currentMP = self.moves[move].maxMP
    else:
      self.moves[move].currentMP = new_move_count
      
  