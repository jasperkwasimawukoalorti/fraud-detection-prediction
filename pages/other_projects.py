import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Other Projects", 
    layout="wide", 
    initial_sidebar_state="auto"
)

# --- Custom CSS for Catchy & Professional Look (Non-Dark Mode) ---
custom_css = """
<style>
    /* Cool Blue/Purple Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #e6e6ff 0%, #cc99ff 100%); /* Light Purple/Blue */
        color: #1a1a1a;
    }
    .main-content {
        padding: 30px;
        border-radius: 15px;
        background-color: #ffffff; /* White card */
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    h1 {
        color: #4a00e0; /* Deep Purple for main title */
        font-size: 2.5em;
        border-bottom: 3px solid #6600cc;
        padding-bottom: 10px;
    }
    .project-card {
        background-color: #f7f4ff;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        border: 1px solid #ddd;
        transition: all 0.3s ease;
    }
    .project-card:hover {
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        border-color: #6600cc;
    }
    .project-title {
        font-weight: 700;
        color: #4a00e0;
        font-size: 1.5em;
        margin-bottom: 5px;
    }
    .tech-pill {
        display: inline-block;
        background-color: #cc99ff;
        color: #4a00e0;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
        margin-right: 8px;
        margin-top: 10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Project Data (Mock professional data) ---
projects = [
    {
        "title": "Predictive Stock Market Analyst",
        "icon": "📈",
        "description": "Developed a time-series forecasting model (LSTM/ARIMA) to predict short-term stock price movements for tech sector companies. The system includes a web dashboard for real-time visualization of predictions and historical data.",
        "tech": ["Python", "TensorFlow", "Pandas", "Streamlit", "Time-Series Analysis"]
    },
    {
        "title": "Decentralized Voting System (Blockchain Simulation)",
        "icon": "🗳️",
        "description": "A proof-of-concept application demonstrating a secure, transparent, and immutable voting system using a simulated blockchain ledger. Focus on cryptographic hashing and distributed data integrity.",
        "tech": ["Python", "Cryptography", "Flask", "P2P Networking (Simulated)"]
    },
    {
        "title": "E-Commerce Recommendation Engine",
        "icon": "🛍️",
        "description": "Built a collaborative filtering and content-based recommendation engine for an online retail platform. Improved user engagement metrics by 15% in simulation through personalized product suggestions.",
        "tech": ["Python", "Scikit-learn", "Collaborative Filtering", "SQLAlchemy", "Jupyter"]
    },
]

# --- Content ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.title("✨ Other Capstone Projects & Initiatives")
st.markdown("""
<p style="font-size: 1.1em; margin-bottom: 20px;">
    In addition to the Fraud Detection System, our group has actively engaged in high-impact projects that demonstrate proficiency across various domains of modern technology and data science.
</p>
""", unsafe_allow_html=True)

for project in projects:
    st.markdown(f"""
    <div class="project-card">
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <span style="font-size: 2em; margin-right: 15px;">{project['icon']}</span>
            <span class="project-title">{project['title']}</span>
        </div>
        <p>{project['description']}</p>
        <p style="font-weight: 600; margin-top: 15px;">Key Technologies:</p>
        <div style="margin-top: 5px;">
            {''.join(f'<span class="tech-pill">{t}</span>' for t in project['tech'])}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
