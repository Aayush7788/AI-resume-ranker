# AI-resume-ranker

AI Resume Ranker

This project ranks resumes for a job profile using NLP techniques like SpaCy and TF-IDF vectorization, and provides a web interface built with Flask.

Features

- Upload multiple PDF resumes
- Extract and preprocess resume text using SpaCy
- Rank resumes based on job description similarity using TF-IDF + cosine similarity
- Download ranked results as a CSV report

Tools & Libraries
- Python
- Flask
- SpaCy
- PyMuPDF
- scikit-learn
- pandas

Installation

```bash
git clone https://github.com/yourusername/resume-ranker.git
cd resume-ranker
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Run the App

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.


Sample Job Description

Add your job description in `job_description.txt` before running the app.

