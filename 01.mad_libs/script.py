import streamlit as st
import random

def generate_random_story(noun, verb, adjective, place, animal, food, emotion, profession, vehicle, color, celebrity):
    stories = [
        f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was a day to remember! Everyone cheered as the {noun} performed {verb} like never before while eating {food}. The {animal} watched in awe as a {color} {vehicle} passed by, carrying {celebrity}.",
        f"In the {place}, a {adjective} {noun} suddenly started to {verb}, making everyone laugh. A {animal} joined in, adding to the fun! People gathered around to watch the {noun} and soon joined in the {emotion}. Meanwhile, a {profession} arrived in a {color} {vehicle}, looking surprised.",
        f"The {adjective} {noun} wanted to {verb} all day long at the {place}, enjoying every moment. Birds chirped, the sun shone brightly, and the {animal} played nearby while enjoying some {food}. Suddenly, a famous {profession} appeared, holding a {color} umbrella and waving to {celebrity}.",
        f"A {adjective} {noun} arrived at the {place} with a dream to {verb}. As the day passed, the {noun} amazed everyone with its incredible {verb} skills, creating a story worth telling. Even the {animal} couldn't stop showing {emotion}! Later, a {celebrity} arrived in a {color} {vehicle} and congratulated the {noun} on its achievements."
    ]
    return random.choice(stories)

def main():
    st.title("Mad Libs Game")
    st.write("Fill in the blanks and generate your story!")
    
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    adjective = st.text_input("Enter an adjective:")
    place = st.text_input("Enter a place:")
    animal = st.text_input("Enter an animal:")
    food = st.text_input("Enter a type of food:")
    emotion = st.text_input("Enter an emotion:")
    profession = st.text_input("Enter a profession:")
    vehicle = st.text_input("Enter a type of vehicle:")
    color = st.text_input("Enter a color:")
    celebrity = st.text_input("Enter the name of a celebrity:")
    
    if st.button("Generate Story"):
        if noun and verb and adjective and place and animal and food and emotion and profession and vehicle and color and celebrity:
            story = generate_random_story(noun, verb, adjective, place, animal, food, emotion, profession, vehicle, color, celebrity)
            st.subheader("Your Mad Libs Story:")
            st.write(story)
        else:
            st.warning("Please fill in all the fields to generate your story!")
    
    st.write("### More Fun with Mad Libs")
    st.markdown("- **[RedKid.Net's Mad Libs](http://www.redkid.net/madlibs/)**: Create fun and interactive Mad Libs stories!")
    st.markdown("- **[Mad Libs Official Site](https://madlibs.com/)**: Play more Mad Libs online!")
    st.markdown("- **[Crazy Libs Generator](https://www.crazylibs.com/)**: Try more creative story generators!")

if __name__ == "__main__":
    main()
