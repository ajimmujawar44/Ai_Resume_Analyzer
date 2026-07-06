import streamlit as st
import random
import re
import time
from pdf_reader import extract_text
from analyzer import analyze_resume
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.image("image/logo.png", width=350)
# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.main {
    padding: 2rem;
}

.stButton > button {
    width: 100%;
    background-color: #1E88E5;
    color: white;
    font-size: 18px;
    border-radius: 8px;
}

.stDownloadButton > button {
    width: 100%;
    font-size: 17px;
    border-radius: 8px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.title("📄 AI Resume Analyzer")
st.subheader("Offline Resume Analysis using Ollama + LLM")

st.write("""
Upload your resume in **PDF format** and receive an AI-generated analysis including:

- ✅ Resume Summary
- ✅ Strengths
- ✅ Weaknesses
- ✅ Missing Skills
- ✅ ATS Suggestions
- ✅ Improvement Tips
""")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📌 About")

st.sidebar.info("""
This application analyzes resumes locally using **Ollama** and an LLM.

No data is uploaded to external servers.
""")

st.sidebar.markdown("### 🛠 Technologies Used")

st.sidebar.write("""
- Python
- Streamlit
- Ollama
- Gemma / Llama Models
- PDF Processing
""")

st.sidebar.markdown("### 👨‍💻 Developer")

st.sidebar.success("Ajim Mujawar")

st.markdown("## 💼 Job Description (Optional)")

job_description = st.text_area(
    "Paste Job Description Here",
    placeholder="Paste the company's job description...",
    height=180
)
# ----------------------------
# File Upload
# ----------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Resume (PDF)",
    type=["pdf"]
)

# ----------------------------
# Resume Analysis
# ----------------------------

if uploaded_file is not None:

    with st.spinner("📖 Reading Resume..."):
        resume = extract_text(uploaded_file)

    st.success("✅ Resume Loaded Successfully!")

    st.text_area(
        "Resume Preview",
        resume[:1500],
        height=250
    )

    # Analyze button INSIDE uploaded_file block
    if st.button("🚀 Analyze Resume"):

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.015)
            progress.progress(i + 1)

        result = analyze_resume(resume)

        progress.empty()

        # ---------- Clean Text ----------
        def clean_text(text):
            text = text.lower()
            text = re.sub(r'[^a-zA-Z0-9+# ]', ' ', text)
            return text

        resume_clean = clean_text(resume)
        jd_clean = clean_text(job_description)

        # ---------- Skill Matching ----------
        SKILLS = {
            "python","sql","excel","power bi","tableau",
            "pandas","numpy","matplotlib","seaborn",
            "scikit-learn","tensorflow","keras",
            "machine learning","deep learning",
            "flask","django","git","github",
            "aws","docker","kubernetes",
            "statistics","data analysis","data visualization",
            "mysql","mongodb","opencv","nlp",
            "feature engineering","data cleaning",
            "data preprocessing","linux","api","rest api"
        }

        resume_lower = resume.lower()
        jd_lower = job_description.lower()

        matched = []
        missing = []

        for skill in sorted(SKILLS):
            if skill in jd_lower:
                if skill in resume_lower:
                    matched.append(skill)
                else:
                    missing.append(skill)

        if len(matched) + len(missing) > 0:
            keyword_score = (len(matched) / (len(matched) + len(missing))) * 100
        else:
            keyword_score = 0

        # ---------- Cosine Similarity ----------
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_clean, jd_clean])

        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        similarity_score = similarity * 100

        # ---------- Final Score ----------
        score = int((keyword_score * 0.5) + (similarity_score * 0.5))
        score = min(score, 100)
        ats_score = min(score + 10, 100)

        st.success("✅ Analysis Completed Successfully!")

        st.markdown("## 📊 Analysis Report")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("📈 ATS Score", f"{ats_score}/100")
            st.progress(ats_score / 100)

        with col2:
            st.metric("🎯 Job Match", f"{score}%")
            st.progress(score / 100)

        st.markdown("---")

        st.subheader("✅ Matched Skills")

        if matched:
            for skill in matched:
                st.success(f"✅ {skill}")
        else:
            st.warning("No matching skills found.")

        st.markdown("---")

        st.subheader("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.error(f"❌ {skill}")
        else:
            st.success("Excellent! No important skills are missing.")

        st.markdown("---")

        st.subheader("🤖 AI Resume Analysis")
        st.markdown(result)

        report = f"""
===============================
        ATS RESUME REPORT
===============================

ATS Score : {ats_score}/100

Job Match : {score}%

Matched Skills:
{', '.join(matched) if matched else 'None'}

Missing Skills:
{', '.join(missing) if missing else 'None'}

AI Resume Analysis:
{result}
"""

        st.download_button(
            "📥 Download Full Report",
            report,
            file_name="ATS_Report.txt",
            mime="text/plain"
        )
# ----------------------------
# Footer
# ----------------------------
st.markdown("---")

st.markdown("""
<div class="footer">
<h4>Created by <b>Ajim Mujawar</b></h4>
<p>AI Resume Analyzer | Streamlit | Ollama | Python</p>
</div>
""", unsafe_allow_html=True)