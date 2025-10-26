from flask import Flask, render_template, request
import os
import docx2txt
import pdfplumber
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def extract_text(file):
    ext = file.filename.split('.')[-1].lower()
    if ext == 'pdf':
        with pdfplumber.open(file) as pdf:
            return '\n'.join(page.extract_text() or '' for page in pdf.pages)
    elif ext == 'docx':
        return docx2txt.process(file)
    return ''


@app.route('/')
def index():
    return render_template('index.html', results=None)


@app.route('/upload', methods=['POST'])
def upload():
    resumes = request.files.getlist('resumes')
    jd_text = request.form.get('job_description')

    results = []
    for resume in resumes:
        resume_text = extract_text(resume)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([jd_text, resume_text])
        similarity = cosine_similarity(vectors[0:1], vectors[1:2]).flatten()[0]
        percentage = round(similarity * 100, 2)

        results.append({
            'filename': secure_filename(resume.filename),
            'match': percentage
        })

    # Force page reload by rendering new data freshly
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
