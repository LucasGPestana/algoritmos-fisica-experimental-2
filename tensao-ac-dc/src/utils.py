from .oscilloscope import Oscilloscope
from typing import List

def calculateDistance(obtained_voltage: float, expected_voltage: float) -> float:

    return abs(expected_voltage - obtained_voltage)

def generateFile(filename: str, stream: str) -> None:
    
    import os
    
    PROJECT_DIRPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):
         
         os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

    file_stream = open(os.path.join(PROJECT_DIRPATH, "files", filename), "wb")

    file_stream.write(stream.encode())

    file_stream.close()

def compareResults(expected_voltages: List[float],
                   oscilloscope_voltages: List[float],
                   multimeter_voltages: List[float],
                   voltage_kind: str) -> None:

    stream: str = ""

    fullname = {"AC": "Corrente Alternada", "DC": "Corrente Contínua"}

    if not voltage_kind.upper() in ["AC", "DC"]:

            raise Exception("O tipo de tensão só pode ser AC (Alternada) ou DC (Contínua)!")

    for i in range(len(expected_voltages)):

        osc = Oscilloscope(oscilloscope_voltages[i], voltage_kind)

        stream += f"\nTensão Esperada: {expected_voltages[i]} V\n"
        stream += f"Tensão Obtida no sciloscópio: {oscilloscope_voltages[i]} V\n"
        stream += f"Tensão Obtida no multpimetro: {multimeter_voltages[i]} V\n"
        stream += f"Tipo de tensão: {fullname[voltage_kind.upper()]}\n"
        stream += f"Distância entre a tensão do osciloscópio e a tensão esperada: {calculateDistance(osc.effective_voltage if voltage_kind == 'AC' else oscilloscope_voltages[i], expected_voltages[i])} V\n"
        stream += f"Distância entre a tensão do multímetro e a tensão esperada: {calculateDistance(multimeter_voltages[i], expected_voltages[i])} V\n\n"
        
    generateFile(f"{voltage_kind.lower()}-results.txt", stream)