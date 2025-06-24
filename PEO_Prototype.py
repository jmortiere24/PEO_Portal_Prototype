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

    # --- Three Tiles Across the Top ---
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80", use_column_width=True)
        st.markdown("#### OneDigital PEO Solutions")
        st.write("Discover the difference of partnering with OneDigital for your business success.")
        st.markdown(
            '<a href="https://www.onedigital.com/solutions/peo/" target="_blank">'
            '<button style="background-color:#004B49;color:white;padding:0.5rem 1.5rem;border:none;border-radius:6px;font-weight:600;">Learn More</button>'
            '</a>',
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80", use_column_width=True)
        st.markdown("#### On-Demand Webinar")
        st.write("Watch our on-demand webinar to help you weigh your options.")
        st.markdown(
            '<a href="https://event.on24.com/wcc/r/4248893/54A1D7E492C40AF5FEC8DF35C6D2918F?partnerref=peolp" target="_blank">'
            '<button style="background-color:#004B49;color:white;padding:0.5rem 1.5rem;border:none;border-radius:6px;font-weight:600;">Watch Now</button>'
            '</a>',
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80", use_column_width=True)
        st.markdown("#### Contact OneDigital PEO")
        st.write("Connect with our team of fierce advocates for your business.")
        st.markdown(
            '<a href="https://www.onedigital.com/solutions/peo/#Contact" target="_blank">'
            '<button style="background-color:#004B49;color:white;padding:0.5rem 1.5rem;border:none;border-radius:6px;font-weight:600;">Contact Us</button>'
            '</a>',
            unsafe_allow_html=True
        )
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
