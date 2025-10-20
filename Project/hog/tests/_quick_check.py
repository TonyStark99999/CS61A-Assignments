from hog import *
from dice import make_test_dice
print('roll_dice(3):', roll_dice(3, make_test_dice(4,2,1)))
print('boar_brawl(54,32):', boar_brawl(54,32))
print('take_turn(0):', take_turn(0, 54, 32))
print('take_turn(3):', take_turn(3, 0, 0, make_test_dice(3,4,5)))
print('num_factors(12):', num_factors(12))
print('sus_update(0,3,4):', sus_update(0,3,4))
