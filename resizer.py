import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Photo Resizer", layout="centered")

st.title(" Photo Resizer App using OpenCV")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:

    file_bytes =np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1) 
    image_rgb =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.subheader("Original Image")
    st.image(image_rgb, caption="Original Image", use_container_width=True)

    # Get original dimensions
    original_height, original_width = image.shape[:2]

    st.write(f"**Original Dimensions:** {original_width} x {original_height}")  

    # Resize inputs
    new_width = st.number_input("Enter new width", min_value=1, value=original_width)
    new_height = st.number_input("Enter new height", min_value=1, value=original_height)

    if st.button("Resize Image"):
        resized_image = cv2.resize(image, (int(new_width), int(new_height)))
        resized_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        st.subheader("Resized Image")
        st.image(resized_rgb, caption="Resized Image", use_container_width=True)

        # Convert to downloadable format
        pil_img = Image.fromarray(resized_rgb)
        buf = BytesIO()
        pil_img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Resized Image",
            data=byte_im,
            file_name="resized_image.png",
            mime="image/png"
        )
