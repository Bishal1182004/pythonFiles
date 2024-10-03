from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai
import apikey

# Load your API key from the environment or directly
API_KEY = apikey.api_keys
genai.configure(api_key=API_KEY)

# Define the template

# Google Gemini configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 1024,
}

def parse_with_gemini(dom_chunks, parse_description):
    template = f"""
        You are tasked with extracting specific information from the following text content: {dom_chunks}. 
        Please follow these instructions carefully:

        1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. 
        2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. 
        3. **Empty Response:** If no information matches the description, return an empty string ('').
        4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
        """



    parsed_results = []

    # Generate prompt using template and description
    prompt_template = template

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = prompt_template.format({"dom_content": chunk, "parse_description": parse_description})

        # Make the request to the Google Gemini API
        response = genai.generate_text(
            prompt=prompt,
            generation_config=generation_config
        )

        if 'text' in response:
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
            parsed_results.append(response["text"])
        else:
            print(f"Error parsing batch {i}: No text returned")
            parsed_results.append("")

    return "\n".join(parsed_results)

# Example of how to use the function:
# dom_chunks = ["chunk1", "chunk2"]  # Split your DOM content into chunks
# parse_description = "Extract specific information"
# result = parse_with_gemini(dom_chunks, parse_description)
# print(result)
