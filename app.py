import streamlit as st
import pandas as pd
import re 
# st.set_page_config(layout="wide")  # Set Streamlit layout to wide


st.set_page_config('Text Tool', layout="wide")
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

# Button to trigger action
submit = st.button("Submit IDs")

if elements_str or submit:
    elements = elements_str.split('\n')
    elements_list = [element for element in elements if element]
    st.write(elements_list)
else:
    st.write('Please enter some IDs.')

st.write('---')
st.header("Regex Search")
regex_pattern = st.text_input("Enter Regex Pattern:")
text = st.text_area("Enter Text:")

def regex_search(pattern, text):
    matches = list(re.finditer(pattern, text))
    
    # 3.a List without index
    list_without_index = [match.group() for match in matches]
    
    # 3.b String with '\n' separator
    string_with_separator = "\n".join(list_without_index)
    
    # 3.c List with index (dictionary form)
    list_with_index = [{"index": match.start(), "value": match.group()} for match in matches]
    
    return list_without_index, string_with_separator, list_with_index

if st.button("Search"):
    if regex_pattern and text:
        try:
            list_without_index, string_with_separator, list_with_index = regex_search(regex_pattern, text)
            
            # Display results
            st.subheader("Search Result as List:")
            st.write(list_without_index)
            
            st.subheader("Search Result as String:")
            st.text(string_with_separator)
            
            st.subheader("Search Result as List with Index:")
            st.write(list_with_index)
        except re.error:
            st.error("Invalid regex pattern.")
    else:
        st.warning("Please enter both the regex pattern and text.")

import streamlit.components.v1 as components

st.title("Embed a Web Page in Streamlit App")

# Specify the URL you want to display
url = "https://myapi.fyers.in/docsv3#tag/Broker-Config/paths/~1Broker%20Config/put"  # Replace with the desired URL

# Set the dimensions for the iframe
# height = 600
# width = 800

# Insert iframe using HTML
components.html(f"""
    <iframe src="{url}" style="position:absolute; top:0; left:0; width:100%; height:100%;" frameborder="0"></iframe>
""", height=700)

