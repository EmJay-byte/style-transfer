
import streamlit as st
import requests
import streamlit.components.v1 as components
from PIL import Image
import io

st.set_page_config(page_title="Neural Style Transfer", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap');
            
    /* Bigger font and improved readability */
            
    html, body, [class*="css"] {
        font-size: 26px !important;
        font-family: Garamond;
        line-height: 1.6;
    }
    .stApp {
            background-color: #2e3b4e;
            background-image: linear-gradient(45deg, #d44c93, #3d719c, #a10ee6);
            background-size: 400% 400%;
            height: 100%;
            animation: gradientBG 10s ease infinite;
        }
    
    @keyframes gradientBG {
           0% { background-position: 0% 50%; }
           50% { background-position: 100% 50%; }
           100% { background-position: 0% 50%; }
       }       
    
    h1, h2, h3 {
        color: #333;
    }

    /* Optional: Adjust tab layout if you're using st.tabs (safe to leave in) */
            
    .stTabs [data-baseweb="tab-list"] {
        flex-wrap: wrap;
    }

    /* Optional: Rounded box feel and background */
            
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
        background-color: #f9f9f9;
        border-radius: 12px;
    }

    /* Slight shadow for visual depth */
    .block-container {
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)


st.title("🎨🖌️ Neural Style Transfer")

page = st.sidebar.radio("Navigate", ["🏠 𝐻𝑜𝓂𝑒", "🖼️ 𝒮𝓉𝓎𝓁𝒾𝓏𝑒!", "ℹ️ 𝒜𝒷𝑜𝓊𝓉"])

if page == "🏠 𝐻𝑜𝓂𝑒":
    st.header("Welcome to the Neural Style Transfer Application!")
    st.write("""
        Upload the image you want to style 𝘸𝘪𝘵𝘩 the image you want to style and witness the magic!✨
             
        Head to the 🖼️ Stylize! section to begin your alchemy 🔮
    """)

elif page == "🖼️ 𝒮𝓉𝓎𝓁𝒾𝓏𝑒!":
    st.header("Upload and Stylize Your Image")

    content = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
    style = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])

    if content and style:
        if st.button("Stylize Image"):
            files = {
                "content": content,
                "style": style
            }

            colab_url = "https://d7b6-35-197-151-153.ngrok-free.app/stylize/"

            with st.spinner("Sending to Colab..."):
                response = requests.post(colab_url, files=files)

            if response.status_code == 200:
                result_img = Image.open(io.BytesIO(response.content))
                st.image(result_img, caption="Stylized Output", use_column_width=True)

                buf = io.BytesIO()
                result_img.save(buf, format="PNG")
                st.download_button("Download Image", buf.getvalue(), "stylized.png", "image/png")
            else:
                st.error("Something went wrong. Check Colab is running.")

elif page == "ℹ️ 𝒜𝒷𝑜𝓊𝓉":
    st.header("About This Project")
    st.markdown("""
    - 📌 This application is built with **Streamlit** + **FastAPI** + **TensorFlow Hub** to provide you fast performance!
    - 💻 Backend runs on **Google Colab**, exposed via **ngrok**
    - 🧠 Uses a pretrained style transfer model to enhance your experience
    - 🌟 This Application is based on the neural style transfer concept and enhanced to let you customize your styled images!
    - 👨‍💻 Made by: 𝑨𝒎𝒂𝒏 𝑲𝒂𝒌𝒌𝒂𝒓 & 𝑱𝒂𝒏𝒉𝒗𝒊 𝑴𝒊𝒔𝒉𝒓𝒂
    """)
