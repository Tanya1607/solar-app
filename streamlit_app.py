import os
from io import BytesIO
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

#loading .env
load_dotenv()

st.set_page_config(page_title="Solar Rooftop AI Analysis", page_icon="🔆")

# Page title is given here
st.title("🔆 Solar Rooftop AI Analysis Tool")
st.markdown("""
Upload a **satellite image** of your rooftop to receive an AI-generated solar feasibility report.

The analysis will include:
- ✅ Estimated usable roof area for solar installation (in m²)
- ✅ Recommended system size (in kWp)
- ✅ Projected annual energy generation (in kWh/year)
- ✅ Estimated return on investment (ROI)
- ✅ Key site considerations (e.g., shading, panel tilt, access)
""")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a satellite rooftop image (JPG or PNG format)", 
    type=["jpg", "jpeg", "png"]
)

# Function to analyze rooftop using Gemini API
def analyze_rooftop_with_gemini(image_bytes):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "❌ Error: Gemini API key is missing. Please check your .env file."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "You are a professional solar consultant. Analyze the rooftop image provided and respond with:\n"
        "1. Estimated total roof area (m²)\n"
        "2. Estimated usable area for solar panels (m²)\n"
        "3. Estimated annual energy production (kWh/year)\n"
        "4. Suggested system size (kWp)\n"
        "5. Estimated return on investment (years), accounting for typical incentives\n"
        "6. Notable observations (e.g., shading, tilt angle, installation feasibility)"
    )

    try:
        image = Image.open(BytesIO(image_bytes))
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"❌ An error occurred during analysis: {e}"

# If a file is uploaded
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Rooftop Image", use_container_width=True)

    if st.button("🔍 Analyze Rooftop"):
        with st.spinner("Analyzing image using AI..."):
            image_bytes = uploaded_file.getvalue()
            result = analyze_rooftop_with_gemini(image_bytes)

        st.subheader("📋 Solar Feasibility Report:")
        st.write(result)

# Example image section
st.markdown("---")
st.markdown("#### 🔎 Example Rooftop Image:")
example_url = "https://images.unsplash.com/photo-1624228653103-0f6c379fb1b9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
st.image(example_url, caption="Example Satellite Rooftop Image")
