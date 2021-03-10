from pci.cimpro2 import cimpro2

new_file = r"C:\Users\jimwe\Google_Drive\aFlemingWinter\GEOM75-Advanced-RS\python-cookbook\first-empty-file.pix"
create_channels = [4, 0, 1, 2] #creates 4 8bit, 0 16bit signed, 1 16bit unsigned and 2 32bit real channels
extents = ["514418.000", "5262616.000", "527908.000", "5246564.000"] #List of ULX, ULY, LRX and LRY values
res= "2.0"

cimpro2(file=new_file, dbnc=create_channels, dblayout="PIXEL", project="UTM", zone=[55], row="G", ellips="D000",
        llbound="N", ulx=extents[0], uly=extents[1], lrx=extents[2], lry=extents[3], bxpxsz="2", bypxsz="2")
