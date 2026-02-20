import numpy as np
import pandas as pd
import streamlit as st

# Displaying Text Content

st.title("Welcome to My Streamlit App")

st.write("Hello Anurag")

#Creating charts and graphs
data = pd.DataFrame(
    np.random.randn(10, 2), columns=["Column 1", "Column 2"]
)
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)


#Sidebar, Image and & Video
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar content.")
st.image(
    "./lighthouse.png",
    caption="Lighthouse",
)
st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")

#File Upload (csv)

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

#Taking User Input

name = st.text_input("Enter your name:")
if st.button("Welcome"):
    st.success(f"Welcome to Streamlit, {name}!")

age = st.number_input("Enter your age:", min_value=0, max_value=120)
st.write(f"You are {age} years old.")

#Text and Markdown 
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is some plain text.")
st.markdown(
    "This is **Markdown** text with *emphasis* and [a link](https://www.streamlit.io)."
)
st.code("""
        import streamlit as st

        def greet(name):
            return f'Hello, {name}!'
""", language="python");
