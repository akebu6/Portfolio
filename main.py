import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
  menu_title=None,
  options=['Home', 'About', 'Projects', "Resume"],
  icons=['house-door', 'patch-question', 'kanban', 'file-earmark-person'],
  default_index=0,
  orientation='horizontal',
)

# The Home page view
# The home page will have some basic information about me and my interests as well as well include a picture of me, my resume, and a link to my socials: GitHub LinkedIn, Twitter and Kaggle.

# The About page view

# The Projects page view

# The Resume page view
