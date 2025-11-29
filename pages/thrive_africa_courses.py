import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Thrive Africa Courses", 
    layout="wide", 
    initial_sidebar_state="auto"
)

# --- Custom CSS for Catchy & Professional Look (Non-Dark Mode) ---
custom_css = """
<style>
    /* Vibrant Background */
    .stApp {
        background: linear-gradient(135deg, #BBBBBB 0%, #FF69B4 100%); /* Pink to Light Pink */
        color: #333333;
    }
    .main-content {
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff; /* White card */
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    h1 {
        color: #B8860B; /* Darker Gold for main title */
        font-size: 8.5em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .course-card {
        background-color: #f7f7f7;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #FF8C00; /* Orange accent */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        height: 100%; /* Ensure uniform height in grid */
    }
    .course-card:hover {
        transform: translateY(-5px);
    }
    .course-title {
        font-weight: bold;
        color: #1a1a1a;
        font-size: 2.0em;
        margin-bottom: 10px;
    }
    .course-icon {
        font-size: 3em;
        margin-right: 10px;
        color: #FF8C00;
    }
    .thrive-link {
        color: #004d99;
        font-weight: bold;
        text-decoration: underline;
    }
    /* Responsive grid for courses */
    .course-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Course Data ---
courses = [
    {"name": "Generative AI Engineering", "icon": "🧠", "description": "Mastering large language models, prompt engineering, and building cutting-edge AI applications."},
    {"name": "Cybersecurity Specialist", "icon": "🔒", "description": "Protecting systems, networks, and data from threats. Includes penetration testing and security architecture."},
    {"name": "Cloud Computing (AWS/Azure/GCP)", "icon": "☁️", "description": "Developing, deploying, and managing applications in the cloud environment."},
    {"name": "Data Analytics & Visualization", "icon": "📊", "description": "Transforming raw data into actionable insights using tools like Python, R, and Tableau/Power BI."},
    {"name": "Frontend Engineering", "icon": "💻", "description": "Building responsive and dynamic user interfaces using modern frameworks like React and Vue."},
    {"name": "Backend Engineering", "icon": "⚙️", "description": "Developing robust server-side logic, APIs, and database systems (includes **Machine Learning** deployment focus)."},
    {"name": "Machine Learning Foundations", "icon": "🔬", "description": "Core concepts, model development, evaluation, and deployment of predictive algorithms."},
]

# --- Content ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.title("🚀 Professional Courses by Thrive Africa")
st.markdown("""
<p style="font-size: 2.1em;">
    Thrive Africa is dedicated to empowering the next generation of tech leaders. Explore our career-defining professional courses designed to equip you with in-demand skills in the digital economy.
</p>
""", unsafe_allow_html=True)

# Link to Thrive Africa
st.markdown(f"""
<p style="margin-top: 20px;"> 
    🔗 **Visit the Thrive Africa Website:** <a class="thrive-link" href="https://thriveafrica.co/" target="_blank">thriveafrica.co</a>
</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("Course Offerings")

# Display courses in a responsive grid
st.markdown('<div class="course-grid">', unsafe_allow_html=True)
for course in courses:
    st.markdown(f"""
    <div class="course-card">
        <span class="course-icon">{course['icon']}</span>
        <span class="course-title">{course['name']}</span>
        <p>{course['description']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
