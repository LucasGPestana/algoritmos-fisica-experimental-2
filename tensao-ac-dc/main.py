from src.utils import *

if __name__ == "__main__":

    expected_voltages = [3, 6, 9, 12]

    oscilloscope_obtained_dc_voltages = [3.06, 6.24, 9.08, 12.0]
    multimeter_obtained_dc_voltages = [3.017, 5.98, 8.85, 11.84]
    
    oscilloscope_obtained_ac_voltages = [9.12, 18.2, 27.0, 36.0]
    multimeter_obtained_ac_voltages = [3.168, 6.25, 9.40, 12.56]

    compareResults(expected_voltages, oscilloscope_obtained_dc_voltages, multimeter_obtained_dc_voltages, "DC")
    compareResults(expected_voltages, oscilloscope_obtained_ac_voltages, multimeter_obtained_ac_voltages, "AC")