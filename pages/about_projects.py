import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="About Us & Project", 
    layout="wide", 
    initial_sidebar_state="auto"
)

# --- Custom CSS for Catchy & Professional Look (Non-Dark Mode) ---
custom_css = """
<style>
    /* Gradient Background for a catchy, non-dark look */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #e0e8f0 100%);
        color: #1a1a1a;
    }
    /* Main Content Styling (simulating a white card on the gradient) */
    .main-content {
        padding: 30px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #004d99; /* Deep blue for titles */
        border-bottom: 3px solid #FF4B4B; /* Red accent divider */
        padding-bottom: 5px;
        margin-top: 30px;
    }
    .member-card {
        background-color: #f4f7fa;
        border-left: 5px solid #004d99;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    .member-name {
        font-weight: bold;
        color: #1a1a1a;
        font-size: 1.1em;
    }
    /* Responsive grid for members */
    .st-emotion-cache-c3i1z1 { /* Targeting Streamlit columns container */
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- Content ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.title("📚 Capstone Project Overview")

st.header("The Machine Learning Fraud Detection System")
st.markdown("""
This project showcases the development and deployment of a robust, real-time fraud detection system. Leveraging the power of Machine Learning, specifically the **Random Forest Classifier**, the application analyzes core financial transaction features (like transaction type, amount, and balance changes) to instantly predict the probability of a transaction being fraudulent.

* **Objective:** To mitigate financial risk by providing financial institutions with an accurate, scalable, and instant anomaly detection tool.
* **Technology Stack:** Python, Pandas, NumPy, Scikit-learn (Random Forest), and Streamlit for deployment.
* **Performance:** The trained model achieved a **high accuracy** rate in identifying fraudulent transactions, demonstrating the effectiveness of ML in enhancing financial security.
""")

st.header("Group Members and Contact Information")

# Group member data (using names from the presentation file)
group_members = [
    ("Abiba Fuseini", "abiba.f@gmail.com", "+233 24 360 9090"),
    ("Joe Louis Amankwah", "joe.louis@gmail.com", "+233 54 463 6258"),
    ("Jasper Kwasi Mawuko Alorti", "jasper.alorti@yahoo.com.com", "+233 20 859 8037"),
    ("Samson Kotei Kotey", "samson.kotei@gmail.com", "+233 24 655 8137"),
    ("Daniel Aryeetey", "daniel.aryeetey@gmail.com", "+233 27 225 7131"),
    ("Joseph Asante", "joseph.asante@gmail.com", "+233 20 887 6365"),
    ("Ibrahim Salma Niina", "salma.niina@gmail.com", "+233 20 919 4684"),
    ("Henry Adigbe", "henry.adigbe@gmail.com", "+233 54 086 6811"),
    ("Isaac Agyei", "isaac.agyei@gmail.com", "+233 55 269 4080"),
    ("Nadia Nanor", "nadia.nanor@gmail.com", "+233 54 989 8267"),
]

# Display members in a responsive layout
cols = st.columns(2) # Two columns per row

for i, (name, email, phone) in enumerate(group_members):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="member-card">
            <p class="member-name">{name}</p>
            <p>📧 {email}</p>
            <p>📞 {phone}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.caption("Note: Placeholder contact numbers are used for demonstration.")
