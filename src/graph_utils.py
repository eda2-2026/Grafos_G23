from typing import Set, List, Dict
from src.estruturasCurriculares import DISCIPLINAS

def build_graph(subject_codes_in_course: List[str]) -> Dict[str, List[str]]:
    """
    Constrói a lista de adjacência (grafo direcionado normal).
    Os vértices são os 'codes' das disciplinas (ex: 'CIC0004').
    Retorna: { 'CIC0004': ['codigo_desbloqueado1', ...], ... }
    """
    code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}
    id_to_code = {k: v["code"] for k, v in DISCIPLINAS.items()}
    
    graph = {code: [] for code in subject_codes_in_course}
    
    for code in subject_codes_in_course:
        subj_id = code_to_id.get(code)
        if not subj_id:
            continue
        prereqs = DISCIPLINAS[subj_id].get("prerequisites", [])
        for p in prereqs:
            p_code = id_to_code.get(p)
            if p_code in graph:
                graph[p_code].append(code)
                
    return graph

def build_reverse_graph(subject_codes_in_course: List[str]) -> Dict[str, List[str]]:
    """
    Constrói a lista de adjacência reversa (pré-requisitos).
    Os vértices são os 'codes' das disciplinas (ex: 'CIC0004').
    Retorna: { 'CIC0004': ['prereq1', 'prereq2', ...], ... }
    """
    code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}
    id_to_code = {k: v["code"] for k, v in DISCIPLINAS.items()}
    
    reverse_graph = {code: [] for code in subject_codes_in_course}
    
    for code in subject_codes_in_course:
        subj_id = code_to_id.get(code)
        if not subj_id:
            continue
        prereqs = DISCIPLINAS[subj_id].get("prerequisites", [])
        for p in prereqs:
            p_code = id_to_code.get(p)
            if p_code in reverse_graph:
                reverse_graph[code].append(p_code)
                
    return reverse_graph
