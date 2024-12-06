# **📈 Reddit Stocks Genie**  
"Reddit Stocks Genie" uses sentiment analysis and the Gemini API to provide insights into stock market trends by analyzing Reddit posts. It helps users track market sentiment and make informed decisions by querying stock-related discussions, performing real-time sentiment analysis, and generating AI-driven responses.

---

## **📜 Introduction**  
This project integrates a Jupyter Notebook for model training and a Streamlit web app for deployment. The Reddit API is used for fetching stock-related posts, while the Gemini API generates responses based on these posts. Below are detailed instructions to set up and run the project.

---

## **🚀 Step 1: Setting Up the Reddit API Key**

### **🔑 Create a Reddit API Key**
1. Follow the instructions in this Youtube video below ,click on the video to help you Generate your Reddit API keys:-
   
[![Reddit API Tutorial: How to Get Your API Keys in 2024 | Beginner's Guide](https://i.ytimg.com/an_webp/0mGpBxuYmpU/mqdefault_6s.webp?du=3000&sqp=CKr_yboG&rs=AOn4CLAhdAs-rhLGlNj4YA5cpKmuurywzg)](https://www.youtube.com/watch?v=0mGpBxuYmpU)






2. Note down the following credentials:  
   - **Client ID**  
   - **Client Secret**  
   - **User Agent**

### **📝 Insert Your Reddit API Key in Jupyter Notebook**
- Open the Jupyter Notebook file (`CapX-Reddit_stocks_genie.ipynb`).  
- Navigate to the **Data Scraping using Reddit API** section (around lines **5, 6, 7** of the relevant cell).  
- Paste your credentials in the appropriate placeholders:
- ![image](https://github.com/user-attachments/assets/a6c41217-5609-477d-8a1d-02762ad3e1fe)


```python
client_id="your-client-id"
client_secret="your-client-secret"
user_agent="your-user-agent"
```
---

## **🔮 Step 2: Setting Up the Gemini API Key**

### **🔑 Create a Gemini API Key**
1. Click on this youtube video below to help you create your gemini API key:-



    [![How to Use the Gemini API with Python - Build a Customizable AI Chatbot](https://i.ytimg.com/an_webp/-B-bp3iiCJ0/mqdefault_6s.webp?du=3000&sqp=CKCDyroG&rs=AOn4CLC0rAgqlaJPhg0JpJ1Ka9Adg7A8ww)](https://www.youtube.com/watch?v=-B-bp3iiCJ0)







     
3. Once obtained, navigate to the **Building Chatbot Q&A using Gemini API** section in the Jupyter file.  
4. Paste your Gemini API key in **line 11**:
![image](https://github.com/user-attachments/assets/0fd16be1-6727-459e-b9a3-5cbb301cd8fa)
 

```python
genai.configure(api_key="your-gemini-api-key")
```

---

## **⚙️ Step 3: Install Dependencies for Jupyter Notebook**
To run the Jupyter Notebook, install all the required Python libraries with this single command:
```python
pip install keras google-generativeai numpy pickle tensorflow seaborn matplotlib pandas textblob re praw tweepy nltk scikit-learn
```

---

## **📘 Step 4: Run the Jupyter Notebook**

### **🛠 Install Jupyter Notebook**
- Download and install the latest version of Jupyter Notebook from [Anaconda](https://www.anaconda.com/products/individual) if you don't have it installed.

### **✅ Important Cells to Run**
- **Save the trained model**:  
  ```python
  model.save('model.h5')
  ```

## **📂 Run the Notebook**
Upload the folder to Jupyter Notebook.
Execute each cell sequentially to view the final outputs.
Ensure the following files are generated:
model.h5 (~9–10 KB)
tokenizer.pickle (~12–14 KB)
![image](https://github.com/user-attachments/assets/30ada760-d10d-4e09-9aff-badcbf761107)


## **🌐 Step 5: Set Up and Run the app.py File**
🛠 Install Dependencies for Streamlit App
Run the following command to install required libraries for app.py:
 ```python
pip install streamlit praw google-generativeai pandas matplotlib pickle time base64
```

## **📝 Insert API Keys in app.py**
Open app.py.
Go to line 20 and paste your Gemini API key:
![image](https://github.com/user-attachments/assets/b66a3664-bea1-476f-837c-a405386803f2)

Go to lines 32, 33, and 34 and paste your Reddit API credentials:
![image](https://github.com/user-attachments/assets/b0210bec-cd73-463c-afc0-2a0a51341b55)



## **▶️ Run the Streamlit App**
Ensure the model.h5 and tokenizer.pickle files exist in your project folder.
Open a terminal, navigate to the project directory, and run:
 ```python
streamlit run app.py
```

![image](https://github.com/user-attachments/assets/215f86a8-3307-4938-b3fd-130e9d390c2b)

## **📋 Conclusion**
By following these steps, you will successfully run the Reddit Stocks Genie project. First, set up the Reddit and Gemini API keys, install dependencies, train the model using the Jupyter Notebook, and finally deploy the Streamlit web app. This project provides valuable insights into stock market trends using sentiment analysis and AI-driven responses.

## **💡 Need Help?**
Watch My demo video by click on the video below:- 




[![CapX Reddit Stocks Genie Project Submission](https://i.ytimg.com/an_webp/Kig7WBeLMN4/mqdefault_6s.webp?du=3000&sqp=COiDyroG&rs=AOn4CLC-4DhQzcfx0ZFJONcOTPEjCGpqSg)](https://www.youtube.com/watch?v=Kig7WBeLMN4)







Contact me via email at saviorithik@gmail.com or phone at +91 9840955320.

Note: The API keys provided in the repository are disabled. Please use your own credentials.



