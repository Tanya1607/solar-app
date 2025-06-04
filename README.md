
# 🌞 Solar Rooftop Analysis with AI

## 🚀 Project Overview
This project analyzes rooftop images to assess their solar panel installation potential using AI. Users can upload an image and receive an automated analysis with insights.
I have also added Ai so that if we pass any other image it will automatically tell us that the image is inappropriate.

## 🧠 How the AI Model Works
- Uses **OpenRouter API** to access **Gemini 1.5 Flash** model.
- Used the google gemini key because the OPEN-AI-API -KEY limit was exhausted.
- The model receives the rooftop image and a solar analysis prompt.
- It returns structured text insights about suitability, orientation, and solar feasibility.

## 🧩 Component Structure
- **Frontend**: Built with **Streamlit** for easy user interaction and image upload.
- **Backend**: Python script sends image and  prompt to Gemini model and receives outputs.
- **Integration**: All components run in a unified Streamlit app for a seamless experience.


## 🛠️ Setup Guide

### Prerequisites
- Python 3.9 or above
- pip package manager

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Sanchit1079/solar-ai-app
   cd your-repo-directory
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```


### Live Deployment Link
https://solar-ai-app.streamlit.app/

using this link you will be redirected to the deployed app.