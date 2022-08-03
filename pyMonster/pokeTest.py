import unittest

from numpy import equal
import main

class pokeTest(unittest.TestCase):
  def setUp(self):
    self.pokemon = main.Pokemon('charmander', 39, 52, 43, 65, 50, ["fire", None], ["Scratch", "Growl"])

  def testName(self):
    self.assertEqual(self.pokemon.name, 'charmander')
    self.pokemon.name = "Steve"
    self.assertEqual(self.pokemon.name, "Steve")
  
  def testBaseStat(self):
    self.assertEqual(self.pokemon.hitPoints, 39)
    self.assertEqual(self.pokemon.attack, 52)
    self.assertEqual(self.pokemon.defense, 43)
    self.assertEqual(self.pokemon.speed, 65)
    self.assertEqual(self.pokemon.special, 50)
  
  def testBreed(self):
    self.assertEqual(self.pokemon.get_breed(), "charmander")
  
  @unittest.expectedFailure
  def testRepr(self):
    messageOne = "Charmander currently has 39 HP."
    print(type(self.pokemon))
    print(self.pokemon)
    self.assertEqual(self.pokemon, messageOne)
    self.pokemon.name = "Steve"
    messageTwo = "Steve (a charmander) currently has 39 HP."
    self.assertEqual(self.pokemon, messageTwo)
                     
  def testType(self):
    types = self.pokemon.get_types()
    self.assertEqual(types[0], 'fire')
    self.assertEqual(types[1], None)

unittest.main()
