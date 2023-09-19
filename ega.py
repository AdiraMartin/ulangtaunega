import streamlit as st
import base64

from lepel1 import buat_lepel1
import lepel1
import lepel3 
import textnya

st.set_page_config(page_title='EGA',  layout='wide', page_icon=':gift:')
col1, col2 = st.columns((0.09, 1))

file_ = open(r"Untitled design.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

col1.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="ega gif">', unsafe_allow_html=True)
col2.markdown(
    '''
    <style>
    .title-container {
        display: flex;
        align-items: center;
        margin-bottom: 0;
    }
    
    .title-container h1 {
        margin: 0;
        padding: 0;
    }
    
    .text-container {
        margin: 0;
        padding: 0.1;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

with col2:
    st.markdown('<div class="title-container"><h1>BESBI BESBI EGA!🥳🥳🥳</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="text-container">A simple app buat hadiah hepi bisdey lu</div>', unsafe_allow_html=True)

with st.expander("INI APA WE?"):
     st.write('Aloe gangtemnnnp!!!!')
     st.write(textnya.apa_ini)
     
tabs = st.tabs(["Level 1", "Level 2", 'Level 3'])
with tabs[0]:
    buat_lepel1()
    lepel1.main()
with tabs[1]:
    st.header('The Games')
with tabs[2]:
    lepel3.main()
    

    

     





