import streamlit as st


def display_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def on_change_radio():
    st.session_state["current_chat_id"] = st.session_state["selected_chat_history_id"]
