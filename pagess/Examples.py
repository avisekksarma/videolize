import streamlit as st
from streamlit_extras.app_logo import add_logo

# add kitten logo
add_logo("videolize.png")
# variables
# first element = prompts , second elem. = text for audio, third elem = video file path
inputs_map = {
    'Evolution': ["A chimpanzee in African jungle|Homo habilis holding stone tools in African jungle|Two Archaic Homo Sapiens interacting with each other|A modern human farming in a farmland|A modern human wearing suit in a city with a lot of buildings|A modern human using computers and AI", "Human evolution is a continuous process that spans millions of years, involving biological adaptations and cultural developments that have shaped Homo sapiens into the species we are today.","example_videos/evolution.mp4"],
    'Butterfly':["A yellow butterfly lays egg on a green leaf|Very very tiny egg of butterfly is kept on the green leaves|Caterpillar eats leaves and grows|Green Pupa hangs gently from the branch|A vibrant yellow butterfly emerges from the pupa, ready to dance in the sky.","In a whimsical dance of nature, a yellow butterfly delicately lays tiny eggs on leaves. These eggs hatch into voracious caterpillars, voraciously munching on leaves until they undergo a miraculous transformation within protective pupae. The grand finale reveals a newly emerged butterfly, symbolizing the captivating cycle of life and metamorphosis","example_videos/butterfly.mp4"],
    'Stellar Evolution': ["Empty and dark space in the universe| Stellar nebula| A star grows into an extremely large red giant| A spherical red old sun in space| A burning young star| A star goes supernova| Black-filled hole, black hole, circle, sphere","The star lifecycle begins with a gaseous nebula, a vast cloud of gas and dust in space. Under the influence of gravity, the nebula begins to collapse, giving birth to a young star. As the star matures, it enters the phase of a red giant with the expansion of its outer layers. Massive stars undergo supernova, releasing an immense amount of energy and scattering elements into space. The explosion can lead to the formation of a black hole, an incredibly dense region where gravity is so strong that nothing, not even light, can escape.","example_videos/star-lifecycle.mp4"],
    "World War II": ["US Airplane flies on the sky carrying little boy (bomb used in second world war)|The US airplane drops the bomb on hiroshima.|Bomb creates a huge explosion destroying building in its perimeter in Hiroshima and produces large amount of radiation.|People in the perimeter of explosion turn into ashes.|Eventually, the people who suffer from radiation die due to radiation.","In WWII, a US plane dropped the 'Little Boy' bomb on Hiroshima, causing a massive explosion and releasing lethal radiation. The immediate impact turned people to ashes, while long-term exposure led to fatal radiation-related illnesses. This tragic event left an enduring legacy, illustrating the devastating toll of atomic warfar","example_videos/world-war.mp4"],
    "Abstract Art": ["Abstract human face, happy geometric, colorful|Random geometric abstract art|Abstract human face, happy geometric, colorful|Random geometric abstract art|Abstract human face, happy geometric, colorful|Random geometric abstract art|Abstract human face, happy geometric, colorful|Random geometric abstract art|Abstract human face, happy geometric, colorful","I've wondered that I've never go the hunger to fall asleep only after seeing my dreams. A mixture of miscible fluids wit and wisdom drinking the night off.Now sleepless it remains.What fun we had! Nothing went as bad.As blame We even laughed the same-like a real, true rhyme.I wish we'd had more time.","examples_videos/abstract-art.mp4"]
}

st.header('Examples: ')
st.divider()

if 'clicks' not in st.session_state:
    st.session_state['clicks'] = {}

def click(key):
    st.session_state.clicks.clear()
    st.session_state.clicks[key] = True
    # display_example(key)

# def unclick(key):
#     st.session_state.clicks[key] = False

# top 3 examples choosen
col1, col2, col3, col4, col5 = st.columns(5)
st.button('Clear Example',on_click=lambda:st.session_state.clicks.clear())
show_example_container = st.empty()

with col1:
   st.write("Evolution")
   st.button('Show',key="Evolution",on_click=click,args=('Evolution',))

with col2:
   st.write("Butterfly")
   st.button('Show',key="Butterfly",on_click=click,args=('Butterfly',))

with col3:
   st.write("Stellar Evolution")
   st.button('Show',key="Stellar Evolution", on_click=click,args=('Stellar Evolution',))

with col4:
   st.markdown("###### World War II")
   st.button('Show', key="World War II",on_click=click, args=('World War II',))

with col5:
   st.write("Abstract Art")
   st.button('Show', key="Abstract Art",on_click=click, args=('Abstract Art',))

def display_example(key):
    if st.session_state.clicks.get(key):
        global show_example_container
        data = inputs_map[key]
        
        with show_example_container.container():
            st.markdown('### Prompt:')
            prompts = data[0].split('|')
            for prompt in prompts:
                st.code(prompt)
            st.markdown('### Text Script:')
            st.code(data[1])
            video_file = open(data[2], 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)



for key in inputs_map:
    display_example(key)