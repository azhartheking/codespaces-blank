import streamlit as st

# Title
st.title("Team Project Website")
from PIL import Image

# Sidebar Selector
st.sidebar.title("Dashboard Selector")
view_option = st.sidebar.radio("Choose what to view:", ["Our Team", "Course Introduction", "Lecturer Information", "Mindmap", "Self Reflection", "Extra Categories"])

# Team Photo and Name
if view_option == "Our Team":
    st.header("Our Team")
    team_img = Image.open("/workspaces/codespaces-blank/Members Photo/1.jpg")  # Replace with your image file path
    st.image(team_img, caption="Our Team", use_column_width=True)
    st.write("Team Members: Azhar, Suhayb, Hakimi, Humaira, Lydia")

# Course Introduction
elif view_option == "Course Introduction":
    st.header("Course Introduction")
    st.write("This course covers various topics in Process Instrumentation and Control, including theoretical and practical aspects of control systems.")

# Lecturer Information
elif view_option == "Lecturer Information":
    st.header("Lecturer Information")
    lecturer_img = Image.open("lecturer_photo.jpg")  # Replace with your image file path
    st.image(lecturer_img, caption="Lecturer: Dr. XYZ", use_column_width=True)
    st.write("Lecturer: Dr. XYZ")

# Mindmap Section
elif view_option == "Mindmap":
    st.header("Mindmap")
    selected_chapter = st.selectbox("Select Chapter", [f"Chapter {i}" for i in range(1, 9)])
    selected_person = st.selectbox("Select Member", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
    pdf_file = f"mindmap_{selected_chapter}_{selected_person}.pdf"  # Replace with your PDF file path
    st.write(f"Mindmap for {selected_chapter} by {selected_person}")
    try:
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Download Mindmap PDF", data=pdf, file_name=pdf_file, mime="application/pdf")
    except FileNotFoundError:
        st.write("PDF is not available yet.")

# Self Reflection Section
elif view_option == "Self Reflection":
    st.header("Self Reflection")
    selected_person = st.selectbox("Select a person to view reflection", ["Azhar", "Suhayb", "Hakimi", "Humaira", "Lydia"])
    pdf_file = f"reflection_{selected_person}.pdf"  # Replace with your PDF file path
    st.write(f"Reflection for {selected_person}")
    try:
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Download Reflection PDF", data=pdf, file_name=pdf_file, mime="application/pdf")
    except FileNotFoundError:
        st.write("PDF is not available yet.")

# Extra Categories
#elif view_option == "Extra Categories":
    #st.header("Extra Categories")
    #st.write("Additional sections such as Future Improvements, References, and Appendix can be added here.")

#st.write("Thank you for visiting our project website!")

