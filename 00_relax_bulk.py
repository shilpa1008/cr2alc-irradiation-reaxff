from ase.io import read, write
from utils.qe_calculator import qe_calc

structure = read("../data/structures/initial/cr2alc.xyz")
calc = qe_calc()
structure.set_calculator(calc)

structure.get_potential_energy()
write("../data/structures/relaxed/cr2alc_relaxed.xyz", structure)
