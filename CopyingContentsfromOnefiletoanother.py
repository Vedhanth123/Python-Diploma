
# outputfile = open("file2", "w") # opening a file with write permissions and store into outputfile object

# with open("file1", "r") as scan: # opening a file with read permisions and store into scan object
#     outputfile.write(scan.read()) # This lines reads from file1 and writes it to file2

# print("Copied from file1 to file2")

# outputfile.close()  # closing the file2

# # Output --------------------------------------------------------------------------------------------------------------
# Copid from file1 to file2

import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")