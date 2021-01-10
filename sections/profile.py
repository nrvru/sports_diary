import streamlit as st


def render():
    name = ''
    age = ''
    season_best = ''
    experience = ''

    st.text_input(label='Фамилия Имя', value=name)
    st.text_input(label='Возраст', value=age)
    st.selectbox('Специализация', ('', '400м с/б', '400м'))
    st.selectbox('Квалификация', ('', 'III', 'II', 'I', 'КМС', 'МС', 'МСМК'))
    st.text_input(label='Лучший результат сезона', value=season_best)
    st.text_input(label='Стаж занятий', value=experience)

    if st.button('Сохранить'):
        st.write('Сохранено')
