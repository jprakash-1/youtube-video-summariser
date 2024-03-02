import streamlit as st
from get_transcript import get_transcript


def main():
    st.title("YouTube Video Transcript Extractor")

    video_link = st.text_input("Enter the YouTube video Link:")
    if video_link:
        transcript = get_transcript(video_link)
        if transcript:
            st.header("Transcript:")
            st.write(transcript)
        else:
            st.write("Transcript not available. Please check the provided YouTube video link.")

if __name__ == "__main__":
    main()