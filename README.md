# 📊 Student Data Cleaner & Analyzer

A simple and interactive **Streamlit-based Data Science application** for cleaning, analyzing, and visualizing student data.

The application allows users to upload a CSV file containing student data. It investigates the dataset, handles common data-quality problems, performs basic analysis, creates visualizations, and allows the cleaned data to be downloaded.

---

## 📌 Introduction

Working with real-world data often involves problems such as missing values, duplicate records, and unclean information.

The **Student Data Cleaner & Analyzer** is designed to make this process easier.

The application follows a complete data-processing workflow:

1. **Data Upload** – Users upload a student dataset in CSV format.
2. **Data Investigation** – The application checks the dataset structure, columns, data types, missing values, and duplicate records.
3. **Data Cleaning** – Missing values and duplicate records are handled.
4. **Data Analysis** – Basic statistics are calculated to understand the dataset.
5. **Data Visualization** – Charts are created to represent the data visually.
6. **Download** – Users can download the cleaned dataset as a CSV file.

---

## ✨ Features

* 📂 Upload CSV student datasets
* 🔍 Investigate dataset structure
* 🧹 Clean missing values
* ♻️ Remove duplicate records
* 📊 Perform basic data analysis
* 📈 Create data visualizations
* 💾 Download cleaned CSV data
* 🖥️ Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

* **Python** – Main programming language
* **Pandas** – Data loading, manipulation, and cleaning
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Streamlit** – Interactive web application

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
```

Or install all libraries together:

```bash
pip install pandas numpy matplotlib seaborn streamlit
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git armankhan5094865arman/Student-Data-Cleaner-and-Analyzer
```

### 2. Open the Project Folder

```bash
cd Student-Data-Cleaner-and-Analyzer
```

### 3. Install the Required Libraries

```bash
pip install pandas , numpy , matplotlib , seaborn , streamlit
```

### 4. Run the Streamlit Application

```bash
streamlit run Data_Cleaner.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run Data_Cleaner.py
```

---

## 📂 Project Structure

```text
Student_Data_Cleaner/
│
├── Data_Cleaner.py
├── README.md
└── App_Images/
    ├── App_GUI.png
    ├── Data_Cleaning.png
    ├── Data_Analysis.png
    ├── Data_Visualization.png
    └── ...
```

---

## 🔄 How the Application Works

```text
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
```

---

## 🧹 Data Cleaning

The application checks and handles common data-quality problems.

### Missing Values

The application identifies missing values and handles them using suitable data-cleaning methods.

### Duplicate Records

Duplicate rows are detected and removed from the dataset to improve data quality.

---

## 📊 Data Analysis

After cleaning the dataset, the application performs basic analysis such as:

* Total number of students
* Average marks
* Highest marks
* Lowest marks
* Average age

These results help users understand the important information in the dataset.

---

## 📈 Data Visualization

The project uses **Matplotlib** and **Seaborn** to create visual representations of the student data.

Charts make it easier to understand patterns, relationships, and differences in the dataset.

---

## 💾 Download Cleaned Data

After the cleaning process, users can download the cleaned dataset as:

```text
cleaned_student_data.csv
```

This cleaned file can then be used for further analysis or other Data Science projects.

---

## 🎯 Project Goal

The main goal of this project is to apply Python and Data Science concepts in a practical and functional application.

It demonstrates how different Python libraries can work together:

```text
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
```

---

## 📚 What I Learned

Through this project, I practiced:

* Working with CSV datasets
* Data cleaning with Pandas
* Handling missing values
* Removing duplicate data
* Performing basic data analysis
* Creating data visualizations
* Using Matplotlib and Seaborn
* Building an interactive application with Streamlit
* Combining multiple Python libraries in one project
* Turning Data Science concepts into a functional application

---

## 🔮 Future Improvements

Possible future improvements include:

* More advanced data-cleaning options
* Additional visualization types
* More statistical analysis
* Support for additional dataset formats
* More interactive features
* Machine Learning functionality

---

## 👨‍💻 About the Developer

**Arman Khan**

Computer Science Student | Data Science Enthusiast | Aspiring AI Engineer

This project is part of my journey of learning **Python, Data Science, Machine Learning, and AI Engineering** through practical projects.

---

## ⭐ Acknowledgment

This project was created as part of my learning journey in **Python, Data Science, and AI Engineering**.

Building this application helped me understand how different Python libraries can be combined to create a complete and useful Data Science application.
