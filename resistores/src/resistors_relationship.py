from typing import List

class ResistorsRelationsip:

  def __init__(self, resistances: List[float], relationship_kind: str):

    if len(resistances) != 2:

      raise Exception("A quantidade de resistências em uma relação deve ser 2!")

    self.resistances = resistances
    self.relationship_kind = relationship_kind
  
  @property
  def equivalent_resistance(self) -> float:

    match self.relationship_kind:

      case "paralelo":

        return (self.resistances[0] * self.resistances[1]) / sum(self.resistances)
      
      case "serie":

        return sum(self.resistances)

      case _:

        raise Exception("Tipo de relação entre resistores inválido. O tipo deve ser 'paralelo' ou 'serie'!")