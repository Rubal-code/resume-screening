# Resume Screening

An intelligent resume screening system powered by machine learning, designed to automatically classify and evaluate resumes based on predefined criteria using advanced NLP techniques.

## 🎯 Overview

Resume Screening is a production-ready application that leverages machine learning and natural language processing to automate the resume evaluation process. It provides REST APIs for both text and PDF-based resume analysis, enabling organizations to streamline their recruitment workflows and reduce manual screening efforts.

## ✨ Features

- **Dual Input Methods**: Analyze resumes from raw text or PDF files
- **ML-Powered Classification**: Advanced machine learning model trained for accurate resume categorization
- **PDF Processing**: Direct PDF file upload and extraction for seamless document handling
- **Text Preprocessing**: Intelligent text cleaning with lemmatization, stopword removal, and noise filtering
- **Fast API Framework**: High-performance REST API built with FastAPI
- **Scalable Architecture**: Modular design supporting easy deployment and scaling

## 🏗️ Project Structure

```
resume-screening/
├── app/
│   ├── main.py              # FastAPI application & endpoints
│   └── __init__.py
├── model/
│   ├── resume_model.pkl     # Trained classification model
│   └── tfidf.pkl            # TF-IDF vectorizer
├── data/                    # Dataset directory
├── notebooks/               # Jupyter notebooks for experimentation
├── frontend/                # Frontend application (if applicable)
├── requirements.txt         # Python dependencies
└── start.sh                 # Startup script
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | FastAPI |
| **Server** | Uvicorn |
| **ML/NLP** | scikit-learn, NLTK |
| **Data Processing** | NumPy, Pandas |
| **PDF Processing** | PyPDF2 |
| **Serialization** | joblib |

## 📋 Requirements

- Python 3.8+
- All dependencies listed in `requirements.txt`

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Rubal-code/resume-screening.git
cd resume-screening
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the API Server
```bash
bash start.sh
```

Or manually:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### 1. Health Check
```http
GET /
```

**Response:**
```json
{
  "message": "Resume Analyzer API is running"
}
```

### 2. Classify from Text
```http
POST /predict-text
```

**Parameters:**
- `text` (string, required): Resume content as text

**Example:**
```bash
curl -X POST "http://localhost:8000/predict-text?text=John%20Doe%20Software%20Engineer..."
```

**Response:**
```json
{
  "prediction": [1]
}
```

### 3. Classify from PDF
```http
POST /predict-pdf
```

**Parameters:**
- `file` (file, required): PDF resume file

**Example:**
```bash
curl -X POST "http://localhost:8000/predict-pdf" \
  -F "file=@resume.pdf"
```

**Response:**
```json
{
  "filename": "resume.pdf",
  "prediction": [1]
}
```

## 🔧 Text Preprocessing Pipeline

The application employs a sophisticated text preprocessing approach:

1. **URL Removal**: Strips HTTP/HTTPS links
2. **Special Character Removal**: Keeps only alphabetic characters
3. **Lowercasing**: Converts to lowercase for uniformity
4. **Stopword Removal**: Eliminates common English words
5. **Lemmatization**: Reduces words to base forms using WordNetLemmatizer
6. **Vectorization**: Converts text to numerical features using TF-IDF

## 📊 Model Details

- **ML Algorithm**: Classification model trained with scikit-learn
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Input**: Preprocessed resume text
- **Output**: Binary/Multi-class classification predictions

## 🚀 Deployment

### Docker (Recommended)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r resume-screening/requirements.txt
CMD ["bash", "resume-screening/start.sh"]
```

Build and run:
```bash
docker build -t resume-screening .
docker run -p 8000:8000 resume-screening
```

### Production Considerations
- Use environment variables for configuration
- Implement proper error handling and logging
- Add authentication for API security
- Use process managers like Gunicorn or Supervisor
- Set up monitoring and alerting

## 📈 Performance Optimization

- Model is loaded once at startup for efficiency
- Vectorizer cache for repeated predictions
- Async request handling with FastAPI
- Minimal preprocessing overhead

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature suggestions.

## 📝 License

This project is available for educational and commercial use.

## 👤 Author

Created and maintained by [@Rubal-code](https://github.com/Rubal-code)

## 📞 Support

For issues, questions, or suggestions, please open an issue on [GitHub Issues](https://github.com/Rubal-code/resume-screening/issues).

---

**Last Updated:** 2026-04-25 17:07:30  
**Repository:** https://github.com/Rubal-code/resume-screening