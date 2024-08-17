from src.capacitors_relationship import CapacitorsRelationsip
from src.utils import *


# Todas as capacitâncias estão em farads
capacitances = [9.71e-6, 9.57e-6, 9.45e-6, 44.59e-6, 48.64e-9]
stream: str = ""

# Em série

for num_capacitors in range(2, 5):

  stream += displayCapacitances(capacitances, "serie", num_capacitors)

# Em paralelo

for num_capacitors in range(2, 5):

  stream += displayCapacitances(capacitances, "paralelo", num_capacitors)

# Misto

# C1 e C2 em paralelo
# C3 e C4 em paralelo
# As suas capacitancias equivalentes estao em serie

stream += "Misto (C1 e C2 em paralelo, C3 e C4 em paralelo)\n\n"

m1_c1_c2 = CapacitorsRelationsip([capacitances[0], capacitances[1]], "paralelo")
m1_c3_c4 = CapacitorsRelationsip([capacitances[2], capacitances[3]], "paralelo")
m1_c_total = CapacitorsRelationsip([m1_c1_c2.equivalent_capacitance, m1_c3_c4.equivalent_capacitance], "serie")

stream += f"C1 e C2 e C3 e C4: {m1_c_total.equivalent_capacitance} F\n\n"

# C1 e C2 em serie
# C3 e C4 em paralelo
# As suas capacitancias equivalentes estao em serie

stream += "Misto (C1 e C2 em serie, C3 e C4 em paralelo)\n\n"

m2_c1_c2 = CapacitorsRelationsip([capacitances[0], capacitances[1]], "serie")
m2_c3_c4 = CapacitorsRelationsip([capacitances[2], capacitances[3]], "paralelo")
m2_c_total = CapacitorsRelationsip([m2_c1_c2.equivalent_capacitance, m2_c3_c4.equivalent_capacitance], "serie")

stream += f"C1 e C2 e C3 e C4: {m2_c_total.equivalent_capacitance} F\n\n"

# C1, C2, C3 em paralelo
# A sua resistencia equivalente junto ao C4 em serie

stream += "Misto (C1, C2 e C3 em paralelo, Req[C1, C2, C3] e C4 em serie)\n\n"

m3_c1_c2 = CapacitorsRelationsip([capacitances[0], capacitances[1]], "paralelo")
m3_c1_c2_c3 = CapacitorsRelationsip([m3_c1_c2.equivalent_capacitance, capacitances[3]], "paralelo")
m3_c_total = CapacitorsRelationsip([m3_c1_c2_c3.equivalent_capacitance, capacitances[4]], "serie")

stream += f"C1 e C2 e C3 e C4: {m3_c_total.equivalent_capacitance} F\n\n"

saveStreamOnFile(stream)