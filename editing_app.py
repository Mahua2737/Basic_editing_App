import streamlit as st
from PIL import Image
import io
import base64
from gray import apply_gray
from black_and_white import apply_black_and_white
from pencil_sketch import apply_pencil_sketch
from blur_effect import apply_blur_effect

# UI code
image = Image.open("Log.jpeg")
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.markdown(
        """ <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """,
        unsafe_allow_html=True,
    )
    st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)

with col2:
    st.image(image, width=150)

st.sidebar.markdown('<p class="font">Image Processing App</p>', unsafe_allow_html=True)
with st.sidebar.expander("About the App"):
    st.write(
        """
        This is a Simple image processing app built using Streamlit that allows you to perform basic image operations.
     """
    )

filter = st.sidebar.radio(
    "Convert your photo to:",
    ["Original", "Gray Image", "Black and White", "Pencil Sketch", "Blur Effect"],
)

uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Before</p>', unsafe_allow_html=True)
        st.image(image, width=300)

    with col2:
        st.markdown('<p style="text-align: center;">After</p>', unsafe_allow_html=True)

        rotate_angle = st.sidebar.slider("Rotate Image (degrees)", -180, 180, 0)
        resized_width = st.sidebar.slider("Resize Width", 50, 1000, 300)
        resized_height = st.sidebar.slider("Resize Height", 50, 1000, 300)

        transformed_image = image.rotate(rotate_angle, expand=True)
        transformed_image = transformed_image.resize((resized_width, resized_height))

        if filter == "Gray Image":
            transformed_image = apply_gray(transformed_image)
        elif filter == "Black and White":
            transformed_image = apply_black_and_white(transformed_image, slider)
        elif filter == "Pencil Sketch":
            transformed_image = apply_pencil_sketch(transformed_image, slider)
        elif filter == "Blur Effect":
            transformed_image = apply_blur_effect(transformed_image, slider)
        else:
            pass

        st.image(transformed_image, caption="Transformed Image", width=300)

        buffered = io.BytesIO()
        transformed_image.save(buffered, format="JPEG")
        buffered.seek(0)
        b64_image = base64.b64encode(buffered.read()).decode()
        href = f'<a href="data:file/jpg;base64,{b64_image}" download="transformed_image.jpg">Download image</a>'
        st.sidebar.markdown(href, unsafe_allow_html=True)

