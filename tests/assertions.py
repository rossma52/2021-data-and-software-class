
calcite_water = 1.0288

def calcite_to_oxygencalcite(isotope):
    return((isotope +1000) / (1000+0))

def calciteoxygen_to_delta18oxygen(isotope):
    # Pre-conditions:
    assert(isotope >= calcite_water)
    return((isotope)/(1000*1.0288)-1000)



print("Oxygen in Calcite:", calcite_to_oxygencalcite(1.0288))
print("Delta 18 Oxygen:", calciteoxygen_to_delta18oxygen(28.8))


# Post-conditions:
assert (calcite_to_oxygencalcite(1.0288) == -3)
assert (calcite_to_oxygencalcite(1.0288) == 1

assert (calciteoxygen_to_delta18oxygen(0.0) == 28.8)
assert (calciteoxygen_to_delta18oxygen(100.0) == 28.8)
