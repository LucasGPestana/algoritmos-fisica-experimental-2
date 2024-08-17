from .resistors_relationship import ResistorsRelationsip
from typing import List, Tuple

def saveStreamOnFile(stream: str) -> None:

    import os

    PROJECT_DIRPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):

        os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

    file_stream = open(os.path.join(PROJECT_DIRPATH, "files", "results.txt"), 'a', encoding="utf-8")
    
    file_stream.write(stream)

    file_stream.close()

def calculateResistance(resistances: List[float], relationship_kind: str) -> float:

    if len(resistances) < 2: 
        
        raise Exception("Pelo menos duas resistências devem ser passadas!")
    
    if len(resistances) == 2:
        
        return ResistorsRelationsip([resistances[0], resistances[1]], relationship_kind).equivalent_resistance
    
    else:
        
        rel = ResistorsRelationsip([resistances[0], resistances[1]], relationship_kind)

        return calculateResistance([rel.equivalent_resistance] + resistances[2:], relationship_kind)

def displayResistances(all_resistances: List[float], relationship_kind: str, num_resistors: int) -> str:
    
    resistances_relationship_indexes: List[Tuple[int]] = None
    output: str = ""

    match num_resistors:
        
        case 2:
            
            resistances_relationship_indexes = [(2, 3), (3, 4), (4, 5), (6, 7), (5, 6), 
                                                (7, 8), (8, 9), (9, 10), (10, 11)]
        
        case 3:
            
            resistances_relationship_indexes = [(2, 3, 4), (3, 4, 5), (4, 5, 6), 
                                                (5, 6, 7), (6, 7, 8)]
        
        case 4:
            
            resistances_relationship_indexes = [(2, 3, 4, 5), (6, 7, 8, 9)]
        
        case _:
            
            raise Exception("A quantidade de resistores (num_resistors) deve ser 2, 3 ou 4!")
    
    resistances_relationship_indexes = [tuple(map(lambda x: x - 2, resistance_relationship_indexes)) for resistance_relationship_indexes in resistances_relationship_indexes]
    
    output += f"{relationship_kind.capitalize()} ({num_resistors} resistores)\n\n"

    for resistance_relationship_indexes in resistances_relationship_indexes:
        
        output += f'{" e ".join([f"R{j+2}" for j in resistance_relationship_indexes])} -> {calculateResistance([all_resistances[i] for i in resistance_relationship_indexes], relationship_kind)} \u2126\n'

    output += "\n\n"

    return output