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
