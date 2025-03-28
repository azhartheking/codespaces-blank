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
    
    st.write("Lecturer: Ts. ChM. Dr. Mohd Dzul Hakim Wirzal is a highly esteemed academic and researcher in the field of chemical engineering. As a Senior Lecturer at the Chemical Engineering Department of Universiti Teknologi PETRONAS (UTP) and a key researcher at the Centre of Research in Ionic Liquids (CORIL), his contributions to academia, research, and industrial collaboration are truly commendable. His expertise spans multiple advanced fields, including advanced oxidation processes, ionic liquids, hydrogen production, nanofiber membranes, and rare earth element (REE) separation and purification. His groundbreaking research focuses on the extraction and separation of rare earth elements, utilizing innovative approaches such as advanced leaching agents, supported liquid membranes, ion-exchange resins, and electrochemical processes. These research endeavors address the increasing global demand for REEs in high-tech industries while promoting sustainable resource management.Dr. Hakim's dedication to advancing chemical engineering is evident through his extensive research portfolio, which has secured more than RM12 million in research funding. He has led numerous high-impact studies that bridge academic advancements with practical, real-world applications. His research excellence is further reflected in his 112+ published scientific papers, accumulating nearly 2,000 citations with an impressive h-index of 26. These achievements underscore his significant contributions to knowledge creation and technological innovation within the chemical engineering domain. In recognition of his exceptional work, Dr. Hakim has been honored with numerous prestigious awards and accolades. He was recently awarded an Honorary Professorship from Karshi Engineering-Economics Institute, Uzbekistan (2024) and has been invited as a Fellow Teacher under the ERASMUS Grant at UCBL, France, and Oita Kosen, Japan. His commitment to both research and education has earned him multiple Gold Awards for Research Grants (2022, 2024) and Gold and Silver Medals for teaching innovations (2020). Furthermore, his contributions to student development were recognized with the Outstanding Student Development Award (2023), solidifying his impact on shaping future engineers and researchers.  ")

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
