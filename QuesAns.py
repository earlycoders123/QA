# 📚 Import Libraries
import streamlit as st
import google.generativeai as genai

# 🔑 Gemini API Key Setup (Replace YOUR_API_KEY_HERE)
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")

# 🎯 Load Gemini Model
model = genai.GenerativeModel('gemini-2.5-pro')

# 🏠 Streamlit App Setup
st.set_page_config(page_title="AI Question Answering Tool", page_icon="💬")
st.title("💬 AI Question Answering Tool (Powered by Gemini)")
st.write("Ask anything, and Gemini AI will answer!")

# 📝 Input Box for Question
user_question = st.text_input("❓ Type your question here:")

# 🚀 When Button Clicked
if st.button("Get Answer"):
    if user_question.strip() != "":
        with st.spinner("Thinking..."):
            response = model.generate_content(user_question)
            answer = response.text
            st.success("Here's the Answer:")
            st.write(answer)
    else:
        st.warning("Please type a question!")

# 📎 Footer
st.caption("Made with ❤️ using Streamlit & Gemini AI")
