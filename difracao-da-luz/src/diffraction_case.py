import numpy as np
from typing import List

class DiffractionCase:

  def __init__(self, slit_length: float):

    self.__slit_length = slit_length
  
  def setSlitToBulkheadDists(self, slit_bulkhead_dists: List[float]):

    self.__slit_bulkhead_dists = np.array(slit_bulkhead_dists)
  
  def setDestructInterfDists(self, dest_interf_dists: List[float]):

    if len(dest_interf_dists) != len(self.__slit_bulkhead_dists):

      raise Exception("A quantidade de distâncias de interferências destrutivas de ser a mesma de distâncias da fenda ao anteparo!")

    self.__dest_interf_dists = np.array(dest_interf_dists) / 2
  
  def __calculateWaveLength(self, slit_bulkhead_dist: float, dest_interf_dist: float, order: int) -> float:

    return (self.__slit_length * dest_interf_dist) / (slit_bulkhead_dist * order)
  
  def __setValuesOfWaveLengths(self) -> None:

    wave_lengths = np.array([], dtype=np.float32)

    for i in range(len(self.__dest_interf_dists)):

      wave_lengths = np.append(wave_lengths, self.__calculateWaveLength(self.__slit_bulkhead_dists[i], self.__dest_interf_dists[i], i+1))
    
    return wave_lengths
  
  @property
  def dest_interf_dists(self):

    return self.__dest_interf_dists

  @property
  def slit_bulkhead_dists(self):

    return self.__slit_bulkhead_dists
  
  @property
  def wave_lengths(self):

    return self.__setValuesOfWaveLengths()
  
  @property
  def slit_length(self):

    return self.__slit_length
  
  @staticmethod
  def convertMilimetersToNanometers(value_in_mm):

    return value_in_mm * (10 ** 6)
  
  def generateReport(self, case_name: str) -> None:

    import os

    PROJECT_DIRPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):

      os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

    file_stream = open(os.path.join(PROJECT_DIRPATH, "files", f"{case_name}.txt"), 'a', encoding="utf-8")

    file_stream.write(f"Para o comprimento da fenda (a) igual a {self.__slit_length}: \n\n")

    for i in range(len(self.__dest_interf_dists)):

      file_stream.write(f"Distância das interferências destrutivas de ordem {i+1}: {self.__dest_interf_dists[i]}\n")
      file_stream.write(f"Comprimento da onda de ordem {i+1}, em mm: {self.wave_lengths[i]}\n")
      file_stream.write(f"Comprimento da onda de ordem {i+1}, em nm: {DiffractionCase.convertMilimetersToNanometers(self.wave_lengths[i])}\n\n")

    file_stream.close()