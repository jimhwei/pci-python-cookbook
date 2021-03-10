import pci
from pci.pcimod import pcimod
from pci.ihs import ihs
from pci.fun import fun
from pci.lut import lut
from pci.rgb import rgb
# print("This version of PCI is", pci.version)
# print(ihs)

#Add new image channels to existing file
new_file = r"C:\Users\jimwe\github\pci-python-cookbook\OakRidgesV1.pix" # File location
channels = [7] #add 4 8bit, 0 16bit signed, 3 16bit unsigned and 1 32bit real channels

# Adding new channels
pcimod(file=new_file, pciop="ADD", pcival=channels)

file = new_file
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
dblut = [2] # This should match the lut file created
maskfile = ""
mask = []
filo = fili
dboc = [9]
datatype = ""
ftype = ""
foptions = ""

lut(fili, dbic, lutfile, dblut, maskfile, mask, filo, dboc, datatype, ftype, foptions)

dbic = [9,7,8]
dboc = [10,11,12]
dbiw = []
ihsmodel = "CYLINDER"

rgb(file, dbic, dboc, dbiw, ihsmodel)