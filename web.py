import streamlit as st
import utils

st.title("My to-do app")
st.write("This app is used to track the to do items")
content = utils.get_todos()
print(content)

def add_item():
    if "to-do" in st.session_state:
        item = st.session_state["to-do"] + "\n"
        content.append(item)
        utils.write_todo(content)
        st.rerun()

for index, todo in enumerate(content):
    checkbox = st.checkbox(label=todo, key=f"{index}-{todo}")
    if checkbox:
        content.pop(index)
        utils.write_todo(content)
        del st.session_state["to-do"]
        st.rerun()


st.text_input(label="add items", placeholder="enter the to do item..", on_change=add_item(), key="to-do")

print(f"session_state: {st.session_state}")