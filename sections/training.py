import streamlit as st


def render():
    height = ''
    weight = ''

    st.text_input(label='Пульс утром в покое', value=height)
    st.date_input(label='Дата тренировки')
    st.text_input(label='Количество тренировок', value=weight)
    st.time_input(label='Время начала основной тренировки')
    st.text_input(label='Продолжительность тренировки', value=weight)
    st.selectbox('Направленность', (
        '', 'Силовая', 'Скоростно-силовая', 'Специяльная выносливость', 'Общая выносливость', 'ОФП', 'Техническая'))

    if st.button('Сохранить'):
        st.write('Сохранено')
