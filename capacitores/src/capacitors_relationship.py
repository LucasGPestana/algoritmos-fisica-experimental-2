from typing import List

class CapacitorsRelationsip:

  def __init__(self, capacitances: List[float], relationship_kind: str):

    if len(capacitances) != 2:

      raise Exception("A quantidade de capacitâncias em uma relação deve ser 2!")

    self.capacitances = capacitances
    self.relationship_kind = relationship_kind
  
  @property
  def equivalent_capacitance(self) -> float:

    match self.relationship_kind:

      case "paralelo":

        return sum(self.capacitances)
      
      case "serie":

        return (self.capacitances[0] * self.capacitances[1]) / sum(self.capacitances)

      case _:

        raise Exception("Tipo de relação entre capacitores inválido. O tipo deve ser 'paralelo' ou 'serie'!")