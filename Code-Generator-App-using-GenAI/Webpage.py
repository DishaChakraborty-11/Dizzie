import streamlit as st
import google.generativeai as genai

api_key = "YOUR_API_KEY"

GOOGLE_API_KEY = api_key

genai.configure(api_key=GOOGLE_API_KEY)
st.set_page_config(page_title="Code Generator")

model = genai.GenerativeModel("gemini-1.5-pro")

def generator(programming_language):
    
    st.markdown(f"""
    <div style="text-align: center;">
        <h1>{programming_language} Code Generator</h1>
        <h3>I can generate {programming_language} code for you!</h3>
        <h4>With Explanation as well!!!</h4>
        <p>This tool generates {programming_language} code based on your plain English description.</p>
    </div>    
    """, unsafe_allow_html=True)

    # Input area for plain English descrisption
    text_input = st.text_area(f"Enter your {programming_language} code description in Plain English:")

    submit = st.button(f"Generate {programming_language} Code")

    if submit:
        if text_input.strip() == "":
            st.warning("Please enter a valid query description.")
        else:
            with st.spinner(f"Generating {programming_language} code..."):
                
                # Template that you use to generate code
                template = f"""
                    Create a {programming_language} code snippet to execute based on the following description:

                    Description: {text_input}

                    Output: {programming_language} code to generate the wanted program from the description.
                """
                
                formatted_template = template.format(text_input=text_input)
                response = model.generate_content(formatted_template)

                with st.container():
                    st.success(f"{programming_language} Code generated successfully! Here is your code below:")
                
                generated_code = response.text
                st.code(generated_code, language=programming_language.lower())  # Use the appropriate language for syntax highlighting

                        # Clean up the generated code (if needed)
        
                generated_code = generated_code.strip().lstrip("```").rstrip("```")

                        # Now, generate the explanation for the code
                explanation = f"""
                            Explain this {programming_language} code:
                            {generated_code}
                            Please provide the simplest of explanations after the code, not in the code box!:
                        """

                explanation_formatted = explanation.format(generated_code=generated_code)
                explanation_response = model.generate_content(explanation_formatted)
                explanation_text = explanation_response.text
                st.write(explanation_text)



# Use st.radio to create navigation to different pages
page = st.radio("Select a language", ["🐍 Python 🐍", "🦬 Javascript 🦬", "🦣 Java 🦣", "🦍 C# 🦍","🦏 C++ 🦏","🕸 C 🕸", "🐦‍🔥 SQL 🐦‍🔥", "🦩 R 🦩","🐎 Go 🐎"])

    # Handle what happens when buttons in each section are clicked

if page == "🐍 Python 🐍":
    generator("Python")

elif page == "🦬 Javascript 🦬":
    generator("Javascript")

elif page == "🦣 Java 🦣":
    generator("Java")

elif page == "🦍 C# 🦍":
    generator("C#")

elif page == "🦏 C++ 🦏":
    generator("C++")

elif page == "🕸 C 🕸":
    generator("C")

elif page == "🐦‍🔥 SQL 🐦‍🔥":
    generator("SQL")

elif page == "🦩 R 🦩":
    generator("R")

elif page == "🐎 Go 🐎":
    generator("Go")

