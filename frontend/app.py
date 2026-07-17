import streamlit as st

st.set_page_config(page_title="Sports Injury Risk Detection")

st.title("🏃 Sports Injury Risk Detection")

uploaded_file = st.file_uploader("Upload a sports video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.success("Video uploaded successfully!")
    st.video(uploaded_file)