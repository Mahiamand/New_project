"""This file is all about taking a text input, detecting its languages  and  answering the questions 
of users as asked in text and returning  in the same language sent by user """

from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer
from sentence_transformers import SentenceTransformer, util

# Load the sentence transformer model
sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Pre-defined responses 
responses = {
    "hello": "Hello! How can I help you?",
    "how_are_you": "I'm good, thank you! How about you?",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure, I'm here to help. What do you need?"
}
response_texts = list(responses.values())

def load_translation_model(src_lang, tgt_lang="en"):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate(text, src_lang, tgt_lang="en"):
    tokenizer, model = load_translation_model(src_lang, tgt_lang)
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def detect_language(text):
    return detect(text)

def get_response_in_language(response_text, detected_lang):
    if detected_lang == "en":
        return response_text  # No need to translate if English
    tokenizer, model = load_translation_model("en", detected_lang)
    tokens = tokenizer(response_text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def get_best_response(user_input_in_english):
    # Compute semantic similarity between input and predefined responses
    input_embedding = sentence_model.encode(user_input_in_english, convert_to_tensor=True)
    response_embeddings = sentence_model.encode(response_texts, convert_to_tensor=True)

    # Find the most similar response
    similarities = util.cos_sim(input_embedding, response_embeddings)
    best_match_idx = similarities.argmax().item()
    return response_texts[best_match_idx]

def process_user_query(user_input):
    # Detecting the language of the input text here
    detected_lang = detect_language(user_input)
    print(f"Detected Language: {detected_lang}")

    # Translating user input to English for its internal processing
    user_input_in_english = translate(user_input, detected_lang)
    print(f"Translated Input: {user_input_in_english}")

    # Getting the best-matching response based on its similarity from above mentioend sentences
    response_text = get_best_response(user_input_in_english)

    # Translate the response back to the original language now
    final_response = get_response_in_language(response_text, detected_lang)
    return final_response

# calling the abovr functions now  : 
#¿Cuántos países hay en el mundo?
#¿Quién es el Primer Ministro de la 
# India?

user_input = "आप कैसे हैं?" #"आप कैसे हैं?"
response = process_user_query(user_input)
print(f"Bot Response: {response}")
