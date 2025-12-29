from ase.io import read, write
structure = read("../../data/structures/initial/Cr2AlC.cif")
write("../../data/structures/initial/Cr2AlC.xyz", structure)
