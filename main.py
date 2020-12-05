# ==================================================== #
#  Created By: Darhil Aslaliya -  GitHub :- darsh-22   #
#  Created By: Dhruv Prajapati -  GitHub :- imdhruv99  #
# ==================================================== #

import glob 
import os

# EX: '/home/username/Desktop/any folder path/**/*.<txt>' <---- ANY FILE TYPE ---->
PATH = "Enter your Path Here"

# Returns a list of names in list files. 
print("Using glob.glob()") 
files = glob.glob( PATH , recursive = True) 
for file in files: 
    os.remove(file)