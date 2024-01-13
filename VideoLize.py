import time
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo


st.set_page_config(
    page_title="VideoLize",
)


# add kitten logo
add_logo("videolize.png")


# st.sidebar.image("videolize.png",use_column_width=True)

# utility functions
def display_video():
    video_file = open('example_videos/butterfly.mp4', 'rb')
    video_bytes = video_file.read()
    return video_bytes

def generate_output():
    progress_text = "Operation in progress. Please wait. Might take about 15-20 minutes"
    count = 0
    my_bar = st.progress(count, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.1)
        count+=1
        my_bar.progress(count, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    return display_video()
    # st.write('Generated....')
    # st.button("Rerun")


# main content
st.image("videolize.png")
main_col1 , main_col2 = st.columns(2)
with main_col1:
    prompts = st.text_area("Enter Prompts separated by comma: ")
    # print(type(prompts))
    agree = st.checkbox('Enter Audio Script [Optional]:')

    if agree:
        audio = st.text_area("Enter audio that will be overlayed in generated video: ")
    btn = st.button('Generate')
with main_col2:
    show_generated_content = st.empty()
    
    # st.markdown(
    #     """
    #     <style>
    #         .progress-container {
    #             background-color: #E0E0E0;
    #             border-radius: 10px;
    #             padding: 10px;
    #             height: 350px;
    #             width: 350px;
    #         }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    # # Use the rectangle to hold the progress bar
    # progress_container = st.markdown(
    #     "<div class='progress-container'></div>", unsafe_allow_html=True)
    # progress_bar = st.progress(0)

if btn:
    video_bytes = generate_output()
    show_generated_content.video(video_bytes, format="video/mp4")




