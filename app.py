import streamlit as st
import subprocess
import io

# Function to execute Python script and capture output
def execute_script(script_file):
    try:
        # Execute the Python script
        process = subprocess.Popen(['python', script_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Check for errors
        if error:
            return f"Error occurred: {error.decode('utf-8')}"
        
        return output.decode('utf-8')
    except Exception as e:
        return f"Error occurred: {e}"

# Streamlit app
def main():
    st.title('MULTIMODAL FUSION TO ENHANCE HUMAN COMPUTER INTERACTION')

    # File paths of Python script files
    curlcounter_file="curlcounter.py"
    eyetracker_file = "eyetracker.py"
    handtracker_file = "handtracker.py"

    # Align buttons at the center
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)

    st.markdown("<h3><b>Run Curl Counter</b></h3>", unsafe_allow_html=True)
    if st.button('Click here to open Curl Counter', key="curncounter"):
        st.write("### Opening Curl Counter")
        output_curlcounter = execute_script(curlcounter_file)
        st.code(output_curlcounter, language='python')

    # Button to execute eye_tracker.py
    st.markdown("<h3><b>Run Eye Tracker</b></h3>", unsafe_allow_html=True)
    if st.button('Click here to open Eye Tracking Mouse', key="eyetracker"):
        st.write("### Opening Eye Tracker")
        output_eyetracker = execute_script(eyetracker_file)
        st.code(output_eyetracker, language='python')

    # Button to execute hand_tracker.py
    st.markdown("<h3><b>Run Hand Tracker</b></h3>", unsafe_allow_html=True)
    if st.button('Click here to open Hand Tracking Mouse', key="handtracker"):
        st.write("### Opening Hand Tracker")
        output_handtracker = execute_script(handtracker_file)
        st.code(output_handtracker, language='python')

    st.write("</div>", unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
