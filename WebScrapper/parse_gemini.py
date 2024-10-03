import google.generativeai as genai
import apikey


def gemini_calling(cleaned_content, parse_description):
# Directly set the API key (replace with your actual API key)
  api_key = apikey.api_keys

  # Configure the API key
  genai.configure(api_key=api_key)

  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 2048,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  template = f"""
    You are tasked with extracting specific information from the following text content: {cleaned_content}. 
    Please follow these instructions carefully:

    1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. 
    2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. 
    3. **Empty Response:** If no information matches the description, return an empty string ('').
    4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
    """


  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", 
                                generation_config=generation_config,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[])


  convo.send_message(template)
  result = convo.last.text
  return result


print(gemini_calling(cleaned_content="amazon", parse_description= "can you name 5 products "))