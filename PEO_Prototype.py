import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="OneDigital Client Portal", layout="wide")

# --- CUSTOM CSS for cards/tiles ---
st.markdown("""
<style>
.card {
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 12px 0 rgba(0,0,0,0.07);
    padding: 2rem 2rem 1.5rem 2rem;
    margin-bottom: 2rem;
}
.card-header {
    font-size: 1.2rem;
    font-weight: 700;
    color: #004B49;
    margin-bottom: 0.5rem;
}
.stButton>button {
    background-color: #004B49;
    color: white;
    border-radius: 6px;
    padding: 0.5rem 1.5rem;
    border: none;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.stButton>button:hover {
    background-color: #006F6B;
}
</style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Dashboard", "HR Tools", "Compliance Hub", "Case Management"],
    icons=["speedometer2", "wrench-adjustable", "shield-check", "envelope-paper"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FFFFFF", "border-bottom": "1px solid #E0E0E0"},
        "icon": {"color": "#004B49", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px",
            "font-weight": "500",
            "color": "#333333",
            "text-align": "center",
            "margin": "0px 10px",
            "--hover-color": "#F0F2F6",
        },
        "nav-link-selected": {"background-color": "#E0E0E0", "color": "#004B49", "font-weight": "bold"},
    },
)

def dashboard():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/OneDigital_Logo.png", width=180)
    st.markdown("</div>", unsafe_allow_html=True)

    col_main, col_side = st.columns([2, 1], gap="large")

    with col_main:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">FEATURED</div>', unsafe_allow_html=True)
        st.markdown("### Using a Mortgage to your Advantage")
        st.write("Choosing the right mortgage isn’t just about securing a loan – it’s locking in a commitment that will facilitate your homeownership a...")
        st.button("Watch Now ➔", type="secondary")
        st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        col_tools, col_calc = st.columns(2, gap="large")
        with col_tools:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-header">Financial Academy</div>', unsafe_allow_html=True)
            st.write("Empowering financial wellness through webinars, articles, and resources.")
            st.button("Access Financial Academy Resources Here", key="fin_academy")
            st.markdown("</div>", unsafe_allow_html=True)
        with col_calc:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-header">Tools & Calculators</div>', unsafe_allow_html=True)
            st.button("Determine Your Net Worth", key="tool1")
            st.button("How Can Systematic Investing Benefit You?", key="tool2")
            st.button("What Is Your Life Expectancy?", key="tool3")
            st.markdown("</div>", unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Your Advisor Team</div>', unsafe_allow_html=True)
        st.write("**Taylor Scott**")
        st.write("*Payroll & HR Specialist*")
        st.write("✉️ taylor.scott@onedigital.com")
        st.write("📞 (123) 456-7890")
        st.button("Schedule Consultation", key="advisor_contact")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Benefit Enrollment</div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80", width=120)
        st.button("Enroll Here", key="enroll")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Retirement Plan</div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80", width=150)
        st.button("View Your Retirement Plan Highlights", key="401k")
        st.markdown("</div>", unsafe_allow_html=True)

def hr_tools():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("HR Tools")
    st.write("Access payroll and employee management tools here. (Placeholder)")
    st.markdown("</div>", unsafe_allow_html=True)

def compliance_hub():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("Compliance Hub")
    st.write("Find the latest HR, tax, and labor law requirements specific to your state. Select a state to view resources and regulations that apply to your business.")
    st.write("(Interactive US map and state-specific info would go here.)")
    st.write("Example: Select 'Alabama' to see compliance topics like Emergency Response Leave, Family and Medical Leave, etc.")
    st.markdown("</div>", unsafe_allow_html=True)

def case_management():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("Submit a Request")
    st.write("Use this form to request support from the OneDigital PEO team. Your case will be routed based on the selected request type.")
    request_types = [
        "Plan/Employer", "Complete Retirement Solution Implementation", "Education Meeting", "Fund Change", "Internal VM Changes", "Internal/Compliance", "Marketing Services", "Onboarding/Terminations", "Participant", "RPS Client Conversions", "Trade Error or Incident", "VM Prospect Paperwork", "VM Service Request"
    ]
    request_type = st.selectbox("Request Type", request_types)
    contact_name = st.text_input("Contact Name")
    email = st.text_input("Email")
    description = st.text_area("Description")
    if st.button("Submit"):
        st.success("Request submitted!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- ROUTING ---
if selected == "Dashboard":
    dashboard()
elif selected == "HR Tools":
    hr_tools()
elif selected == "Compliance Hub":
    compliance_hub()
elif selected == "Case Management":
    case_management()
