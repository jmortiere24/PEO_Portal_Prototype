import streamlit as st

st.set_page_config(page_title="OneDigital Client Portal", layout="wide")

# --- Custom CSS for a tight, modern nav bar and header ---
st.markdown("""
<style>
/* NAV BAR */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
div[data-testid="stHorizontalBlock"] > div {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
}
div[data-testid="stHorizontalBlock"] {
    background: #fff !important;
    border-bottom: 1px solid #e0e0e0 !important;
    margin-bottom: 0.5rem !important;
}
.st-emotion-cache-1v0mbdj {
    padding-top: 0.5rem !important;
}
.st-emotion-cache-1v0mbdj, .st-emotion-cache-1v0mbdj > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
.st-emotion-cache-1v0mbdj > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div {
    margin-bottom: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# --- NAV BAR (text only, compact) ---
nav = st.columns([1,1,1,1,8])
with nav[0]:
    st.markdown('<b>Dashboard</b>', unsafe_allow_html=True)
with nav[1]:
    st.markdown('Compliance Hub', unsafe_allow_html=True)
with nav[2]:
    st.markdown('Case Management', unsafe_allow_html=True)
with nav[3]:
    st.markdown('', unsafe_allow_html=True)
with nav[4]:
    st.markdown('', unsafe_allow_html=True)

# --- HEADER ---
st.markdown("### Hello Jane,")
st.write("Here's what we have for you today.")

# --- Your tiles/cards go here ---

def dashboard():
    # --- HEADER: Greeting left, logo right ---
    col_left, col_right = st.columns([3, 2])
    with col_left:
        st.markdown("## Hello Heather")
        st.write("Here's what we have for you today!")
    with col_right:
        st.image("onedigital_logo.PNG", width=220)

    # --- Three Large Boxed Tiles Across the Top ---
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            """
            <div class="card-tile">
                <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80" class="card-img"/>
                <div class="card-title">OneDigital PEO Solutions</div>
                <div class="card-desc">Discover the difference of partnering with OneDigital for your business success.</div>
                <a href="https://www.onedigital.com/solutions/peo/" target="_blank">
                    <button style="background-color:#004B49;color:white;padding:0.5rem 1.5rem;border:none;border-radius:6px;font-weight:600;">Learn More</button>
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card-tile">
                <img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80" class="card-img"/>
                <div class="card-title">On-Demand Webinar</div>
                <div class="card-desc">Watch our on-demand webinar to help you weigh your options.</div>
                <a href="https://event.on24.com/wcc/r/4248893/54A1D7E492C40AF5FEC8DF35C6D2918F?partnerref=peolp" target="_blank">
                    <button style="background-color:#004B49;color:white;padding:0.5rem 1.5rem;border:none;border-radius:6px;font-weight:600;">Watch Now</button>
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card-tile">
                <img src="https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80" class="card-img"/>
                <div class="card-title">Contact OneDigital PEO</div>
                <div class="card-desc">Connect with our team of fierce advocates for your business.</div>
                <a href="https://www.onedigital.com/solutions/peo/#Contact" target="_blank">
                    <button style="background-color:#004B49;color:white;padding:0.5rem 1.5rem;border:none;border-radius:6px;font-weight:600;">Contact Us</button>
                </a>
            </div>
            """, unsafe_allow_html=True
        )

def compliance_hub():
    st.markdown('<div class="card-tile">', unsafe_allow_html=True)
    st.title("Compliance Hub")
    st.write("Find the latest HR, tax, and labor law requirements specific to your state. Select a state to view resources and regulations that apply to your business.")
    st.write("(Interactive US map and state-specific info would go here.)")
    st.write("Example: Select 'Alabama' to see compliance topics like Emergency Response Leave, Family and Medical Leave, etc.")
    st.markdown("</div>", unsafe_allow_html=True)

def case_management():
    st.markdown('<div class="card-tile">', unsafe_allow_html=True)
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
elif selected == "Compliance Hub":
    compliance_hub()
elif selected == "Case Management":
    case_management()
