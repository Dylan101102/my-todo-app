import streamlit as st
import functions

todos = functions.get_to_dos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # This captures what the user typed in.
    todos.append(todo)
    functions.write_to_dos(todos)
    st.session_state["new_todo"] = "" # Clears input box


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # If the checkbox is checked
        todos.pop(index)
        functions.write_to_dos(todos) # Writes the new todo list.
        del st.session_state[todo] # Deletes the selected pair from the session state.
        st.rerun() # Needed when working with checkboxes.


st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# st.session_state # Use while building web app