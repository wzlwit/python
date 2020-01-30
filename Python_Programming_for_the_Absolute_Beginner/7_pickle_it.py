# Pickle It     (revserve it)
# Demonstrates pickling and shelving data
import pickle
import shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

# Pickled objects must be stored in a binary file
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()


""" 
dump(object, file, [,bin])      Writes pickled version of object to file. If bin is True, object is written in binary format. If bin is False, object is written in less
efficient, but more human- readable, text format. The default value of bin is equal to False.
load(file)                      Unpickles and returns the next pickled object in file.
"""
