from .capacitors_relationship import CapacitorsRelationsip
from typing import List, Tuple

def saveStreamOnFile(stream: str) -> None:

    import os

    PROJECT_DIRPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):

        os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

    file_stream = open(os.path.join(PROJECT_DIRPATH, "files", "results.txt"), 'a', encoding="utf-8")
    
    file_stream.write(stream)

    file_stream.close()

def calculateCapacitance(capacitances: List[float], relationship_kind: str) -> float:

    """

        Serve para calcular a capacitância resultante em circuitos com apenas um tipo de relacionamento entre os capacitores (ou seja, todos os capacitores em paralelo ou todos os capacitores em série)
    
    """

    if len(capacitances) < 2: 
        
        raise Exception("Pelo menos duas capacitâncias devem ser passadas!")
    
    if len(capacitances) == 2:
        
        return CapacitorsRelationsip([capacitances[0], capacitances[1]], relationship_kind).equivalent_capacitance
    
    else:
        
        rel = CapacitorsRelationsip([capacitances[0], capacitances[1]], relationship_kind)

        return calculateCapacitance([rel.equivalent_capacitance] + capacitances[2:], relationship_kind)

def displayCapacitances(all_capacitances: List[float], relationship_kind: str, num_capacitors: int) -> str:

    """
        Serve para guardar o fluxo de caracteres, correspondente ao conteudo de "results.txt", em uma só string
    """
    
    capacitances_relationship_indexes: List[Tuple[int]] = None
    output: str = ""

    match num_capacitors:
        
        case 2:
            
            capacitances_relationship_indexes = [(0, 1), (0, 2), (0, 3), (0, 4),
                                                (1, 2), (1, 3), (1, 4),
                                                (2, 3), (2, 4),
                                                (3, 4)]
        
        case 3:
            
            capacitances_relationship_indexes = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 2, 4),
                                                (0, 1, 3), (0, 1, 4), (1, 2, 3),
                                                (2, 3, 4), (1, 2, 4), 
                                                (1, 3, 4)]
        
        case 4:
            
            capacitances_relationship_indexes = [(0, 1, 2, 3), (0, 1, 2, 4), (1, 2, 3, 4),
                                                (0, 2, 3, 4), (0, 1, 3, 4)]
        
        case _:
            
            raise Exception("A quantidade de capacitores (num_capacitors) deve ser 2, 3 ou 4!")
    
    output += f"{relationship_kind.capitalize()} ({num_capacitors} capacitores)\n\n"
    
    for capacitance_relationship_indexes in capacitances_relationship_indexes:
        
        output += f'{" e ".join([f"C{i+1}" for i in capacitance_relationship_indexes])} -> {calculateCapacitance([all_capacitances[i] for i in capacitance_relationship_indexes], relationship_kind)} F\n'

    output += "\n\n"

    return output