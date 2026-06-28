import streamlit as st

from src.estruturasCurriculares import CURSOS, DISCIPLINAS, get_subjects_by_course
from src.selector import course_selector, subject_checklist
from src.graph_utils import build_reverse_graph, validate_planned_subjects
from html import escape
import textwrap
import graphviz


st.set_page_config(
    page_title="Validador de Matrícula UnB Gama",
    page_icon="🎓",
    layout="wide",
)

st.title("Validador de Matrícula em Disciplinas")

st.write(
    """
    Este trabalho modela as matrizes curriculares dos cursos de Engenharia do campus UnB Gama
    (Engenharia **Aeroespacial**, Engenharia **Automotiva**, Engenharia **de Energia**, Engenharia **de Software**
    e Engenharia **Eletrônica**) como um **grafo direcionado**, onde cada disciplina é um vértice, e cada pré-requisito é uma aresta.
    """
)

st.info(
    """
    **Fluxo da aplicação**

    1. O aluno seleciona sua Engenharia.
    2. O aluno seleciona as disciplinas já concluídas.
    3. O aluno seleciona as disciplinas que pretende cursar.
    4. O sistema utiliza DFS no grafo reverso para buscar pré-requisitos.
    5. A interface mostra se a matrícula planejada é válida ou não.
    """
)

st.divider()

st.header("Curso")
st.write(
    "Selecione o seu curso."
)

selected_course_id = course_selector(CURSOS)
subjects = get_subjects_by_course(selected_course_id)

st.divider()

st.header("Disciplinas do curso selecionado")

st.write(
    """
    Marque as disciplinas que você já concluiu e as disciplinas que
    você pretende cursar no próximo semestre.
    """
)

left_column, right_column = st.columns(2)

with left_column:
    completed_subjects = subject_checklist(
        title="Disciplinas concluídas",
        subjects=subjects,
        key_prefix=f"completed_{selected_course_id}",
    )

with right_column:
    planned_subjects = subject_checklist(
        title="Disciplinas pretendidas",
        subjects=subjects,
        key_prefix=f"planned_{selected_course_id}",
    )


def get_subject_display_name(subject_code: str, code_to_id: dict) -> str:
    """
    Recebe o código oficial da disciplina e retorna o nome formatado dela.
    """
    subject_id = code_to_id.get(subject_code, subject_code)
    subject = DISCIPLINAS.get(subject_id)

    if subject:
        return subject["name"]

    return subject_id


def get_graphviz_node_html(subject_code: str, subject_name: str, status: str) -> str:
    color_map = {
        "completed": "#bbf7d0",
        "missing": "#fef08a",
        "target_allowed": "#bfdbfe",
        "target_blocked": "#fecaca",
    }
    bgcolor = color_map.get(status, "#ffffff")
    
    # Quebra de linha para não ficar uma caixa gigante
    wrapped_name = "<br/>".join(textwrap.wrap(subject_name, width=22))
    
    return f'''<<table border="1" cellborder="1" cellspacing="0" cellpadding="4" bgcolor="{bgcolor}">
      <tr><td align="center" width="140"><font point-size="11"><b>{subject_code}</b></font></td></tr>
      <tr><td align="center" width="140" height="40"><font point-size="10">{wrapped_name}</font></td></tr>
    </table>>'''


def render_dependency_path(result: dict, completed_subjects: set, code_to_id: dict):
    """
    Renderiza visualmente o caminho de pré-requisitos usando Graphviz.
    """
    dot_lines = [
        "digraph G {",
        '  rankdir=LR;',
        '  splines=ortho;',
        '  node [shape=none, margin="0", fontname="sans-serif"];'
    ]
    
    nodes_added = set()
    
    def add_node(code, is_target=False):
        if code in nodes_added:
            return
        name = get_subject_display_name(code, code_to_id)
        if is_target:
            status = "target_allowed" if result["allowed"] else "target_blocked"
        else:
            status = "completed" if code in completed_subjects else "missing"
            
        node_html = get_graphviz_node_html(code, name, status)
        dot_lines.append(f'  "{code}" [label={node_html}];')
        nodes_added.add(code)
    
    edges = result.get("edges", [])
    
    # Adicionar o nó alvo (mesmo se não tiver arestas)
    target = result["subject"]
    add_node(target, is_target=True)
    
    for prereq, subj in edges:
        add_node(prereq)
        add_node(subj)
        dot_lines.append(f'  "{prereq}" -> "{subj}";')
        
    dot_lines.append("}")
    
    dot_str = "\n".join(dot_lines)
    
    # Gera o SVG usando o executável dot do sistema
    try:
        svg_data = graphviz.Source(dot_str).pipe(format='svg').decode('utf-8')
        
        # Centraliza o SVG na tela
        html = f'<div style="display: flex; justify-content: center; margin-bottom: 24px;">{svg_data}</div>'
        st.markdown(html, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Erro ao renderizar gráfico: {e}")


code_to_id = {v["code"]: k for k, v in DISCIPLINAS.items()}

if planned_subjects:
    st.divider()
    st.header("Validação de Matrícula")

    subject_codes_in_course = [s["code"] for s in subjects]
    reverse_graph = build_reverse_graph(subject_codes_in_course)
    
    validation_results = validate_planned_subjects(planned_subjects, completed_subjects, reverse_graph)
    
    for result in validation_results:
        subj_code = result["subject"]
        subj_id = code_to_id.get(subj_code, subj_code)
        
        if result["allowed"]:
            st.success(f"A disciplina **{subj_id}** está liberada.")
        else:
            missing_ids = [code_to_id.get(c, c) for c in result["missing"]]
            st.error(f"A disciplina **{subj_id}** está bloqueada. Você precisa cursar antes: **{', '.join(missing_ids)}**.")

    st.divider()
    st.header("Caminhos de Dependência")
    st.markdown("""
    **Legenda de Cores:**
    <div style="display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 5px;"><span style="display: inline-block; width: 14px; height: 14px; background-color: #bbf7d0; border: 1px solid #9ca3af;"></span> Concluída</div>
        <div style="display: flex; align-items: center; gap: 5px;"><span style="display: inline-block; width: 14px; height: 14px; background-color: #fef08a; border: 1px solid #9ca3af;"></span> Pré-requisito faltante</div>
        <div style="display: flex; align-items: center; gap: 5px;"><span style="display: inline-block; width: 14px; height: 14px; background-color: #bfdbfe; border: 1px solid #9ca3af;"></span> Pretendida liberada</div>
        <div style="display: flex; align-items: center; gap: 5px;"><span style="display: inline-block; width: 14px; height: 14px; background-color: #fecaca; border: 1px solid #9ca3af;"></span> Pretendida bloqueada</div>
    </div>
    """, unsafe_allow_html=True)
    for result in validation_results:
        subject_name = get_subject_display_name(result["subject"], code_to_id)

        st.markdown(f"#### {subject_name}")

        if result["prerequisites"]:
            render_dependency_path(result, completed_subjects, code_to_id)
        else:
            st.info("Esta disciplina não possui pré-requisitos.")
