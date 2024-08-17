from src.diffraction_case import DiffractionCase

if __name__ == "__main__":

  case1 = DiffractionCase(0.1)

  case1.setSlitToBulkheadDists([1000] * 2)
  case1.setDestructInterfDists([12.45, 23.20])

  case1.generateReport(f"a={case1.slit_length}")

  case2 = DiffractionCase(0.2)

  case2.setSlitToBulkheadDists([1000] * 2)
  case2.setDestructInterfDists([6.10, 12.60])

  case2.generateReport(f"a={case2.slit_length}")

  case3 = DiffractionCase(0.4)

  case3.setSlitToBulkheadDists([1000] * 2)
  case3.setDestructInterfDists([2.55, 5.70])

  case3.generateReport(f"a={case3.slit_length}")