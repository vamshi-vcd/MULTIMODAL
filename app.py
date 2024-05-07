import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, ClientSettings
from eyetracker import EyeTracker
from handtracker import HandTracker

# Set up EyeTracker and HandTracker
eye_tracker = EyeTracker()
hand_tracker = HandTracker()

class MyVideoProcessor(VideoProcessorBase):
    def __init__(self):
        super().__init__()

    def recv(self, frame):
        # Process frame (e.g., track eyes and hands)
        frame = eye_tracker.track_eyes(frame)
        frame = hand_tracker.track_hands(frame)
        return frame

def main():
    st.title("Eye and Hand Tracker")

    client_settings = ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
    )

    webrtc_ctx = webrtc_streamer(
        key="example",
        video_processor_factory=MyVideoProcessor,
        client_settings=client_settings,
        async_processing=True,
    )

    if not webrtc_ctx.state.playing:
        st.warning("No video stream detected.")

if __name__ == "__main__":
    main()
