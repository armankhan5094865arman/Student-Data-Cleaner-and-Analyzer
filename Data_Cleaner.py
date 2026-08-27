import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: lightblue;
}
</style>
""", unsafe_allow_html=True)

st.title("Student Data_Cleaner")
st.subheader("Welcome to my Data_Cleaner App ")
file = st.file_uploader("upload your csv file ", type=["csv"])

import pandas as pd

if file is not None:
    df = pd.read_csv(file)
    st.write("your current file is :")
    st.dataframe(df)
    st.subheader("Data Information")
    st.write("Rows : ", df.shape[0])
    st.write("Columns : ", df.shape[1])
    st.write("Missing Values ")
    st.write(df.isnull().sum())
    st.write("Duplicated Values")
    st.write(df.duplicated().sum())
    st.subheader("Data Cleaning ")
if st.button("clean Data "):
    df = df.drop_duplicates()
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
    df["City"] = df["City"].fillna("unknown")

    st.success("Data cleaned successfully! ")
    st.markdown("Data cleaned")
    st.dataframe(df)

    csv = df.to_csv(index=False)
    st.download_button(
        label="Download cleaned data ",
        data=csv,
        file_name="student_cleaned_data.csv",
        mime="text/csv",
    )
    st.subheader("Data Analysis")
    st.write("Total students are ", len(df))
    st.write("Average marks is : ", df["Marks"].mean())
    st.write("Maximum marks is : ", df["Marks"].max())
    st.write("Minimum marks is : ", df["Marks"].min())
    st.write("Average age of the student is : ", df["Age"].mean())
    st.write("Minimum age of the student is : ", df["Age"].min())
    st.write("Maximum age of the student is : ", df["Age"].max())

    st.subheader("Data visualization")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.bar(df["Name"], df["Marks"], color=["green", "blue", "yellow", "red"])
    ax.set_xlabel("Student Names")
    ax.set_ylabel("Student Marks")
    ax.set_title("Student Marks Representation")
    st.pyplot(fig)
    
    
    cities = df["City"].unique()

    selected_city = st.selectbox(
       "Select a City",
    cities
    )

    filtered_df = df[df["City"] == selected_city]

    st.dataframe(filtered_df)
    
    
    
