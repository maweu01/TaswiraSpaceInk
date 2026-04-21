import streamlit as st
import subprocess
import os
import re

st.title("🎨 Taswira Space Ink")

city = st.text_input("City Name", "Nairobi")
country = st.text_input("Country", "Kenya")

if st.button("Generate Map"):
    with st.spinner("Running Engine..."):
        # Run the engine
        cmd = f"uv run ./create_map_poster.py --city '{city}' --country '{country}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # This part 'hunts' for the filename in the success message
        # Matches: "Poster saved as Nairobi.png"
        match = re.search(r"saved as ([\w\.-]+\.png)", result.stdout)
        
        if match:
            generated_file = match.group(1)
            if os.path.exists(generated_file):
                st.image(generated_file)
                st.success(f"Successfully generated {generated_file}")
            else:
                st.error(f"File {generated_file} created but not found in directory.")
        else:
            st.error("Engine finished but I couldn't find the filename in the output.")
            # Show the terminal output so you can see what happened
            st.code(result.stdout)