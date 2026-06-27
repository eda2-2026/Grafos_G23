DISCIPLINAS = {
    # Compartilhadas
    "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES": {
        "code": "CIC0004",
        "name": "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
        "prerequisites": [],
    },
    "ENGENHARIA E AMBIENTE": {
        "code": "FGA0161",
        "name": "ENGENHARIA E AMBIENTE",
        "prerequisites": [],
    },
    "INTRODUÇÃO À ENGENHARIA": {
        "code": "FGA0163",
        "name": "INTRODUÇÃO À ENGENHARIA",
        "prerequisites": [],
    },
    "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR": {
        "code": "FGA0168",
        "name": "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
        "prerequisites": [],
    },
    "CÁLCULO 1": {
        "code": "MAT0025",
        "name": "CÁLCULO 1",
        "prerequisites": [],
    },

    "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA": {
        "code": "FGA0157",
        "name": "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
        "prerequisites": ["CÁLCULO 1"],
    },
    "FISICA 1": {
        "code": "IFD0171",
        "name": "FISICA 1",
        "prerequisites": [],
    },
    "FISICA 1 EXPERIMENTAL": {
        "code": "IFD0173",
        "name": "FISICA 1 EXPERIMENTAL",
        "prerequisites": [],
    },
    "CÁLCULO 2": {
        "code": "MAT0026",
        "name": "CÁLCULO 2",
        "prerequisites": ["CÁLCULO 1"],
    },
    "INTRODUCAO A ALGEBRA LINEAR": {
        "code": "MAT0031",
        "name": "INTRODUCAO A ALGEBRA LINEAR",
        "prerequisites": [],
    },

    "ENGENHARIA ECONÔMICA": {
        "code": "FGA0133",
        "name": "ENGENHARIA ECONÔMICA",
        "prerequisites": [],
    },
    "MÉTODOS NUMÉRICOS PARA ENGENHARIA": {
        "code": "FGA0160",
        "name": "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
        "prerequisites": ["CÁLCULO 2"],
    },
    "HUMANIDADES E CIDADANIA": {
        "code": "FGA0164",
        "name": "HUMANIDADES E CIDADANIA",
        "prerequisites": [],
    },

    # Compartilhadas sem contar Software
    "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA": {
        "code": "FGA0154",
        "name": "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA",
        "prerequisites": ["FISICA 1"],
    },
    "QUIMICA GERAL TEORICA": {
        "code": "IQD0125",
        "name": "QUIMICA GERAL TEORICA",
        "prerequisites": [],
    },
    "QUIMICA GERAL EXPERIMENTAL": {
        "code": "IQD0126",
        "name": "QUIMICA GERAL EXPERIMENTAL",
        "prerequisites": [],
    },
    "CÁLCULO 3": {
        "code": "MAT0027",
        "name": "CÁLCULO 3",
        "prerequisites": ["CÁLCULO 1"],
    },

    # Aeroespacial
    "CIÊNCIAS AEROESPACIAIS": {
        "code": "FGA0254",
        "name": "CIÊNCIAS AEROESPACIAIS",
        "prerequisites": [],
    },
    "SISTEMAS AEROESPACIAIS": {
        "code": "FGA0008",
        "name": "SISTEMAS AEROESPACIAIS",
        "prerequisites": ["FISICA 1", "CIÊNCIAS AEROESPACIAIS"],
    },

    # Automotiva
    "ONDULATÓRIA E FÍSICA TÉRMICA PARA ENGENHARIA": {
        "code": "FGA0090",
        "name": "ONDULATÓRIA E FÍSICA TÉRMICA PARA ENGENHARIA",
        "prerequisites": ["CÁLCULO 1", "FISICA 1", "FISICA 1 EXPERIMENTAL"],
    },
    "LABORATÓRIO DE ONDULATÓRIA E FÍSICA TÉRMICA PARA A ENGENHARIA": {
        "code": "FGA0107",
        "name": "LABORATÓRIO DE ONDULATÓRIA E FÍSICA TÉRMICA PARA A ENGENHARIA",
        "prerequisites": ["FISICA 1", "FISICA 1 EXPERIMENTAL"],
    },
    "INTRODUÇÃO AO DESIGN E CONCEPÇÃO DE VEÍCULOS": {
        "code": "FGA0155",
        "name": "INTRODUÇÃO AO DESIGN E CONCEPÇÃO DE VEÍCULOS",
        "prerequisites": ["DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR"],
    },

    # Energia

    # Software
    "MATEMÁTICA DISCRETA 1": {
        "code": "FGA0085",
        "name": "MATEMÁTICA DISCRETA 1",
        "prerequisites": ["APC"],
    },
    "ORIENTAÇÃO A OBJETOS": {
        "code": "FGA0158",
        "name": "ORIENTAÇÃO A OBJETOS",
        "prerequisites": ["ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES"],
    },

    # Eletrônica

    # Software e Eletrônica
    "PRÁTICA DE ELETRÔNICA DIGITAL 1": {
        "code": "FGA0071",
        "name": "PRÁTICA DE ELETRÔNICA DIGITAL 1",
        "prerequisites": ["INTRODUCAO A ALGEBRA LINEAR"],
    },
    "TEORIA DE ELETRÔNICA DIGITAL 1": {
        "code": "FGA0073",
        "name": "TEORIA DE ELETRÔNICA DIGITAL 1",
        "prerequisites": ["INTRODUCAO A ALGEBRA LINEAR"],
    },
}


CURSOS = {
    "AEROESPACIAL": {
        "name": "Engenharia Aeroespacial",
        "subjects": [
            "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
            "ENGENHARIA E AMBIENTE",
            "INTRODUÇÃO À ENGENHARIA",
            "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
            "CÁLCULO 1",
            "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
            "FISICA 1",
            "FISICA 1 EXPERIMENTAL",
            "CÁLCULO 2",
            "INTRODUCAO A ALGEBRA LINEAR",
            "ENGENHARIA ECONÔMICA",
            "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
            "HUMANIDADES E CIDADANIA",
            "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA",
            "QUIMICA GERAL TEORICA",
            "QUIMICA GERAL EXPERIMENTAL",
            "CÁLCULO 3",
            "CIÊNCIAS AEROESPACIAIS",
            "SISTEMAS AEROESPACIAIS"
        ],
    },
    "AUTOMOTIVA": {
        "name": "Engenharia Automotiva",
        "subjects": [
            "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
            "ENGENHARIA E AMBIENTE",
            "INTRODUÇÃO À ENGENHARIA",
            "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
            "CÁLCULO 1",
            "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
            "FISICA 1",
            "FISICA 1 EXPERIMENTAL",
            "CÁLCULO 2",
            "INTRODUCAO A ALGEBRA LINEAR",
            "ENGENHARIA ECONÔMICA",
            "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
            "HUMANIDADES E CIDADANIA",
            "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA",
            "QUIMICA GERAL TEORICA",
            "QUIMICA GERAL EXPERIMENTAL",
            "CÁLCULO 3",
            "ONDULATÓRIA E FÍSICA TÉRMICA PARA ENGENHARIA",
            "LABORATÓRIO DE ONDULATÓRIA E FÍSICA TÉRMICA PARA A ENGENHARIA",
            "INTRODUÇÃO AO DESIGN E CONCEPÇÃO DE VEÍCULOS"
        ],
    },
    "ENERGIA": {
        "name": "Engenharia de Energia",
        "subjects": [
            "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
            "ENGENHARIA E AMBIENTE",
            "INTRODUÇÃO À ENGENHARIA",
            "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
            "CÁLCULO 1",
            "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
            "FISICA 1",
            "FISICA 1 EXPERIMENTAL",
            "CÁLCULO 2",
            "INTRODUCAO A ALGEBRA LINEAR",
            "ENGENHARIA ECONÔMICA",
            "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
            "HUMANIDADES E CIDADANIA",
            "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA",
            "QUIMICA GERAL TEORICA",
            "QUIMICA GERAL EXPERIMENTAL",
            "CÁLCULO 3",
        ],
    },
    "SOFTWARE": {
        "name": "Engenharia de Software",
        "subjects": [
            "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
            "ENGENHARIA E AMBIENTE",
            "INTRODUÇÃO À ENGENHARIA",
            "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
            "CÁLCULO 1",
            "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
            "FISICA 1",
            "FISICA 1 EXPERIMENTAL",
            "CÁLCULO 2",
            "INTRODUCAO A ALGEBRA LINEAR",
            "ENGENHARIA ECONÔMICA",
            "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
            "HUMANIDADES E CIDADANIA",
            "MATEMÁTICA DISCRETA 1",
            "ORIENTAÇÃO A OBJETOS",
            "PRÁTICA DE ELETRÔNICA DIGITAL 1",
            "TEORIA DE ELETRÔNICA DIGITAL 1",
        ],
    },
    "ELETRONICA": {
        "name": "Engenharia Eletrônica",
        "subjects": [
            "ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES",
            "ENGENHARIA E AMBIENTE",
            "INTRODUÇÃO À ENGENHARIA",
            "DESENHO INDUSTRIAL ASSISTIDO POR COMPUTADOR",
            "CÁLCULO 1",
            "PROBABILIDADE E ESTATÍSTICA APLICADO A ENGENHARIA",
            "FISICA 1",
            "FISICA 1 EXPERIMENTAL",
            "CÁLCULO 2",
            "INTRODUCAO A ALGEBRA LINEAR",
            "ENGENHARIA ECONÔMICA",
            "MÉTODOS NUMÉRICOS PARA ENGENHARIA",
            "HUMANIDADES E CIDADANIA",
            "MECANICA DOS SÓLIDOS 1 PARA ENGENHARIA",
            "QUIMICA GERAL TEORICA",
            "QUIMICA GERAL EXPERIMENTAL",
            "CÁLCULO 3",
            "PRÁTICA DE ELETRÔNICA DIGITAL 1",
            "TEORIA DE ELETRÔNICA DIGITAL 1",
        ],
    },
}


def get_subjects_by_course(course_id: str) -> list[dict]:
    """
    Retorna as disciplinas de um curso.
    """
    course = CURSOS[course_id]

    return [
        DISCIPLINAS[subject_code]
        for subject_code in course["subjects"]
    ]
