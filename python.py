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
        "Members Photo/1.jpg",
        "Members Photo/1.jpg",
        "Members Photo/1.jpg",
        "Members Photo/2.jpg",
    ]
    # Team member names
    team_member_names = ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia", "Ghost"]
    
    # First row: Azhar, Suhayb, Hakimi
    row1_cols = st.columns(3, gap="small")  # Create 3 columns for the first row
    for col, img_path, name in zip(row1_cols, team_img_path[:3], team_member_names[:3]):
        with col:
            if os.path.exists(img_path):
                # Display the image with a caption
                st.image(img_path, caption=f"**{name}**", use_container_width=True)
            else:
                # Display a placeholder for missing images
                st.error(f"Image for {name} not found.")

    # Second row: Humaira, ghost, Lydia
    row2_cols = st.columns(3, gap="small")  # Create 2 columns for the second row
    for col, img_path, name in zip(row2_cols, team_img_path[3:], team_member_names[3:]):
        with col:
            if os.path.exists(img_path):
                # Display the image with a caption
                st.image(img_path, caption=f"**{name}**", use_container_width=True)
            elif name == "Ghost":
                st.write("")
            else:
                # Display a placeholder for missing images
                st.error(f"Image for {name} not found.")

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
    
    # Select a person
    selected_person = st.selectbox("Select Member", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
    
    # Loop through all chapters and display their images
    for chapter in range(1, 10):  # Assuming there are 9 chapters
        image_file = f"Su/Ch{chapter}_{selected_person[0].upper()}.jpg"  # Use the first letter of the person's name
        
        if os.path.exists(image_file):
            st.subheader(f"Chapter {chapter}")
            st.image(image_file, caption=f"Mindmap for Chapter {chapter} by {selected_person}", use_container_width=True)
        else:
            st.warning(f"Mindmap for Chapter {chapter} by {selected_person} is not available.")

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
