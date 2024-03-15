import streamlit as st
st.sidebar.markdown("# Upload Files 🎈")
st.title("Upload Document")
custom_css = """
<style>
    .stApp {
        max-width: 80%;
    
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
# Cho phép tải lên nhiều file và lưu vào session_state
if 'uploaded_files' not in st.session_state:
    st.session_state['uploaded_files'] = []

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=["pdf", "jpeg", "png", "jpg"])

if uploaded_files:
    st.session_state['uploaded_files'].extend(uploaded_files)

if st.session_state['uploaded_files']:
    for uploaded_file in st.session_state['uploaded_files']:
        st.write(uploaded_file.name)
else:
    st.write("No files uploaded yet.")