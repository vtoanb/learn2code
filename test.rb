class Viking
  # class methods and variables here
  # attribute accessor 
  attr_accessor :name, :age, :health, :strength
  
  # Initialize method for viking
  def initialize(name, age, health, strength)
    @name = name
    @age = age
    @health = health
    @strength = strength
  end

  def attack(enemy)
    # code to fight
  end

  def health
    @health
  end

  # setter method have equal sign
  def health=(new_health)
     @health = new_health
  end

  def take_damage(damage)
    self.health -= damage
    self.shout("OUCH!")
  end
  
  # shouting when being hit
  def shout(str)
    puts str
  end
  
  # creating warrior, rand = random
  # below is factory method, kind of classmethod in python
  def self.create_warrior(name)
    age = rand * 20 + 15
    health = [age * 5, 120].min
    strength = [age / 2, 10].min
    Viking.new(name, health, age, strength)
  end
  
  def self.random_name
    ["Erik", "Lars", "Leif"].sample
  end
  
  def self.silver_to_gold(silver_pieces)
    gold_pieces * 10
  end
end
