# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Allison Hai
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year  = float('nan') 
month = float('nan') 
day   = float('nan') 
hour  = float('nan') 
min   = float('nan') 
sec   = float('nan') 

# parse script arguments
if len(sys.argv)==7:
    year  = float(sys.argv[1])
    month = float(sys.argv[2])
    day   = float(sys.argv[3])
    hour  = float(sys.argv[4])
    min   = float(sys.argv[5])
    sec   = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 year month day hour min sec'\
    )
    exit()

# calculate fractional julian date 
JD =  math.floor(day - 32075 + 1461* (year+4800+(month-14)/12)/4 +367*(month-2-(month-14)/12*12)/12 -3*((year+4900+(month-14)/12)/100)/4)
JD_midnight = JD - 0.5
D_frac = (sec+60*(min+60*hour))/86400
JD_frac = JD_midnight+D_frac

print(JD_frac)