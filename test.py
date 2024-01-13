import streamlit as st

if 'c' not in st.session_state:
    st.session_state.c = 2

if 'prompts' not in st.session_state:
    st.session_state.prompts = []

def inc_c():
    st.session_state.c += 1


for i in range(st.session_state.c):
    c1, c2 = st.columns(2)
    with c1:
        st.text_input(f"Scene {i}", key=f"text{i}")


def collect():
    st.session_state.prompts = []
    prompts = []
    for k, v in st.session_state.items():
        if k.startswith("text"):
            prompts.append(v)
    st.session_state.prompts = prompts


st.button("➕ Add field", on_click=inc_c)
st.button("Submit", on_click=collect)
##
#prompts = st.session_state.prompts
