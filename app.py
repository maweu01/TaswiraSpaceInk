import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Taswira Space Ink", page_icon="🎨")

st.title("🎨 Taswira Space Ink")
st.markdown("### Cartographic Artistry Engine")

# User Inputs
city = st.text_input("Enter City", "Nairobi")
country = st.text_input("Enter Country", "Kenya")

if st.button("Generate Map Poster"):
    with st.spinner("Engine is running..."):
        # This executes the uv run command from your README
        cmd = f"uv run ./create_map_poster.py --city '{city}' --country '{country}'"
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # Check if an image was created (adjust 'output.png' if your script uses a different name)
        if os.path.exists("output.png"):
            st.image("output.png", caption=f"Map of {city}")
        else:
            st.error("Engine finished but image not found.")
            st.info("Terminal Output:")
            st.code(process.stdout)