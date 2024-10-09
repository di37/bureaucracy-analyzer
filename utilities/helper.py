import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import streamlit as st


def initialize_session_state():
    if "department" not in st.session_state:
        st.session_state.department = None
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
