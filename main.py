import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

add_page_title() # By default this also adds indentation

# # Specify what pages should be shown in the sidebar, and what their titles and icons
# # should be
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Section(name="For Tutors Only", icon="🎈️"),
        Page("pages/tutor_registration.py", "Tutor Registration"),
        Page("pages/tutor_availability.py", "Tutor Availability Update"),
        
        Section(name="For Students Only", icon="💪"),    
        Page("pages/student_registration.py", "Student Registration"),
        Page("pages/tutor_signup.py", "Tutor Sign Up"),
    ]
)

st.write("# Welcome to AAH Tutor Scheduler Website! 👋")

st.markdown(
    """
    
    **👈 Select the option from the left sidebar to proceed!
    ### Tutors
    - Please complete your registration first before participating in tutor program!
    - You must send us the email with photo ID (i.e. student ID) to complete the registration
    ### Students
    - Please complete your registration (Student registration) before signing up for the tutor!
    - Currently you can book up to 2 tutor sessions per week
"""
)
