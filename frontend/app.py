import streamlit as st
import requests
import tempfile
from PIL import Image

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="CopMap AI", layout="wide")

st.title("CopMap AI - Police Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload Surveillance Image", type=["jpg","jpeg","png"])

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    image.save(temp_file.name)

    location = st.text_input("Location", "Sector A Market")
    timestamp = st.text_input("Timestamp", "2026-03-10 18:20")

    col1, col2 = st.columns(2)

    if col1.button("Analyze Scene"):

        payload = {
            "image_path": temp_file.name,
            "location": location,
            "timestamp": timestamp
        }

        response = requests.post(f"{API_URL}/analyze", json=payload)

        if response.status_code == 200:

            data = response.json()

            st.subheader("Detection Results")

            colA, colB = st.columns(2)

            with colA:
                st.markdown("### Crowd Analysis")
                st.write(data["crowd"])

                st.markdown("### Alerts")
                st.write(data["alerts"])

            with colB:
                st.markdown("### Risk Assessment")
                st.write(data["risk"])

                st.markdown("### Unattended Bags")
                st.write(data["unattended_bags"])

            st.markdown("### Raw Detections")
            st.write(data["detections"])

        else:
            st.error("Analyze API failed")

    if col2.button("Generate Patrol Summary"):

        payload = {
            "query": f"Provide patrol summary for {location}"
        }

        response = requests.post(f"{API_URL}/summary", json=payload)

        if response.status_code == 200:

            summary = response.json()["summary"]

            st.subheader("Patrol Intelligence Summary")

            st.success(summary)

        else:
            st.error("Summary API failed")
