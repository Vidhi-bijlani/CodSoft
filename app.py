import streamlit as st
from PIL import Image
import random
from caption_model import ImageCaptioner

# Load model once
@st.cache_resource
def load_model():
    return ImageCaptioner()

st.set_page_config(page_title="Image Captioning AI", page_icon="🖼️")
st.title("🖼️ Image Captioning AI - CodSoft Task 3")
st.write("Upload any image and get AI captions!")

# EDIT 1: ADD THIS SPINNER SO YOU DON'T SEE BLACK SCREEN
with st.spinner("⏳ Loading AI Model... Please wait 20-30 seconds on first run"):
    captioner = load_model()

st.success("✅ Model Loaded! Upload an image below")

# Upload button
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
style = st.selectbox("Caption Style", ["Normal", "Detailed", "Funny", "Poetic"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    # EDIT 2: use_column_width is old. Use this for new streamlit
    st.image(image, caption="Your Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        with st.spinner("AI is thinking..."):
            caption = captioner.generate_caption(image, style.lower())
        st.success(f"**[{style}] AI Caption:** {caption}")