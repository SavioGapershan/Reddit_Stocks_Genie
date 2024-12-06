import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import praw
import google.generativeai as genai
import pickle
import time
import base64
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences  # Import for padding sequences

# Streamlit Page Configuration (must be the first Streamlit command)
st.set_page_config(page_title="Reddit Stocks Genie", layout="wide", page_icon="🧞")

# Load the tokenizer (using the pickle file)
with open("tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)

# Configure Gemini API
genai.configure(api_key="your Gemini API Key here")  # Replace with your actual API key

# Helper function to format text with bold and italics
def format_response_with_bold(text):
    # First, replace any text surrounded by ** or * (for bold) and _ (for italics) to proper markdown
    formatted_text = re.sub(r"\*(.*?)\*", r"**\1**", text)  # Bold text between *
    formatted_text = re.sub(r"\_(.*?)\_", r"*\1*", formatted_text)  # Italics text between _
    return formatted_text

# Function to fetch Reddit posts dynamically
def fetch_reddit_posts(subreddit, num_posts=5):
    reddit = praw.Reddit(
        client_id="Your Client ID Here",
        client_secret="your Client Secret here",
        user_agent="apiprojectname-script by /u/Reddit_username"
    )

    subreddit = reddit.subreddit(subreddit)
    posts = [submission.title for submission in subreddit.hot(limit=num_posts)]
    return pd.DataFrame({"cleaned_post": posts})

# Function to fetch answers from Gemini
def fetch_gemini_answer(question, data):
    try:
        prompt = f"Based on the following Reddit posts, answer the question: {question}\n\nData: {data}"
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to analyze sentiment (mocked for now)
def predict_sentiment(dataframe):
    sentiments = ["Positive", "Neutral", "Negative"]  # Placeholder for actual predictions
    dataframe["sentiment"] = [sentiments[i % 3] for i in range(len(dataframe))]
    return dataframe

# Set Background Image
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_png_as_page_bg('static/background-image.jpg')

# Custom CSS
st.markdown(
    r"""<style>
        .centered {
            text-align: center;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: black;
            margin-top: 20px;
        }
        .curved-box {
            border: 2px solid #FF4500;
            border-radius: 15px;
            padding: 20px;
            margin: 20px auto;
            width: 60%;
            background-color: white;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .start-button {
            display: block;
            margin: 20px auto;
            padding: 15px 30px;
            font-size: 1.5em;
            font-weight: bold;
            color: white;
            background-color: blue;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease;
        }
        .start-button:hover, .start-button:active {
            background-color: orange;
        }
    </style>""", unsafe_allow_html=True
)

# Header and Title
st.markdown('<div class="centered"><h1 class="title">Reddit Stocks Genie</h1></div>', unsafe_allow_html=True)

# Subreddit and Slider Controls
subreddit = st.text_input("Enter Subreddit:", "stocks")
num_posts = st.slider("Number of Posts to Fetch:", 1, 50, 5)

# Start Button
if st.button("START NOW", key="start_now_button"):
    with st.spinner("Fetching Reddit posts..."):
        time.sleep(2)
        # Fetch Reddit Posts
        st.session_state.reddit_data = fetch_reddit_posts(subreddit, num_posts)
        st.session_state.reddit_data = predict_sentiment(st.session_state.reddit_data)
        st.success("Fetched Reddit posts! ✅")

# Display charts and data
if "reddit_data" in st.session_state and st.session_state.reddit_data is not None:
    # Sentiment Distribution Chart
    st.header("Sentiment Distribution")
    sentiment_counts = st.session_state.reddit_data["sentiment"].value_counts()

    # Plot the Pie Chart
    fig, ax = plt.subplots(figsize=(3, 3))  # Smaller size
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Sentiment Distribution")
    st.pyplot(fig)

    # Table of Fetched Posts
    st.header("Fetched Posts")
    st.dataframe(st.session_state.reddit_data)

    # Sentiment Counts
    st.subheader("Sentiment Counts")
    st.markdown(f"**Positive Comments:** {sentiment_counts.get('Positive', 0)}")
    st.markdown(f"**Neutral Comments:** {sentiment_counts.get('Neutral', 0)}")
    st.markdown(f"**Negative Comments:** {sentiment_counts.get('Negative', 0)}")
else:
    st.warning("No data available yet. Please click 'START NOW' to fetch Reddit posts.")

# Ask Genie Section
st.markdown('<div class="curved-box">', unsafe_allow_html=True)
st.subheader("Ask Genie a Question")
question = st.text_input("Your Question:")
if st.button("Ask Question"):
    with st.spinner("Wanders off into thought... I'll be right back."):

        time.sleep(2)
        gemini_raw_response = fetch_gemini_answer(question, st.session_state.reddit_data.to_string())
        st.session_state.gemini_response = format_response_with_bold(gemini_raw_response)

if "gemini_response" in st.session_state:
    st.markdown(st.session_state.gemini_response, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""<footer style="text-align: center; margin-top: 20px; color: white;">
        &copy; 2024 Reddit Stocks Genie. All rights reserved.
    </footer>""", unsafe_allow_html=True)
