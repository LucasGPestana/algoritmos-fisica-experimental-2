from typing import Union, List, Tuple
import numpy as np
import math

class RefractiveModule:

  def __init__(self, air_refractive_index: float, ini_env: str):
    
    self.__air_refractive_index = air_refractive_index

    if not ini_env.casefold() in ("ar", "acrilico", "acrílico"):

      raise Exception("O meio inicial deve ser ar ou acrílico!")
    
    self.__ini_env = ini_env

    self.__incidence_thetas = np.array([0]*8, dtype=np.float64)
    self.__refraction_thetas = np.array([0]*8, dtype=np.float64)
  
  def setIncidenceThetas(self, ini_incidence_theta: float, sample_number: int):

    if sample_number <= 0:

      raise Exception("O número de amostras deve ser, no mínimo, um!")

    self.__incidence_thetas = np.arange(
      ini_incidence_theta, 
      ini_incidence_theta * sample_number + 1, 
      ini_incidence_theta)
  
  def setRefractionThetas(self, refraction_thetas: Union[np.ndarray, List, Tuple]):

    if len(refraction_thetas) != len(self.__incidence_thetas):

      raise Exception("A quantidade de amostras de ângulos de refração não corresponde ao de ângulos de incidência!")

    self.__refraction_thetas = np.array(refraction_thetas, dtype=np.float32)
  
  def __calculateAcrylicRefractiveIndex(self, incidence_theta, refraction_theta):

    if self.__ini_env.casefold() == "ar":

      return self.__air_refractive_index * (math.sin(math.radians(incidence_theta)) / math.sin(math.radians(refraction_theta)))
    
    else:

      return self.__air_refractive_index * (math.sin(math.radians(refraction_theta)) / math.sin(math.radians(incidence_theta)))
    
  def __setValuesOfAcrylicRefractiveIndex(self):

    acrylic_refractive_indexes = np.array([], dtype=np.float32)

    if not any(self.__incidence_thetas) or not any(self.__refraction_thetas):

      raise Exception("Os ângulos de incidência e/ou os ângulos de refração não foram definidos!")

    for i in range(len(self.__incidence_thetas)):

      acrylic_refractive_indexes = np.append(acrylic_refractive_indexes, self.__calculateAcrylicRefractiveIndex(self.__incidence_thetas[i], self.__refraction_thetas[i]))
    
    return acrylic_refractive_indexes
  
  def calculateMeanAcrylicRefractiveIndex(self):

    return math.fsum(self.__setValuesOfAcrylicRefractiveIndex()) / len(self.__setValuesOfAcrylicRefractiveIndex())
  
  @property
  def acrylic_refractive_indexes(self):
    
    return self.__setValuesOfAcrylicRefractiveIndex()
  
  @property
  def incidence_thetas(self):

    return self.__incidence_thetas
  
  @property
  def refraction_thetas(self):

    return self.__refraction_thetas
  
  def generateReport(self, module_name):

    import os

    PROJECT_DIRPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):

      os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

    file_stream = open(os.path.join(PROJECT_DIRPATH, "files", f"{module_name.casefold()}.txt"), 'w', encoding="utf-8")

    file_stream.write("\u03b8i - Ângulo de incidência\n")
    file_stream.write("\u03b8r - Ângulo de refração\n")
    file_stream.write("N. ac - Índice de refração do acrílico\n")

    file_stream.write(f"\n{module_name.title()}\n\n")

    file_stream.write("\u03b8i | \u03b8r | N. ac\n")
    for i in range(len(self.incidence_thetas)):

      file_stream.write(f"{self.incidence_thetas[i]:02d} | {self.refraction_thetas[i]:02.0f} | {self.acrylic_refractive_indexes[i]}\n")
  
    file_stream.write("\n")
  
    file_stream.write(f"Média dos indíces de refração do acrílico: {self.calculateMeanAcrylicRefractiveIndex()}\n")

    file_stream.close()