import streamlit as st
import os
from PIL import Image, ExifTags
import base64  # Import base64 for encoding images


# Title
st.title("Analytical Chemistry E-Portfolio")

# Sidebar Selector
st.sidebar.title("Dashboard Selector")
view_option = st.sidebar.radio(
    "Choose what to view:",
    ["Our Team", "Course Introduction", "Lecturer Information", "Mindmap", "Self Reflection", "Extra Information"]
)

# Team Photo and Name
if view_option == "Our Team":
    st.header("Our Team")
    
    # Team Members images path handling
    team_img_path = [
        "Members Photo/3.jpeg",
        "Members Photo/1.jpg",
        "Members Photo/2.jpeg",
        "Members Photo/4.jpg",
        "Members Photo/5.jpeg"
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
    st.write("This course is a required component of core discipline in Chemical Engineering profession.  It is designed to equip engineers with the fundamental of analytical chemistry.  This course will help Engineers to take up challenges in analyzing and evaluating samples in chemical industries. ")
    selected_chapter = st.selectbox("Select a chapter to view Notes", 
                                ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", 
                                 "Chapter 5", "Chapter 6", "Chapter 7", "Chapter 8" , "Chapter 9"], 
                                index=0)
    
    pdf_file = f"Notes/Chapter_{selected_chapter.split(' ')[1]}.pdf"
    
    if os.path.exists(pdf_file):
        st.subheader(selected_chapter)
        
        if hasattr(st, "pdf_viewer"):
            st.pdf_viewer(pdf_file)
        else:
            st.warning("PDF viewer not supported in your Streamlit version. Please download the file instead.")
        
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Download PDF", data=pdf, file_name=f"Chapter_{selected_chapter.split(' ')[1]}.pdf", mime="application/pdf")
    else:
        st.error("PDF not found. Please check the file name and directory.")


# Lecturer Information
elif view_option == "Lecturer Information":
    st.header("Lecturer Information")
    
    lecturer_img_path = "Members Photo/drhakim.1.jpg"
    lecturer_img_path_1 = "Members Photo/drhakim2.jpg"

    if os.path.exists(lecturer_img_path):
        st.write("An Outstanding Educator, Researcher, and Innovator")
        lecturer_img = Image.open(lecturer_img_path)
        st.image(lecturer_img, caption="Lecturer: Ts. ChM. Dr. Mohd Dzul Hakim Wirzal",  use_container_width=True)
    else:
        st.error("Error: Lecturer image not found. Please check the file path.")
    
    st.write("Ts. ChM. Dr. Mohd Dzul Hakim Wirzal is a highly esteemed academic and researcher in the field of chemical engineering. As a Senior Lecturer at the Chemical Engineering Department of Universiti Teknologi PETRONAS (UTP) and a key researcher at the Centre of Research in Ionic Liquids (CORIL), his contributions to academia, research, and industrial collaboration are truly commendable. His expertise spans multiple advanced fields, including advanced oxidation processes, ionic liquids, hydrogen production, nanofiber membranes, and rare earth element (REE) separation and purification. His groundbreaking research focuses on the extraction and separation of rare earth elements, utilizing innovative approaches such as advanced leaching agents, supported liquid membranes, ion-exchange resins, and electrochemical processes. These research endeavors address the increasing global demand for REEs in high-tech industries while promoting sustainable resource management.")
    st.write("Dr. Hakim's dedication to advancing chemical engineering is evident through his extensive research portfolio, which has secured more than RM12 million in research funding. He has led numerous high-impact studies that bridge academic advancements with practical, real-world applications. His research excellence is further reflected in his 112+ published scientific papers, accumulating nearly 2,000 citations with an impressive h-index of 26. These achievements underscore his significant contributions to knowledge creation and technological innovation within the chemical engineering domain.")
    st.write("In recognition of his exceptional work, Dr. Hakim has been honored with numerous prestigious awards and accolades. He was recently awarded an Honorary Professorship from Karshi Engineering-Economics Institute, Uzbekistan (2024) and has been invited as a Fellow Teacher under the ERASMUS Grant at UCBL, France, and Oita Kosen, Japan. His commitment to both research and education has earned him multiple Gold Awards for Research Grants (2022, 2024) and Gold and Silver Medals for teaching innovations (2020). Furthermore, his contributions to student development were recognized with the Outstanding Student Development Award (2023), solidifying his impact on shaping future engineers and researchers.")
    if os.path.exists(lecturer_img_path_1):
        lecturer_img = Image.open(lecturer_img_path_1)
        st.image(lecturer_img, use_container_width=True)
    st.write("Dr. Hakim is also highly regarded for his international collaborations, working closely with renowned institutions such as NTNU (Norway), USP (Brazil), PRSB, UCBL (France), UCLL (Belgium), and KEEI (Uzbekistan). His active involvement in cross-border research and academic exchange programs has significantly contributed to scientific knowledge, technological advancements, and global cooperation in chemical engineering. ")
    st.write("Beyond his research and academic pursuits, Dr. Hakim plays a crucial role in mentoring and guiding students, inspiring them to excel in their respective fields. His ability to bridge theoretical knowledge with industrial applications makes him a highly respected figure among both students and fellow academics. His passion for research, education, and innovation continues to drive progress in chemical engineering, making a lasting impact on both the academic community and the industry. ")
    st.write("A true inspiration and a remarkable leader in the field, Dr. Hakim’s unwavering dedication to excellence sets an outstanding example for aspiring engineers and researchers worldwide  ")
    
# Mindmap Section
elif view_option == "Mindmap":
    st.header("Mindmap")
    selected_person = st.selectbox("Select Member", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
           
    # Loop through all chapters and display their images
    for chapter in range(1, 10):  # Assuming there are 9 chapters
        image_file = f"{selected_person}/Ch{chapter}_{selected_person}.jpg"
        
        if os.path.exists(image_file):
            st.subheader(f"Chapter {chapter}")
            # Encode the image file to base64
            with open(image_file, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode()

            # Apply the centered-image style by wrapping the image in a div with the class
            st.markdown(
                f"""
                <div class="centered-image">
                    <img src="data:image/jpeg;base64,{encoded_image}" alt="Mindmap for Chapter {chapter} by {selected_person}" style="width:100%;">
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning(f"Mindmap for Chapter {chapter} by {selected_person} is not available.")

# Self Reflection Section
elif view_option == "Self Reflection":
    st.header("Self Reflection")
    selected_person = st.selectbox("Select a person to view reflection", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
    
    pdf_file = f"Reflections/reflection_{selected_person}.pdf"
    reflection_image = f"Reflections/reflection_{selected_person}.jpg"
    
    if os.path.exists(pdf_file):
        # Display PDF using Streamlit's built-in PDF viewer
        st.subheader(f"Reflection by {selected_person}")
        st.write("You can view the reflection below:")

        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Download PDF", data=pdf, file_name=f"reflection_{selected_person}.pdf", mime="application/pdf")
    
    else:
        st.warning(f"Reflection PDF for {selected_person} is not available yet.")
    
    # Display reflection image if available
    if os.path.exists(reflection_image):
        st.write("### View PDF:")
        st.image(reflection_image, caption=f"Reflection by {selected_person}", use_container_width=True)
    else:
        st.warning(f"Reflection PDF for {selected_person} is not available.")
elif view_option == "Extra Information":
    st.write("Do you know how Analytical Instrument works?")
    st.markdown(" Gas Chromotography In Industry")
    st.video('https://youtu.be/q-N4fSSz3ME?si=GJTfq5md3G0fiK_y')
    st.markdown("High Liquid Performance Chromotograph")
    st.video('https://youtu.be/9ZqL4MOWAi8?si=o8g7mMWniBGtJkMc')
    st.markdown('Do you know how to read IR Spectroscopy?')
    st.video('https://youtu.be/WTmj_9VT5oE?si=0v6m1A6CA9c6XRUU')
    st.markdown(" Atomic Absorption Spectroscopy")
    st.video('https://youtu.be/miKyZm_vI_g?si=mUOT50boMPBThzUF')
    st.markdown(" Atomic Emmision Spectroscopy")
    st.video('https://youtu.be/avFm5M9TiVE?si=XsjRumbf67M3089-')
    st.markdown("Atomic Fluorescence Spectroscopy")
    st.video("https://youtu.be/W9p6Y8IW89A?si=UpXJucanCAB3tllv")
