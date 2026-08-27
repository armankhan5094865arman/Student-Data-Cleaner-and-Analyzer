# Student Data Cleaner & Analyzer

A simple and interactive Data Science application built with Python and Streamlit.

This project allows users to upload a student dataset in CSV format. The application investigates the uploaded data, cleans common data problems, performs basic data analysis, creates visualizations, and allows the cleaned dataset to be downloaded.

The main purpose of this project is to turn basic Data Science and Python knowledge into a practical and usable application.

---

## 📌 Introduction

Working with real-world data often involves problems such as missing values, duplicate records, and unclean information.

The **Student Data Cleaner & Analyzer** is designed to make this process easier.

The user uploads a student dataset in CSV format, and the application performs several steps:

1. **Data Upload** – The user uploads a CSV file.
2. **Data Investigation** – The application checks the structure of the dataset, including rows, columns, missing values, and duplicate records.
3. **Data Cleaning** – Missing values and duplicate records are handled.
4. **Data Analysis** – The application calculates useful information such as average marks, highest marks, lowest marks, average age, and total students.
5. **Data Visualization** – The application creates charts to help users understand the data visually.
6. **Download** – The cleaned dataset can be downloaded as a new CSV file.

---

## ✨ Features

- 📂 Upload student data in CSV format
- 🔍 Investigate dataset structure
- 🧹 Handle missing values
- ♻️ Remove duplicate records
- 📊 Calculate basic statistics
- 📈 Create data visualizations
- 💾 Download cleaned data
- 🖥️ Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Pandas** – Data loading, manipulation, and cleaning
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Streamlit** – Interactive web application

---

## 📋 Requirements

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install streamlit

---

## 🚀 How to run 

1. Clone the repository
git armankhan5094865arman/Student-Data-Clreaner and Analyzer
2. Install the required libraries
pip install pandas , numpy , matplotlib , seaborn , streamlit
3. Run the Streamlit application
streamlit run Data_Cleaner.py

If the streamlit command is not recognized, use:

python -m streamlit run Data_Cleaner.py

---

## 📂 Project Structure
Student_Data_Cleaner/
│
├── Data_Cleaner.py
├── README.md
└── App_images

---

## 🔄 How the Application Works

CSV File
   ↓
Data Upload
   ↓
Data Investigation
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Data Visualization
   ↓
Download Cleaned CSV

---

## 📊 Data Cleaning

The application checks and handles common data-quality problems.

Missing Values

The application identifies missing values using Pandas and handles them using suitable methods.

Duplicate Records

Duplicate rows are detected and removed from the dataset.

---

## 📈 Data Analysis

After cleaning the dataset, the application performs basic analysis such as:

Total number of students
Average marks
Highest marks
Lowest marks
Average age

These results help users quickly understand the dataset.

---

## 📉 Data Visualization

The project uses Matplotlib and Seaborn to represent student data visually.

Charts make it easier to understand patterns and differences in the dataset.

---

## 💾 Download Cleaned Data

After the cleaning process, users can download the cleaned dataset as:

cleaned_student_data.csv

This allows users to use the cleaned data for further analysis or other Data Science projects.

---

## 🎯 Project Goal

The goal of this project is to practice and apply Python and Data Science concepts in a practical application.

It demonstrates how different Python libraries can work together:

Python
   ↓
Pandas + NumPy
   ↓
Data Cleaning & Analysis
   ↓
Matplotlib + Seaborn
   ↓
Data Visualization
   ↓
Streamlit
   ↓
Interactive Data Science Application

---

## 📚 What I Learned

Through this project , I practiced:

Working with CSV datasets
Data cleaning with Pandas
Handling missing values
Removing duplicate data
Performing basic data analysis
Creating visualizations
Using Streamlit to build an interactive application
Combining multiple Python libraries in one project
Turning Data Science concepts into a functional application 

---

## 🔮 Future Improvements

Possible future improvements include:

More advanced data-cleaning options
More visualization types
Additional statistical analysis
Support for more dataset formats
More interactive controls
Machine Learning features

---

## 👨‍💻 Author

Arman Khan

Aspiring AI Engineer | Data Science & Python Learner

---

## ⭐ Acknowledgment

This project was created as part of my learning journey in Python, Data Science, and AI Engineering.

Building this project helped me understand how individual Python libraries can be combined to create a complete and useful application.