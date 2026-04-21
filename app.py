import streamlit as st
import subprocess
import os
import glob
import time

# ... (keep your title and inputs the same) ...

if st.button("Generate Map"):
    with st.spinner("Running Engine..."):
        # 1. Run the engine
        cmd = f"uv run ./create_map_poster.py --city '{city}' --country '{country}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # 2. Give the system a second to finish writing the file to disk
        time.sleep(2) 
        
        # 3. Look for ANY png file in the current folder
        png_files = glob.glob("*.png")
        
        if png_files:
            # Sort by time to get the newest file created
            newest_file = max(png_files, key=os.path.getmtime)
            st.image(newest_file, caption=f"Generated: {newest_file}")
            st.success(f"Found your map: {newest_file}")
        else:
            st.error("Engine finished but no .png files were found in the folder.")
            st.info("Terminal Output for Debugging:")
            st.code(result.stdout)
            st.code(result.stderr) # This shows hidden errors