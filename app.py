import streamlit as st
import random 
from pdf_reader import extract_text
from analyzer import analyze_resume

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
if st.button("🚀 Analyze Resume"):

    progress = st.progress(0)
    import time

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    result = analyze_resume(resume)
    progress.empty()

    resume_words = set(resume.lower().split())
    jd_words = set(job_description.lower().split())

    if len(jd_words) > 0:
        matched = resume_words.intersection(jd_words)
        score = int((len(matched) / len(jd_words)) * 100)
        score = min(score, 100)
    else:
        score = 0

    ats_score =  int(score * 0.9 + 10)

    progress.empty()

    st.success("✅ Analysis Completed Successfully!")

    st.markdown("## 📊 Analysis Report")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📈 ATS Score", f"{ats_score}/100")

    with col2:
        st.metric("🎯 Job Match", f"{score}%")

    st.markdown("---")

    st.markdown(result)

    st.download_button(
        "📥 Download Report",
        result,
        file_name="resume_analysis.txt",
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