# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Python**, **Streamlit**, and **Ollama**. The application analyzes resumes in PDF format, provides ATS-friendly feedback, matches resumes against a job description, and generates suggestions for improvement—all while running locally.

---

## 🚀 Features

* 📄 Upload resumes in PDF format
* 🤖 AI-powered resume analysis using Ollama
* 📈 ATS Score estimation
* 🎯 Job Description matching
* 💡 Suggestions to improve resume quality
* 📥 Download the analysis report
* 🔒 Runs locally for better privacy

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* PDF Processing
* Large Language Models (DeepSeek / Qwen)

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── image/
│   └── logo.png
├── app.py
├── analyzer.py
├── pdf_reader.py
├── prompts.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ajimmujawar44/ai-resume-analyzer.git
```

Move into the project folder:

```bash
cd ai-resume-analyzer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama from the official website:

https://ollama.com

Pull a supported model, for example:

```bash
ollama pull deepseek-r1:1.5b
```

or

```bash
ollama pull qwen2.5:3b
```

Ensure the Ollama service is running before starting the application.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📊 How It Works

1. Upload a PDF resume.
2. (Optional) Paste a Job Description.
3. Click **Analyze Resume**.
4. The AI evaluates the resume and provides:

   * Resume summary
   * ATS Score
   * Job match score
   * Strengths
   * Weaknesses
   * Missing skills
   * Suggestions for improvement
5. Download the generated report.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

* Home Page
* Resume Upload
* Analysis Report
* ATS Score
* Job Match Result

---

## 📌 Future Improvements

* Resume keyword highlighting
* Support for DOCX resumes
* Multiple AI model selection
* PDF report generation
* Skill visualization charts
* Multi-language support

---

## 👨‍💻 Author

**Ajim Mujawar**

GitHub: https://github.com/ajimmujawar44

---

## 📄 License

This project is developed for learning and portfolio purposes.
