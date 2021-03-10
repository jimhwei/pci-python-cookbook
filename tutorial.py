import pci
from pci.ihs import ihs
from pci.fun import fun
from pci.lut import lut
# print("This version of PCI is", pci.version)
# print(ihs)

file = r"C:\Users\jimwe\github\pci-python-cookbook\OakRidgesV1.pix" # File location
dbic = [5,4,3] # Input RGB channels
# Need empty channels
dboc = [6,7,8] # Output IHS channels
dbiw = [] # Input Window - Optional
ihsmodel = "CYLINDER"

ihs(file, dbic, dboc, dbiw, ihsmodel)

func = "MATC" # Enhancement function
dbic = [1] # Input raster channel(s)
dblut = []
dbsn = "Testing"
dbsd = "SPOT Matched to Intensity" # Output LUT segment description
ostr = []
sdpt = []
trim = []
mask = []
dbhc = [6] #Input histogram match channel
lasc = []

fun(file, func, dbic, dblut, dbsn, dbsd, ostr, sdpt, trim, mask, dbhc, lasc)

fili = file
dbic = [1]
lutfile = file # Input file name
dblut = [3] # This should match the lut file created
maskfile = ""
mask = []
filo = fili
dboc = [9]
datatype = ""
ftype = ""
foptions = ""

lut(fili, dbic, lutfile, dblut, maskfile, mask, filo, dboc, datatype, ftype, foptions)