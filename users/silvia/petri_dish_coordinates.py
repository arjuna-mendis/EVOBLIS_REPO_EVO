# Coordinates of the Petri dishes on the experimental layer
import sys
from petridish import PetriDish
sys.path.append('../api')
sys.path.append('../settings')


# coordinates of the petri dishes centers with syringe in socket 4 - decanol
petri_dish_coord = {0: (193, 154),
                    1: (193, 252),
                    2: (193, 350),
                    3: (193, 448),
                    4: (97, 154),
                    5: (97, 252),
                    6: (97, 350),
                    7: (97, 448),
                    'waste': (23, 415),
                    'clean_water': (23, 499)
                    }


goalPos = -40
diameter = 90
cleanliness = True
evobot = None
# the petridishes are instantiated with the cleanliness flag set to True, same diameter and coordinates from the dict
petridishes = []
for i in range(len(petri_dish_coord)-2):
    petridishes.append(PetriDish(evobot, petri_dish_coord[i], goalPos, diameter, cleanliness, worldCor=None))

# toilet_petri = PetriDish(evobot, petri_dish_coord['toilet'], goalPos, diameter, worldCor=worldcor)





