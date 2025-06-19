from time import time

import requests
import streamlit as st

from src.utils import display_messages, on_change_radio

if not st.session_state.get("chat_history"):
    chat_id = f"chat-{time()}"
    st.session_state["current_chat_id"] = chat_id
    st.session_state["chat_history"] = {chat_id: []}


st.title("Chat layer")

with st.sidebar:
    new_chat = st.button("New chat", use_container_width=True)
    st.title("Chat History")


if new_chat:
    chat_id = f"chat-{time()}"
    st.session_state["chat_history"][chat_id] = []
    st.session_state["current_chat_id"] = chat_id


st.sidebar.radio(
    "_",
    options=st.session_state["chat_history"].keys(),
    key="selected_chat_history_id",
    on_change=on_change_radio,
)

messages = st.session_state["chat_history"][st.session_state.get("current_chat_id")]

prompt = st.chat_input("Écrire ici...")

if prompt:
    messages.append({"role": "user", "content": prompt})
    display_messages(messages)

    response = requests.post("http://localhost:8000/chat", json=messages)

    with st.chat_message("assistant"):
        st.write(response.json()["content"])
        messages.append(response.json())

    st.session_state["chat_history"][st.session_state.get("current_chat_id")] = messages
else:
    display_messages(messages)
