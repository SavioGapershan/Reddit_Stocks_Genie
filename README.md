# Reddit_Stocks_Genie
 "Reddit Stocks Genie," uses sentiment analysis and the Gemini API to provide insights into stock market trends by analyzing Reddit posts. It allows users to track market sentiment and make informed decisions by querying stock-related discussions, providing real-time sentiment analysis, and generating context-based responses using the Gemini model.

**Introduction**
This README provides the steps required to run the Reddit Stocks Genie project, which includes both a Jupyter Notebook for data processing and a Streamlit web app for interactive querying. The project uses Reddit API for fetching stock-related posts and the Gemini API for generating answers based on those posts. Below are the instructions for setting up and running both the Jupyter Notebook and the Streamlit app.

**Step 1:Setting Up the Reddit API Key**
**Create a Reddit API Key**:

Follow the instructions in this YouTube video {_"https://www.youtube.com/watch?v=0mGpBxuYmpU_"} to create a Reddit API key.
**You will need the following credentials:**

 [ Client ID,
Client Secret,
User Agent ]

**Insert Your Reddit API Key in Jupyter Notebook:**

Open the Jupyter Notebook file (CapX-Reddit_stocks_genie.ipynb).
Navigate to the Data Scraping using Reddit API section (around lines 5,6,7 of this cell).
Paste your Client ID, Client Secret, and User Agent in the relevant places in the cell.
![image](https://github.com/user-attachments/assets/88e199ea-fd7e-44a0-affd-a0feb9774f64)



**Gemini API Key Setup:**

Follow the instructions in this YouTube video {"_https://www.youtube.com/watch?v=-B-bp3iiCJ0&t=33s_"} to create your Gemini API key.
Once you have the key, open the Building Chatbot Q&A using Gemini API section in the Jupyter file and paste your Gemini API key in the respective line (line 11 og this cell).
![image](https://github.com/user-attachments/assets/c93fa14f-caff-49ad-b4a5-77dab49eeae7)


**Step 2: Install Dependencies for Jupyter Notebook**
To run the Jupyter Notebook, you will need to install the following Python libraries. Run the following command to install all required packages:

pip install keras google-generativeai numpy pickle tensorflow seaborn matplotlib pandas textblob re praw tweepy nltk scikit-learn 

**Step 3: Run the Jupyter Notebook**
if you dont have Jupyter , Install Jupyter Notebook:

Download the latest version of Jupyter Notebook from Anaconda and install it if you haven't already.
Important Cells to Run:

Run the cell that saves the trained model: model.save('model.h5').
Run the cell that saves the tokenizer: pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL).
Execute the Evaluation Section properly to save the model and tokenizer files.
Run the Notebook:

Upload your folder to Jupyter Notebook and run each cell sequentially to view the final outputs.

**Step 4: Set Up and Run the app.py File** 
**Ensure Generated Files Exist:**

After running the Jupyter Notebook, ensure the following files are generated:
model.h5 (approximately 9-10 KB)
tokenizer.pickle (approximately 12-14 KB)
![image](https://github.com/user-attachments/assets/6b678bd1-0c18-4c0f-acab-5043868ca3c6)

Install Streamlit and Required Libraries: Run the following command to install the dependencies for the app:

pip install streamlit praw google-generativeai pandas matplotlib pickle time base64

**Insert API Keys in app.py:**

Open the app.py file.
Go to line 20 and paste your Gemini API key.
![image](https://github.com/user-attachments/assets/7a812e37-91ff-4fea-80e6-b08eb3bf143f)
Go to lines 32, 33, and 34 in app.py and paste your Reddit API keys (Client ID, Client Secret, and User Agent).
![image](https://github.com/user-attachments/assets/bb2f32cf-2caf-4123-bd01-2c5a7e79cfcc)

**Run the Streamlit App:**

To run the app, you can use VSCode or open the terminal.

In the terminal, navigate to your project folder and run:
streamlit run app.py
![image](https://github.com/user-attachments/assets/7ab03d8e-6c96-4c8a-9e04-d2186fc43cfd)

Also if some problems are occuring in the static or templates folder , you are welcomed to change the directory in the respective lines of the app.py (75h line),
![image](https://github.com/user-attachments/assets/560c106c-cc43-4441-850a-df84e50fb2fc)


**Conclusion**
By following the steps outlined above, you will be able to run the Reddit Stocks Genie project. First, set up the Reddit and Gemini API keys, install the necessary dependencies, run the Jupyter notebook to train the model, and then run the app.py file to deploy the Streamlit web app. This project provides insights into stock market trends using sentiment analysis and AI-driven responses from Reddit posts.

if you have any more doubts , or want to watch a demonstration you can watch my Youtube video :- {"_https://www.youtube.com/watch?v=Kig7WBeLMN4&t=198s_"}

or even you can mail me here saviorithik@gmail.com or even can reach out to me through my number +919840955320

DW You cant use my API Key I Have Disabled it :)
