import streamlit as st
from streamlit_option_menu import option_menu

st.title('Hello World')

selected = option_menu(
  menu_title=None,
  options=['Home', 'About', 'Projects', "Resume"],
  icons=['🏠', '📝', '📂', '📄'],
  default_index=0,
  orientation='horizontal',
)

# The Home page view

# The About page view

# The Projects page view

# The Resume page view
