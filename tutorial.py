import pci
from pci.ihs import ihs
# print("This version of PCI is", pci.version)
# print(ihs)

file = r"C:\Users\jimwe\github\pci-python-cookbook\OakRidgesV1.pix" # File location
dbic = [5,4,3] # Input RGB channels
# Need empty channels
dboc = [6,7,8] # Output IHS channels
dbiw = [] # Input Window - Optional
ihsmodel = "CYLINDER"

ihs(file, dbic, dboc, dbiw, ihsmodel)