# This is my business website.
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# ---- website config ----
st.set_page_config(page_title='Mohammad Bazmara', page_icon=':chart_with_upwards_trend:', layout='wide')

# ---- website functions ---
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

def load_css(file):
    with open(file) as f:
        st.markdown(f'<style>{f.read}</style>', unsafe_allow_html=True)

# ---- load things ----
lottie_ai = load_lottie('https://assets1.lottiefiles.com/private_files/lf30_cmd8kh2q.json')
my_image = Image.open('images/mmb1.jpeg')
thumbnail = Image.open('images/maxresdefault.jpg')
load_css('style/style.css')

left_col, right_col = st.columns((2,1))
with left_col:
    with st.container():
        st.subheader('Hi, I am Mohammad bazmara :floppy_disk:')
        st.title('A Data Scientist from Iran')
        st.write(''' 
                I am passionate about finding new ways to use machine Learning to solve unresolved problems.
                 Help new data scientists to learn more and level up their self.
                 ''')
        st.write('[See my CV](https://www.webfx.com/tools/emoji-cheat-sheet/)')
with right_col:
    st.image(my_image)
st.write('---')

left, right = st.columns(2)
with left:
    with st.container():
        st.header('What I do')
        st.write('##')
        st.write('''
        - Create ML project's for big companies.
        - Teach Data Science for passionate students and colleges.
        - Teach Python and Programming at Universities.
        - Updating my knowledge on AI and ML.
        ''')
with right:
    st_lottie(lottie_ai, height=300, key='coding')
st.write('---')

with st.container():
    left , right = st.columns((1,2))
    with left:
        st.image(thumbnail)
    with right:
        st.subheader('How You Would Learn Data Science in 2022')
        st.write('''
                I think this video can help you to learn the best path to be a data science.
                let me know what you think of this vide.
                if you want to watch it from Iran, you should use VPN !!! :closed_lock_with_key:
                ''')
        st.markdown('[Watch the video...](https://www.youtube.com/watch?v=xpIFS6jZbe8)')
    st.write('---')

# ---- Contact US ----

with st.container():
    st.header('If you want to talk to me!')
    st.write('##')
    contact_form = '''
    <form action="d3518bae-1a0a-4bc2-b3e1-4abd4a976c82" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Enter your message here" required> </textarea>
        <button type="submit">Send</button>
    </form>
    '''