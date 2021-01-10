import streamlit as st


def render():
    height = ''
    weight = ''

    st.text_input(label='Рост', value=height)
    st.text_input(label='Вес', value=weight)
    st.text_input(label='Обхват груди', value=weight)
    st.text_input(label='Обхват талии', value=weight)
    st.text_input(label='Обхват бедра', value=weight)
    st.text_input(label='Обхват голени', value=weight)
    st.text_input(label='Длина бедра', value=weight)
    st.text_input(label='Длина голени', value=weight)

    if st.button('Сохранить'):
        st.write('Сохранено')
