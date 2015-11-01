#
# Neil Trimboy 2011
#

from hm_constants import *

# Master Address
MY_MASTER_ADDR = 0x81

# A zone is a controlled area from a single thermostat
# A zone my consist of one or more heating circuits
# Each heating circuit covers a floor area

# A list of controllers
# Adjust the number of rows in this list as required
# Items in each row are :
# Controller Address, ShortName, LongName, Controller Type, Graph Colour, List of circuits on this zone
StatList = [
[1,  "Study", "Study",    HMV3_ID, "A020F0", [19,20]],
[2,  "Entrc", "Entrance", HMV3_ID, "D02090", [21,22]],
[3,  "Dinig", "Dining",   HMV3_ID, "FF4500", [17,18]],
[4,  "Livig", "Living",   HMV3_ID, "FF8C00", [13,14,15,16]],
[5,  "Kitch", "Water",  HMV3_ID, "FA8072", [23,5,7]],
]
# Named indexing into StatList
SL_ADDR = 0
SL_SHRT_NAME = 1
SL_LONG_NAME = 2
SL_CONTR_TYPE = 3
SL_GRAPH_COL = 4
SL_CIRCUITS = 5


# A list of circuits
# A circuit is a single run of pipe from manifold
# Circuit No., ShortName, LongName, Area heated
# Area heated is a list of rectangles, each rectangle has a x and y dimension
#    This means you do not have to work out the area, just the size of the rectangles that make up the area
CircuitList = [
[1,  "Bthrm", "Bathroom", [[2.15,2.8],[1.0,1.0]]],
[2,  "M_E_S", "M_E_S", [[2.0,3.96]]],
[3,  "W_I_R", "WIR", [[2.1,5.45]]],
[4,  "BD1_E", "Bed1 East", [[5.7,1.735]]],
[5,  "HALLE", "Hallway East",[[1.15,8.51],[2.36,1.0]]],
[6,  "BD1_W", "Bed1 West", [[5.7,1.735],[3.22,0.41]]],
[7,  "HALLW", "Hallway West", [[1.15,5.5]]],
[8,  "LAUND", "Laundry", [[2.4,2.01],[1.135,0.6],[2.36,1.02]]],
[9,  "FAM_N", "Family North", [[5.74,2.23]]],
[10, "FAM_S", "Family South", [[5.74,2.23]]],
[11, "BED_3", "Bed3", [[3.6,3.6]]],
[12, "BED_2", "Bed2", [[3.6,3.6]]],
[13, "LG_NW", "Lounge NW", [[2.75,3.35]]],
[14, "LG_SW", "Lounge SW", [[2.75,3.35]]],
[15, "LG_NE", "Lounge SE", [[2.75,3.35]]],
[16, "LG_SE", "Lounge SE", [[2.75,3.35]]],
[17, "DIN_N", "Dining N", [[2.75,4.5]]],
[18, "DIN_S", "Dining S", [[2.75,4.5]]],
[19, "STD_W", "Study W", [[2.21,3.55]]],
[20, "STD_E", "Study E", [[2.21,3.55]]],
[21, "TOILT", "Toilet", [[1.44,1.57],[1.0,2.22],[1.0,1.44],[1.57,1.06],[1.67,1.63]]],
[22, "ENTRC", "Entry", [[2.82,2.6],[1.0,1.44]]],
[23, "KITCH", "Kitchen", [[5.02,4.84]]],
]

# Kitchen area to correct

# Named indexing into CircuitList
CL_ADDR = 0
CL_SHRT_NAME = 1
CL_LONG_NAME = 2
CL_RECTANGLES = 3
