import streamlit as st
from PIL import Image

# selected = option_menu(
#   menu_title=None,
#   options=['Home', 'About', 'Projects', "Resume"],
#   icons=['house-door', 'patch-question', 'kanban', 'file-earmark-person'],
#   default_index=0,
#   orientation='horizontal',
# )

# add images
hackstorm_logo = Image.open('images/hackstorm_home.jpeg')
ecoread_logo = Image.open('images/ecoread_logo.png')

# The About page view
st.markdown("""Hey👋, I'm Akebu!""")
st.markdown("## A Data Analyst and Android Developer.")
st.markdown("I'm passionate about using data to solve problems and make decisions. I'm also interested in Machine Learning and Artificial Intelligence as well as Open Source. I'm currently learning more about Data Science and Machine Learning.")

# The Projects page view
st.write('---')
st.header(':computer: Projects')
st.markdown("""Here are some of the projects I've worked on:""")
with st.container():
  left_col, right_col = st.columns(2)
  with left_col:
    st.image(hackstorm_logo)
  
  with right_col:
    st.markdown("### [HackStorm]")
    st.markdown("Designed to help hackers find all the resources for their projects in one place, whether you have an idea or don't, you can always access the resources that HackStorm has to offer.")
    st.markdown("Built with: Streamlit, OpenAI, YoutTube API")
    st.markdown("[View Project](#)")

with st.container():
  left_col, right_col = st.columns(2)
  with left_col:
    st.image(ecoread_logo, width=300)
  
  with right_col:
    st.markdown("### [EcoRead]")
    st.markdown("Uncover the hidden insights in climate change-related text data to better understand the impact and take informed actions.")
    st.markdown("Built with: Streamlit, NLTK, Pandas and Plotly")
    st.markdown("[View Project](ecoread.streamlit.app/)")


# Add resume
st.write('---')
st.header(':page_facing_up: Resume')
st.markdown("To learn more about my work experience and education, check out my resume:")
st.markdown("[View Resume](https://drive.google.com/file/d/1qku5IupTzbu2CIRnLhbB7m9rFEaaI95M/view?usp=sharing)")

# add socials as well
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
