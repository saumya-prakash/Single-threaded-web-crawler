from modules import *
from db_utilities import *

store = "/home/saumya/Desktop/DATA_alt/"

f1 = os.listdir(store)


for a in f1:

    os.rename(store+a, store+'x'+a)

