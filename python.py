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
    
 # Team Members images path handling
    team_img_path = [
        "Members Photo/azhar.JPG",
    "Members Photo/1.jpg",
    "Members Photo/2.jpg",
    "Members Photo/3.jpg",
    "Members Photo/4.jpg"
    ]
    # Team member names
    team_member_names = ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"]
    
    # Create 5 columns
    cols = st.columns(5)
    
    # Loop through each column and display the corresponding image and name
    for col, img_path, name in zip(cols, team_img_path, team_member_names):
        if os.path.exists(img_path):
            img = Image.open(img_path)
            col.image(img, caption=name, use_container_width=True)
        else:
            col.error(f"Image for {name} not found.")

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
        lecturer_img = Image.open(azhar.JPG)
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
