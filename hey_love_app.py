import streamlit as st

# Page configuration
st.set_page_config(page_title="HEY! LOVE💌", page_icon="💌", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6e6;
    }
    .stButton>button {
        background-color: #ff4d4d;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("HEY! LOVE💌")
st.write("Welcome to our special love app 💖")

# Questions

q1 = st.text_input("1. What's your ideal way to spend time together?")
q2 = st.radio("2. Will you go on a date with me?", ["Yes", "Maybe", "No"])
q3 = st.radio("3. How excited are you to go on a date with me?",
              ["Very", "Can't wait to see you"])
q4 = st.radio("4. Are you free on 28 June?", ["Yes", "No"])
q5_choice = st.radio("5. Where do you want to go?",
                     ["Majnu Ka Tilla", "Connaught Place", "Somewhere else"])
q5_custom = ""
if q5_choice == "Somewhere else":
    q5_custom = st.text_input("Tell me where:")

# Submit button
if st.button("Submit 💌"):
    st.write("### Your answers:")
    st.write(f"1. Ideal time together: {q1}")
    st.write(f"2. Date?: {q2}")
    st.write(f"3. Excitement level: {q3}")
    if q4 == "Yes":
        st.write("4. Free on 28 June: Yes")
    else:
        st.write("4. Free on 28 June: No")
    destination = q5_choice if q5_choice != "Somewhere else" else q5_custom
    st.write(f"5. Going to: {destination}")
    
    # Final message logic
    if q2 == "Yes":
        st.success("✨ Yay!! 🎉 I can't wait to spend time with you 🥰")
        st.write(
            "For my cutest boy, Raghvi ❤️\n\n"
            "I am grateful that you came into my life. You are all "
            "the motivation I need in life and I love you so much "
            "that I don't want to let you go. I am so in love with you, "
            "honey🐝. See you soon kutte🐶"
        )
    else:
        st.warning("Hmm... I'm still taking you out anyway 😜")
