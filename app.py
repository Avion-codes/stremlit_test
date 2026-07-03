import stremlit as st

# take user input
name=st.text_input("Enter your name")
# heading 
st.title("Take the input ")
# create button for submite
if st.button("Submite"):
  st.write(f"print the name: {name}")
