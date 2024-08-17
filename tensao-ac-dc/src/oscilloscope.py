class Oscilloscope:

    def __init__(self, voltage: float, voltage_kind: str):
        
        self.voltage_kind = voltage_kind.upper()
        self.voltage = voltage
        
    @property
    def peak_to_peak_voltage(self) -> float:

        if self.voltage_kind == "AC":

            return self.voltage

        return 0.0

    @property
    def effective_voltage(self) -> float:

        return self.peak_to_peak_voltage / (2 * 2 ** (1/2))    

        

    
