import streamlit as st
import pandas as pd
import re 

st.set_page_config('Text Tool')
st.title('Text Mining Tool!')

st.write('---')
st.header('Get All IDs from the Page Source Code')

src_text = st.text_area('Enter the source code below.' , max_chars=1000000, key='src_elm')

# Button to trigger action
submit = st.button("Submit Text")

if src_text or submit:
    pattern = re.compile("(?<=reviewstatus_)\d+")
    q_ids = pattern.findall(src_text)
    if q_ids:
        # st.text_area('Question IDs:', value= ',\n'.join(q_ids))
        q_ids_str = '\n'.join(q_ids)
        q_ids_str_display = f"```\n{q_ids_str}\n```"
        st.markdown( q_ids_str_display)

    else:
        st.write('No ID found. Please enter another source code.')

st.write('---')
st.header('Get Array for MQL query')
elements_str = st.text_area('Enter the elements.' , max_chars=1000000, key='text_elm')
elements = elements_str.split('\n')
elements_list = [element for element in elements if element]
st.write(elements_list)
