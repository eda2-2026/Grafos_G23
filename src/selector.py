import streamlit as st


def course_selector(courses: dict) -> str:
    """
    Exibe um seletor de curso e retorna o identificador escolhido.
    """
    course_ids = list(courses.keys())

    selected_course_id = st.radio(
        "Selecione seu curso:",
        options=course_ids,
        format_func=lambda course_id: courses[course_id]["name"],
    )

    return selected_course_id


def subject_checklist(title: str, subjects: list[dict], key_prefix: str) -> set[str]:
    """
    Exibe uma lista de disciplinas com checkboxes.

    Retorna um conjunto com os códigos das disciplinas selecionadas.
    """
    st.subheader(title)

    selected_subjects = set()

    for subject in subjects:
        label = f"{subject['code']} - {subject['name']}"

        is_selected = st.checkbox(
            label,
            key=f"{key_prefix}_{subject['code']}",
        )

        if is_selected:
            selected_subjects.add(subject["code"])

    return selected_subjects
