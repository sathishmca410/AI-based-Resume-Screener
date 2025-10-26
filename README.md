AI-based Resume Screener – Project Documentation

1. Project Overview

The AI-based Resume Screener is a web application that helps recruiters automatically screen resumes by comparing them with a job description. It calculates a similarity score between the job description and uploaded resumes, highlights keywords, and provides a percentage match. This reduces manual effort and speeds up candidate shortlisting.

2. Objectives

Allow users to upload multiple resumes in PDF or DOCX format.
Accept job description input from the user.
Extract text from resumes using PDF and DOCX parsers.
Compute similarity score between resumes and job description using TF-IDF and cosine similarity.
Highlight keywords from the job description in each resume for easy visual analysis.
Provide a clean, user-friendly web interface for recruiters.

3. Features

Resume Upload: Supports multiple file uploads (PDF and DOCX).
Job Description Input: Text area to paste job descriptions.
Keyword Highlighting: Automatically highlights important keywords from JD in the resume.
Similarity Scoring: Calculates a percentage match for each resume.
Results Display: Displays match percentage and highlighted resume content in a structured format.

4. Project Structure
AI-based Resume Screener

├── app.py                 # Main Flask application

├── requirements.txt       # Required Python packages

├── utils/

    └── extractor.py       # Functions to extract text from PDF and DOCX resumes

├── templates/

    └── index.html         # Frontend HTML template

└── static/
    
    └── style.css          # CSS file for styling

5. Technology Stack

Frontend:	HTML, CSS

Backend:	Python, Flask

Resume Parsing:	pdfplumber, docx

NLP / Matching:	scikit-learn (TF-IDF, cosine similarity)

File Handling:	werkzeug

6. Requirements

Python 3.11+

Virtual Environment (optional but recommended)

Libraries:

Flask==3.1.2

pdfplumber==0.11.7

docx2txt==0.9

scikit-learn==1.7.2

7. Installation Steps

    1. Clone the repository:

     git clone <repository-url>

     cd AI-based Resume Screener

    2. Create a virtual environment:

     python -m venv venv

     venv\Scripts\activate

    Install dependencies:

    python -m pip install -r requirements.txt


    Run the Flask app:

    python app.py

    Open your browser and navigate to: http://127.0.0.1:5000/

8. Usage Instructions

Open the web app in a browser.

Upload one or multiple resumes in PDF or DOCX format.

Paste the job description in the text area.

Click Submit.

View the results, including:

  Percentage match for each resume.

  Keywords from JD highlighted in resumes.

9. Future Improvements

Add support for DOC format resumes.

Integrate resume parsing with NLP to extract skills, education, experience separately.

Store results in a database for historical tracking.

Add downloadable report of shortlisted resumes.

Improve frontend with Bootstrap / Tailwind for responsive design.

10. References

Flask Documentation

pdfplumber Documentation

docx2txt Documentation

Scikit-learn Documentation
