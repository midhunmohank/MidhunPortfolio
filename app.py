import streamlit as st

# Set page title
st.set_page_config(page_title="My Data Engineering Portfolio")

# Create a header
st.header("My Data Engineering Portfolio")

# Add a short introduction
st.write("""
Welcome to my data engineering portfolio! Below you will find a list of my projects that showcase my skills in data engineering.
""")

# Create a list of your projects with descriptions and links to GitHub
projects = [
    {
        "name": "Project 1",
        "description": "Description of project 1",
        "github": "Link to GitHub repo for project 1"
    },
    {
        "name": "Project 2",
        "description": "Description of project 2",
        "github": "Link to GitHub repo for project 2"
    },
    {
        "name": "Project 3",
        "description": "Description of project 3",
        "github": "Link to GitHub repo for project 3"
    }
]

# Loop through the projects and display them in a table
for project in projects:
    st.subheader(project["name"])
    st.write(project["description"])
    st.write(project["github"])
