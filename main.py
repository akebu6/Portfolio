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
if selected == 'Home':
  # Contact us form
  st.write('---')
  st.header(':mailbox: Get in touch with me')

  contact_form = """
      <form action="https://formsubmit.co/your@email.com" method="POST">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Your name"required>
          <input type="email" name="email" placeholder="Your email" required>
          <textarea name="message" placeholder="Your message here"></textarea>
          <button type="submit">Send</button>
      </form>
      """
      
  def local_css(file_name):
          with open(file_name) as f:
              st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
              
  local_css('styles/styles.css')

  st.markdown(contact_form, unsafe_allow_html=True)

# The About page view

# The Projects page view

# The Resume page view

# add socials as well
  