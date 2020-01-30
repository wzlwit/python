import shelve
print("\nShelving lists.")
s = shelve.open("pickles2.dat")         # works with a file that stores pickled objects and not characters.

s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]

""" 
Access Mode     Description
"c"     <default>. Open a file for reading or writing. If the file doesn’t exist, it’s created.
"n"     Create a new file for reading or writing. If the file exists, its contents are overwritten.
"r"     Read from a file. If the file doesn’t exist, Python will complain with an error.
"w"     Write to a file. If the file doesn’t exist, Python will complain with an error.
"""

# pickles works like a dictionary, but a shelf key can only be a string.

s.sync() # make sure data is written. Though Python writes changes to a shelf file to a buffer and then periodically writes the buffer to the file
print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()