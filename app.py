import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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




st.text_area("Enter your feedback:")
st.number_input("Enter a number:", min_value=0, max_value=100)
st.slider("Select a value:", min_value=0, max_value=100, value=50)
st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C"])
st.date_input("Select a date:")
st.time_input("Select a time:")
st.radio("Choose one:", ["Choice 1", "Choice 2", "Choice 3"])
st.checkbox("I agree to the terms and conditions")


#Matplotlib Chart

fig, ax = plt.subplots()
ax.plot(data["Column 1"], data["Column 2"], marker='o')

st.pyplot(fig)
