import streamlit as st
import base64

st.set_page_config(page_title="Sourov Talukder | Portfolio", layout="wide")

# Adding 01_Profile Top Image.png
st.image("01_Profile Top Image.png")


# Adding Left Section Bio & Logos
import streamlit as st

st.set_page_config(layout="wide")

# Adding Bio And Connection Link
# ----- Two Columns -----
left, right = st.columns([3, 1])   # Adjust ratio as needed

# ---------------- LEFT COLUMN ----------------
with left:
    st.markdown("""
    ### Hi <span style="color:#1E90FF;">👋</span> 
                
    Thank you so much for visiting my portfolio.I simply love to introduce myself as a **Data Professional** : not specifically a Data Analyst, Data Scientist, or Data Engineer — because throughout my data journey I have worked across all parts of the data lifecycle.From **data collection** (<span style="color:#1E90FF;">Web, ETL, Python, SQL</span>) to **data cleaning** (<span style="color:#1E90FF;">Python, Excel, Power Query</span>),to **data modeling & dashboarding** (<span style="color:#1E90FF;">Excel, Power BI</span>), and even **predictive analytics** (<span style="color:#1E90FF;">Machine Learning, Python, AI/Analytics</span>),I’ve been involved in it all.  
    Data is everywhere; even you visiting my profile is a form of data. I love working with data,  it’s my passion and my career.  
    If you are also in this field, I would really love to connect with you.  
    I'm always happy to help if you're interested in data or need any support.  
    """, unsafe_allow_html=True)

#################### Adding Connect With Me Functionalities #######
# ---------------- RIGHT COLUMN ----------------
with right:
    st.markdown("### Connect with Me")

    # LinkedIn
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/sourov-talukder-1a5320279" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
            LinkedIn
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # GitHub
    st.markdown(
    """
    <a href="https://github.com/Sourov69" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="40">
        GitHub
    </a>
    """,
    unsafe_allow_html=True,
)


    st.write("")

    # WhatsApp
    st.markdown(
        """
        <a href="https://wa.me/8801940968196" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="40">
            WhatsApp
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # Email
    st.markdown(
    """
    <a href="mailto:meherabsourov7@gmail.com">
        <img src="https://cdn-icons-png.flaticon.com/512/281/281769.png" width="40">
        Mail
    </a>
    """,
    unsafe_allow_html=True
)





#####################################################################

st.markdown("## My Skills")
import streamlit as st

skills = [
    ("Excel", "https://cdn-icons-png.flaticon.com/512/732/732220.png"),
    # Power BI main logo (SVG)
    ("Power BI", "https://logos-world.net/wp-content/uploads/2022/02/Power-BI-Logo.png"),
    ("SQL", "https://cdn-icons-png.flaticon.com/512/4248/4248443.png"),
    ("Python", "https://cdn-icons-png.flaticon.com/512/5968/5968350.png"),
    ("Machine Learning", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8r9P1rohw9vXz-hfg0FYQiD7SWcoMGEKJSg&s"),
    ("AI", "https://thumbs.dreamstime.com/b/stylized-representation-artificial-intelligence-ai-brain-depicted-as-glowing-blue-outline-filled-intricate-circuit-362366255.jpg")
]

cols = st.columns(len(skills))

for col, (name, logo) in zip(cols, skills):
    if name == "Power BI" or name == "AI":
        col.image(logo, width=100)
        col.markdown(f"### {name}")
    else:
        col.image(logo, width=60)
        col.markdown(f"### {name}")




############ Add Work Samples and Projects ########
st.markdown("## My Work Samples and Projects")


























































# if st.checkbox("Show Project Details"):
 
#     # You can use a column just like st.sidebar:

#     # Or even better, call Streamlit functions inside a "with" block:

#     chosen = st.radio(
#         'Sorting hat',
#         ("Sales", "Product", "Customer", "Other"),horizontal=True)
        

  
#     if chosen ==  "Sales":
#         st.image("Screenshot (250).png")
#     elif chosen == "Product":
#         st.image("Screenshot (245).png")
#     elif chosen == "Customer":
#         st.video("My Hridhy.mp4")
#     else:
#         st.image("My pic.png")