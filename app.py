import streamlit as st
import pandas as pd
import re 

st.set_page_config('Text Tool')
st.title('Text Mining Tool!')

st.write('---')
st.header('Get All IDs from the Page Source Code')

src_text = st.text_area('Enter the source code below.' , max_chars=1000000, key='src_elm')

if src_text:
    pattern = re.compile("(?<=reviewstatus_)\d+")
    q_ids = pattern.findall(src_text)
    if q_ids:
        st.text_area('Question IDs:', value= ', '.join(q_ids))
    else:
        st.write('No ID found. Please enter another source code.')
st.write('---')
st.header('Feature-2')
text = st.text_area('Enter the text below.' , max_chars=1000000, key='text_elm')
st.write(text[:1000])
