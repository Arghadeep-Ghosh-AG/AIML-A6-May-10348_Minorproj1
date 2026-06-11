# AIML-A6-May-10348_Minorproj1

# Resume Screening System

## Overview

The Resume Screening System is a Machine Learning and Natural Language Processing (NLP) based application that automatically classifies resumes into different job categories. The system helps recruiters and organizations reduce manual effort by analyzing resume content and predicting the most suitable job domain.

The project uses text preprocessing, TF-IDF vectorization, and machine learning classification algorithms to learn patterns from resume data and categorize unseen resumes accurately.

---

## Features

* Automated resume classification
* NLP-based text preprocessing
* TF-IDF feature extraction
* Machine Learning based prediction
* User-friendly Streamlit interface
* Fast and scalable resume screening process

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* NLP
* TF-IDF Vectorization
* Machine Learning

---

## Dataset

This project uses the Resume Dataset available on Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

After downloading the dataset, place the file in the following location:

dataset/
└── Resume.xls

---

## Project Structure

Resume-Screening-System/

├── dataset/

│   └── Resume.xls

├── models/

├── train.py

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

Clone the repository:

git clone https://github.com/your-username/Resume-Screening-System.git

Move into the project directory:

cd Resume-Screening-System

Install dependencies:

pip install -r requirements.txt

---

## Training the Model

Run:

python train.py

The trained model will be saved inside the models directory.

---

## Running the Application

Run:

streamlit run app.py

Open the generated local URL in your browser.

---

## Workflow

1. Load resume dataset.
2. Preprocess resume text.
3. Convert text into numerical features using TF-IDF.
4. Train the machine learning model.
5. Save the trained model.
6. Predict the category of new resumes through the Streamlit application.

---

## Future Enhancements

* PDF resume upload support
* Resume ranking based on job description
* Skill extraction and analysis
* Candidate-job matching score
* Deep Learning and BERT-based classification
* Resume recommendation system

---

## Author

Arghadeep Ghosh

B.Tech Computer Science Engineering
