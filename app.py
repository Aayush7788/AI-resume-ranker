import os
from flask import Flask, render_template, request, send_file
from utils.extractor import extract_text_from_pdf
from utils.preprocessor import preprocess_text
from model.ranker import rank_resumes
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes/'
REPORT_FILE = 'reports/result.csv'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('reports/', exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/rank', methods=['POST'])
def rank():
    files = request.files.getlist("resumes")
    job_desc = open('job_description.txt').read()
    job_desc_clean = preprocess_text(job_desc)

    resumes, file_names = [], []
    for file in files:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        raw = extract_text_from_pdf(filepath)
        cleaned = preprocess_text(raw)
        resumes.append(cleaned)
        file_names.append(file.filename)

    ranked = rank_resumes(job_desc_clean, resumes)
    results = [{"filename": file_names[i], "score": round(score, 3)} for i, score in ranked]

    pd.DataFrame(results).to_csv(REPORT_FILE, index=False)
    return render_template('index.html', results=results)

@app.route('/download')
def download():
    return send_file(REPORT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
