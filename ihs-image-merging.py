"""
Image Merging using Intensity Hue Saturation (IHS) Method using PCI Geomatica
Author: Jim Honglin Wei
Date: 2021-03-10
Reference/Source: Frank Kenny, GEOM075ImageFusionV1, PCI Geomatica, PCI Geomatica Python Cookbook
License: MIT License
"""

import pci
from pci.pcimod import pcimod
from pci.ihs import ihs
from pci.fun import fun
from pci.lut import lut
from pci.rgb import rgb

#Add new image channels to existing file
print("Pix file must be set up as Channel 1: SPOT Pan June 4, 1985 \nChannel 2-5: TM Band 1-4")
print("Put the correct pix file path into new_file")
# Input version
# new_file = input("Enter file path: ")
# new_file = r"{}".format(new_file)
new_file = r"C:\PCI Geomatics\OakRidgesV1.pix" # File location, reset to local path
channels = [7] #add 7 8bit channels for analysis

# Adding new channels
pcimod(file=new_file, pciop="ADD", pcival=channels)

file = new_file
dbic = [5,4,3] # Input RGB channels
dboc = [6,7,8] # Output IHS channels
dbiw = [] # Input Window - Optional
ihsmodel = "CYLINDER"

ihs(file, dbic, dboc, dbiw, ihsmodel)

# Empty variables indicate optional variables as indicated from documentation
func = "MATC" # Enhancement function
dbic = [1] # Input raster channel(s)
dblut = []
dbsn = "SPOT" # Segment name
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