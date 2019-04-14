import os
import random

eps = os.listdir('episodes/')
episode = 'episodes/' + eps[random.randint(0, len(eps)-1)]
os.system("open " + episode)

