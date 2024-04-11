import streamlit as st

# Add custom CSS to set the background color to white
st.markdown(
    """
    <style>
    .reportview-container {
        background: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu options
menu_options = {
    "Home": None,
    "Chatbot": "Chatbot Page",
    "About": "About the Chatbot"
}

# Function to create chatbot response
def chatbot_response(user_input):
    # Your chatbot logic here
    return "Chatbot: Hello! How can I assist you today?"

# Streamlit UI
def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("", list(menu_options.keys()))

    if selection == "Home":
        st.title("Welcome to Chatbot!")
        st.image("study_chatbot.png")
        st.markdown("Click the button below to start chatting with the chatbot.")

        if st.button("Start Chatbot"):
            st.experimental_set_query_params(menu="Chatbot")
            st.experimental_rerun()

    elif selection == "Chatbot":
        st.title("Chatbot")
        st.write("Welcome to the Chatbot page!")
        
        user_input = st.text_input("You:", "")
        if st.button("Send"):
            if user_input:
                response = chatbot_response(user_input)
                st.text_area("Chatbot:", value=response, height=100)

    elif selection == "About":
        st.title("About the Chatbot")
        st.write("This chatbot is created to assist users with various queries.")

if __name__ == "__main__":
    main()
