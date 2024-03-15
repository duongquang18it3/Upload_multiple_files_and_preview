# pages/preview_data_page.py
import streamlit as st
import pandas as pd
import json
import os
st.set_page_config(layout="wide",page_icon = "🏠")
def main():
    st.sidebar.markdown("# Data preview🎈")

    st.title("Preview & Data")
    custom_css = """
    <style>
        .stApp {
            max-width: 100%;
        }
    </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)
    base_path = 'F:/Streamlit/streamlit'

    if 'uploaded_files' not in st.session_state:
        st.session_state['uploaded_files'] = []

    col1, col2 = st.columns([2, 4])

    with col1:
        st.subheader("File Preview")
        
        file_names = [""] + [file.name for file in st.session_state['uploaded_files']]
        selected_file_name = st.selectbox("Choose a file to preview", options=file_names, index=0)

        if selected_file_name:
            selected_file_index = file_names.index(selected_file_name) - 1
            selected_file = st.session_state['uploaded_files'][selected_file_index]

            # Ví dụ preview file ở đây...

    with col2:
        st.subheader("Data Table (JSON Data)")
        if selected_file_name:
            # Chọn file JSON dựa vào thứ tự file được chọn
            json_file_name = 'sample-json-1.json' if selected_file_index % 2 == 0 else 'sample-json-2.json'
            json_file_path = os.path.join(base_path, json_file_name)

            if os.path.exists(json_file_path):
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # Biến đổi dữ liệu JSON thành DataFrame với các cột ID, Key, Value
                records = []
                for key, value in json_data.items():
                    if isinstance(value, list):  # Xử lý trường hợp value là list
                        # Chuyển đổi tất cả các phần tử trong list thành chuỗi trước khi nối
                        value = ', '.join(str(item) for item in value)
                    records.append({"ID": key, "Key": key, "Value": str(value)})

                df_json_data = pd.DataFrame(records)
                st.table(df_json_data)
            else:
                st.error(f"File {json_file_name} not found.")
        else:
            st.write("Please select a file to preview and view its associated JSON data.")

if __name__ == "__main__":
    main()
