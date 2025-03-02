import streamlit as st
import time

st.title("Countdown Timer")

if 'total_seconds' not in st.session_state:
    st.session_state.total_seconds = 0
if 'running' not in st.session_state:
    st.session_state.running = False
if 'paused_time' not in st.session_state:
    st.session_state.paused_time = None
if 'stop' not in st.session_state:
    st.session_state.stop = False


if not st.session_state.running:
    hours = st.number_input("Enter hours:", min_value=0, step=1, key="hours_input")
    minutes = st.number_input("Enter minutes:", min_value=0, step=1, key="minutes_input")
    seconds = st.number_input("Enter seconds:", min_value=0, step=1, key="seconds_input")


def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


if st.button("Start Timer"):
    st.session_state.total_seconds = convert_to_seconds(hours, minutes, seconds)
    st.session_state.running = True
    st.session_state.paused_time = None
    st.session_state.stop = False


if st.session_state.running and st.button("Pause Timer"):
    st.session_state.running = False
    st.session_state.paused_time = st.session_state.total_seconds


if not st.session_state.running and st.session_state.paused_time and st.button("Resume Timer"):
    st.session_state.running = True


if st.session_state.running and st.button("Stop Timer"):
    st.session_state.running = False
    st.session_state.total_seconds = 0
    st.session_state.paused_time = None
    st.session_state.stop = True
    st.experimental_rerun()


if st.button("Reset Timer"):
    st.session_state.total_seconds = 0
    st.session_state.running = False
    st.session_state.paused_time = None
    st.session_state.stop = False
    st.experimental_rerun()

if st.session_state.running:
    with st.empty():
        for seconds_remaining in range(st.session_state.total_seconds, 0, -1):
            if not st.session_state.running or st.session_state.stop:  
                break
            hours, remainder = divmod(seconds_remaining, 3600)
            minutes, seconds = divmod(remainder, 60)
            st.write(f"Time Remaining: {hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
            st.session_state.total_seconds -= 1

        if st.session_state.total_seconds == 0 and not st.session_state.stop:
            st.write("Time's up!")
            st.session_state.running = False
