newphrase = "rainstorm"
#           012345678
#           123456789 <---- college board version
# create a new variable called shortphrase
# and assign it a value by slicing 
# the newphase variable by removing
# the first 3 characters
# the last 3 characters
# the first three characters are "rai"
# the last three characters are "orrm"
# substring(string, start, end)
shortphrase = newphrase[3:len(newphrase)-3]
# college board version [4:len(newphrase)-3]
print(shortphrase)
# explain len(newphrase)-3 = 9-3 = 6
# why does it end with 6
# because the last index is not included