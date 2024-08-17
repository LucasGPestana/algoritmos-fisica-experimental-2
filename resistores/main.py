from src.resistors_relationship import ResistorsRelationsip
from src.utils import *

# Todas as resistências estão em ohms
resistances = [6.72e3, 3.222e3, 0.979e3, 0.980e3, 326.2,
               325.8, 98.5, 98.8, 99.7e3, 9.83e3, 0.980e3, 99.1, 0.979e3]
stream: str = ""

# Em série

for i in range(2, 5):

  stream += displayResistances(resistances, "serie", i)

# Em paralelo

for i in range(2, 5):
    
  stream += displayResistances(resistances, "paralelo", i)

# Misto

# R2 e R3 em paralelo
# R4 e R5 em paralelo
# As suas resistencias equivalentes estao em serie

stream += "Misto (R2 e R3 em paralelo, R4 e R5 em paralelo)\n\n"

m1_r2_r3 = ResistorsRelationsip([resistances[0], resistances[1]], "paralelo")
m1_r4_r5 = ResistorsRelationsip([resistances[2], resistances[3]], "paralelo")
m1_r_total = ResistorsRelationsip([m1_r2_r3.equivalent_resistance, m1_r4_r5.equivalent_resistance], "serie")

stream += f"R2 e R3 e R4 e R5: {m1_r_total.equivalent_resistance} \u2126\n\n"

# R2 e R3 em serie
# R4 e R5 em paralelo
# As suas resistencias equivalentes estao em serie

stream += "Misto (R2 e R3 em serie, R4 e R5 em paralelo)\n\n"

m2_r2_r3 = ResistorsRelationsip([resistances[0], resistances[1]], "serie")
m2_r4_r5 = ResistorsRelationsip([resistances[2], resistances[3]], "paralelo")
m2_r_total = ResistorsRelationsip([m2_r2_r3.equivalent_resistance, m2_r4_r5.equivalent_resistance], "serie")

stream += f"R2 e R3 e R4 e R5: {m2_r_total.equivalent_resistance} \u2126\n\n"

# R2, R3 e R4 em paralelo
# A sua resistencia equivalente junto ao R5 em serie

stream += "Misto (R2, R3 e R4 em paralelo, Req[R2,R3,R4] e R5 em serie)\n\n"

m3_r2_r3 = ResistorsRelationsip([resistances[0], resistances[1]], "paralelo")
m3_r2_r3_r4 = ResistorsRelationsip([m3_r2_r3.equivalent_resistance, resistances[3]], "paralelo")
m3_r_total = ResistorsRelationsip([m3_r2_r3_r4.equivalent_resistance, resistances[4]], "serie")

stream += f"R2 e R3 e R4 e R5: {m3_r_total.equivalent_resistance} \u2126\n\n"

saveStreamOnFile(stream)