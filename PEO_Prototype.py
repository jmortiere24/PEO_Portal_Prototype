import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="OneDigital Client Portal", layout="wide")

# --- CUSTOM CSS ---
# Using markdown for CSS injection as file creation is restricted.
st.markdown("""
<style>
    /* Remove Streamlit's default padding on the main block container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    /* Main page style */
    #root {
        background-color: #F0F2F6;
    }
    /* Cards */
    .css-1r6slb0, .css-12ttj6m {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 10px;
        padding: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    /* General button styling */
    .stButton>button {
        background-color: #004B49; /* Dark Teal */
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        cursor: pointer;
        font-weight: bold;
        width: 100%; /* Make buttons full width of their container */
    }
    .stButton>button:hover {
        background-color: #006F6B; /* Slightly lighter teal for hover */
        color: white;
    }
    /* Special button style for the main call to action */
    .stButton>button[kind="secondary"] {
         width: auto !important; /* Override full-width for specific buttons if needed */
    }

</style>
""", unsafe_allow_html=True)


# --- TOP NAVIGATION ---
# Using icons from: https://icons.getbootstrap.com/
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


# --- PAGE CONTENT ---

def dashboard():
    # Using a public URL for the logo for portability
    st.image("https://storage.googleapis.com/markprompt-images/onedigital_logo.png", width=200)
    st.write("") # Spacer

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader("FEATURED")
        st.markdown("## Using a Mortgage to your Advantage")
        st.write("Choosing the Right Mortgage for Your Future Choosing the right mortgage isn’t just about securing a loan – it’s locking in a commitment that will facilitate your homeownership a...")
        if st.button("Watch Now ➔", type="secondary"):
            st.info("Video player would be here.")

        # Using a public URL for the image for portability
        st.image("https://storage.googleapis.com/markprompt-images/mortgage_journey.png")

        st.write("---")
        st.markdown("### Tools & Resources")
        
        row1_col1, row1_col2 = st.columns(2, gap="large")
        with row1_col1:
            st.subheader("Financial Academy")
            st.write("Empowering financial wellness through webinars, articles, and resources.")
            st.button("Access Financial Academy Resources Here", key="fin_academy")

        with row1_col2:
            st.subheader("Tools & Calculators")
            st.button("Determine Your Net Worth", key="tool1")
            st.button("How Can Systematic Investing Benefit You?", key="tool2")
            st.button("What Is Your Life Expectancy?", key="tool3")


    with col2:
        # Advisor Card
        st.subheader("Your Advisor Team")
        st.write("**Taylor Scott**")
        st.write("*Payroll & HR Specialist*")
        st.write("✉️ taylor.scott@onedigital.com")
        st.write("📞 (123) 456-7890")
        if st.button("Schedule Consultation", key="advisor_contact"):
            st.success("Contact form would appear here.")
        
        st.write("---")

        # Other tools/cards
        st.subheader("Benefit Enrollment")
        # Using a public URL for the image for portability
        st.image("https://storage.googleapis.com/markprompt-images/the_standard_logo.png", width=150)
        st.button("Enroll Here", key="enroll")

        st.write("---")

        st.subheader("Retirement Plan")
        # Using a public URL for the image for portability
        st.image("https://storage.googleapis.com/markprompt-images/401k_baynum.png", width=200)
        st.button("View Your Retirement Plan Highlights", key="401k")


def hr_tools():
    st.title("HR Tools")
    st.write("Access payroll and employee management tools here. (Placeholder)")

def compliance_hub():
    st.title("Compliance Hub")
    st.write("Find the latest HR, tax, and labor law requirements specific to your state. Select a state to view resources and regulations that apply to your business.")
    st.write("(Interactive US map and state-specific info would go here.)")
    st.write("Example: Select 'Alabama' to see compliance topics like Emergency Response Leave, Family and Medical Leave, etc.")

def case_management():
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


# --- ROUTING ---
if selected == "Dashboard":
    dashboard()
elif selected == "HR Tools":
    hr_tools()
elif selected == "Compliance Hub":
    compliance_hub()
elif selected == "Case Management":
    case_management()