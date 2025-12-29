from ase.calculators.espresso import Espresso

def qe_calc(pseudopot_path="../qe_inputs/pseudopotentials"):
    input_data = {
        "control": {
            "calculation": "relax",
            "pseudo_dir": pseudopot_path,
            "tprnfor": True,
            "tstress": True
        },
        "system": {
            "ecutwfc": 50,
            "ecutrho": 400,
            "occupations": "smearing",
            "smearing": "mp",
            "degauss": 0.02,
            "nspin": 2,
            "starting_magnetization(1)": 0.3,  # Cr1
            "starting_magnetization(2)": 0.3,  # Cr2
        },
        "electrons": {
            "conv_thr": 1e-6,
        }
    }

    pseudopotentials = {
        "Cr": "cr_pbe_v1.5.uspp.F.UPF",
        "Al": "al_pbe_v1.uspp.F.UPF",
        "C":  "c_pbe_v1.2.uspp.F.UPF"
    }

    return Espresso(input_data=input_data,
                    pseudopotentials=pseudopotentials,
                    kpts=(6,6,2))

