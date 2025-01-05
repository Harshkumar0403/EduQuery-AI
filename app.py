from gen_ai import qa_chain, document
import streamlit as st




def generate_response(input_documents, question):
    
    raw_response = qa_chain.run(input_documents=input_documents, question=question)

    # Process the response into the desired format
    processed_response = f"Here are related best searches for you:\n{raw_response}"
    return processed_response


def main():
    # Title and description
    st.title("Analytics Vidya Chatbot")
    st.write("""
        Welcome to the Analytics Vidya Q&A Chatbot! 
        Enter your question below, and the I will provide course-related answers.
        """)

    # Input: User's question
    question = st.text_input("Ask your question:")

    if st.button("Get Answer"):
        if question.strip():
            with st.spinner("Generating your answer..."):
                # Call the response function
                response = generate_response(input_documents=[document], question=question)
                st.success("Here's your answer:")
                st.write(response)
        else:
            st.warning("Please enter a question!")

# Run the Streamlit app
if __name__ == "__main__":
    main()

