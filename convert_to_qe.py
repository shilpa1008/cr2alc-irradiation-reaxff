from ase.io import read, write
structure = read("../../data/structures/initial/cr2alc.cif")
write("../../data/structures/initial/cr2alc.xyz", structure)
