import streamlit as st

import sections.profile
import sections.anthropometry
import sections.training
import sections.condition.index
import sections.control
import sections.analysis

SECTIONS = {
    "Профиль": sections.profile,
    "Антропометрия": sections.anthropometry,
    "Тренировочный процесс": sections.training,
    "Состояние": sections.condition.index,
    "Контрольные тесты, соревнования": sections.control,
    "Анализ тренировочной деятельности": sections.analysis,
}

st.set_page_config(page_title="Спортивный дневник")
st.sidebar.header("Разделы")
selection = st.sidebar.radio("", list(SECTIONS.keys()))
st.title(selection)
section = SECTIONS[selection]
section.render()
