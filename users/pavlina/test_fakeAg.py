
from agilent import Agilent
agilent = Agilent()
agilent.fakeAgilentScan()
newsamp=agilent.agilentScan()
import numpy as np
print newsamp
vol=np.mean(newsamp, axis = 0)
print vol
##newsamp=agilent.fakeAgilentScan()
##import numpy as np
##print newsamp
