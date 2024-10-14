import streamlit as st
from openai import OpenAI
import os


# Load environment variables from .env file

#remove the toml file
# Get the API key from environment variables
OPENAI_API_KEY = "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"


# Debug: Print the first few characters of the API key (remove in production)
print(f"API Key (first 5 chars): {OPENAI_API_KEY[:15]}...")

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY in your .env file.")
    st.stop()

# Initialize OpenAI client with API key directly
client = OpenAI(api_key=OPENAI_API_KEY)

# Set page config
st.set_page_config(page_title="AI Generation Hub", page_icon="🎨", layout="wide")

# Title for website
st.title("🎨 AI Generation Hub")

# Main content
col1, col2 = st.columns([2, 3])

with col1:
    prompt = st.text_area("Enter your prompt here:", height=150)
    size = st.selectbox("Image Size", ["1024x1024", "1024x1792", "1792x1024"])
    quality = st.selectbox("Image Quality", ["standard", "hd"])
    style = st.selectbox("Image Style", ["vivid", "natural"])

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating image..."):
                try:
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt,
                        n=1,
                        size=size,
                        quality=quality,
                        style=style
                    )
                    image_url = response.data[0].url
                    st.session_state['generated_image'] = image_url
                    st.success("Image generated successfully!")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a prompt.")

with col2:
    if 'generated_image' in st.session_state:
        st.image(st.session_state['generated_image'], caption="Generated Image", use_column_width=True)
    else:
        st.info("Your generated image will appear here.")

# Footer
st.markdown("---")
st.markdown("Powered by OpenAI's DALL-E 3")
