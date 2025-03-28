import streamlit as st
import os
from PIL import Image

# Title
st.title("Team Project Website")

# Sidebar Selector
st.sidebar.title("Dashboard Selector")
view_option = st.sidebar.radio(
    "Choose what to view:",
    ["Our Team", "Course Introduction", "Lecturer Information", "Mindmap", "Self Reflection", "Extra Categories"]
)

# Team Photo and Name
if view_option == "Our Team":
    st.header("Our Team")
    
    # Corrected path handling
    team_img_path = os.path.join("azhar.jpg")
    
    if os.path.exists(team_img_path):
        team_img = Image.open(team_img_path)
        st.image(team_img, caption="Our Team", use_column_width=True)
    else:
        st.error("Error: Team image not found. Please check the file path.")

    st.write("Team Members: Azhar, Suhayb, Hakimi, Humaira, Lydia")

# Course Introduction
elif view_option == "Course Introduction":
    st.header("Course Introduction")
    st.write("This course covers various topics in Process Instrumentation and Control, including theoretical and practical aspects of control systems.")

# Lecturer Information
elif view_option == "Lecturer Information":
    st.header("Lecturer Information")
    
    # Corrected path handling for lecturer image
    lecturer_img_path = "lecturer_photo.jpg"
    
    if os.path.exists(lecturer_img_path):
        lecturer_img = Image.open(lecturer_img_path)
        st.image(lecturer_img, caption="Lecturer: Dr. XYZ", use_column_width=True)
    else:
        st.error("Error: Lecturer image not found. Please check the file path.")
    
    st.write("Lecturer: Dr. XYZ")

# Mindmap Section
elif view_option == "Mindmap":
    st.header("Mindmap")
    selected_chapter = st.selectbox("Select Chapter", [f"Chapter {i}" for i in range(1, 9)])
    selected_person = st.selectbox("Select Member", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
    
    pdf_file = f"mindmap_{selected_chapter}_{selected_person}.pdf"
    
    if os.path.exists(pdf_file):
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Download Mindmap PDF", data=pdf, file_name=pdf_file, mime="application/pdf")
    else:
        st.warning(f"Mindmap for {selected_chapter} by {selected_person} is not available yet.")

# Self Reflection Section
elif view_option == "Self Reflection":
    st.header("Self Reflection")
    selected_person = st.selectbox("Select a person to view reflection", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
    
    pdf_file = f"reflection_{selected_person}.pdf"
    
    if os.path.exists(pdf_file):
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Download Reflection PDF", data=pdf, file_name=pdf_file, mime="application/pdf")
    else:
        st.warning(f"Reflection for {selected_person} is not available yet.")
