# from flask import Flask
# from flask_socketio import SocketIO, emit
# from langdetect import detect
# from transformers import MarianMTModel, MarianTokenizer
# from sentence_transformers import SentenceTransformer, util

# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Load the sentence transformer model
# sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# # Predefined responses
# responses = {
#     "hello": "Hello! How can I help you?",
#     "how_are_you": "I'm good, thank you! How about you?",
#     "bye": "Goodbye! Have a nice day!",
#     "help": "Sure, I'm here to help. What do you need?",
#     "who_is_prime_minister_of_india": "The Prime Minister of India is Narendra Modi.",
#     "how_many_countries_are_there_in_world": "There are 195 countries in the world.",
#     "what_is_your_name": "I am Nora, a chatbot.",
#     "what_is_my_favourite_color": "My favourite color is white and black."
# }

# response_texts = list(responses.values())
# response_keys = list(responses.keys())

# def load_translation_model(src_lang, tgt_lang="en"):
#     model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
#     tokenizer = MarianTokenizer.from_pretrained(model_name)
#     model = MarianMTModel.from_pretrained(model_name)
#     return tokenizer, model

# def translate(text, src_lang, tgt_lang="en"):
#     tokenizer, model = load_translation_model(src_lang, tgt_lang)
#     tokens = tokenizer(text, return_tensors="pt", padding=True)
#     translated = model.generate(**tokens)
#     return tokenizer.decode(translated[0], skip_special_tokens=True)

# def detect_language(text):
#     return detect(text)

# def get_response_in_language(response_text, detected_lang):
#     if detected_lang == "en":
#         return response_text
#     tokenizer, model = load_translation_model("en", detected_lang)
#     tokens = tokenizer(response_text, return_tensors="pt", padding=True)
#     translated = model.generate(**tokens)
#     return tokenizer.decode(translated[0], skip_special_tokens=True)

# def get_best_response(user_input_in_english):
#     input_embedding = sentence_model.encode(user_input_in_english, convert_to_tensor=True)
#     response_embeddings = sentence_model.encode(response_texts, convert_to_tensor=True)
#     similarities = util.cos_sim(input_embedding, response_embeddings)
#     best_match_idx = similarities.argmax().item()
#     return response_texts[best_match_idx]

# def process_user_query(user_input):
#     detected_lang = detect_language(user_input)
#     user_input_in_english = translate(user_input, detected_lang)

#     user_input_key = user_input_in_english.lower().replace(" ", "_")
#     if user_input_key in responses:
#         response_text = responses[user_input_key]
#     else:
#         response_text = get_best_response(user_input_in_english)

#     final_response = get_response_in_language(response_text, detected_lang)
#     return final_response

# @socketio.on('user_input')
# def handle_user_input(data):
#     user_input = data['input']
#     response = process_user_query(user_input)
#     emit('response', {'response': response})

# if __name__ == "__main__":
#     socketio.run(app, host='0.0.0.0', port=5000)


# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# from langdetect import detect
# from transformers import MarianMTModel, MarianTokenizer
# from sentence_transformers import SentenceTransformer, util
# import os

# app = Flask(__name__, static_folder=".", static_url_path="")
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Load the sentence transformer model
# sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# # Predefined responses
# responses = {
#     "hello": "Hello! How can I help you?",
#     "how_are_you": "I'm good, thank you! How about you?",
#     "bye": "Goodbye! Have a nice day!",
#     "help": "Sure, I'm here to help. What do you need?",
#     "who_is_prime_minister_of_india": "The Prime Minister of India is Narendra Modi.",
#     "how_many_countries_are_there_in_world": "There are 195 countries in the world.",
#     "what_is_your_name": "I am Nora, a chatbot.",
#     "what_is_my_favourite_color": "My favourite color is white and black."
# }

# response_texts = list(responses.values())
# response_keys = list(responses.keys())

# def load_translation_model(src_lang, tgt_lang="en"):
#     model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
#     tokenizer = MarianTokenizer.from_pretrained(model_name)
#     model = MarianMTModel.from_pretrained(model_name)
#     return tokenizer, model

# def translate(text, src_lang, tgt_lang="en"):
#     tokenizer, model = load_translation_model(src_lang, tgt_lang)
#     tokens = tokenizer(text, return_tensors="pt", padding=True)
#     translated = model.generate(**tokens)
#     return tokenizer.decode(translated[0], skip_special_tokens=True)

# def detect_language(text):
#     return detect(text)

# def get_response_in_language(response_text, detected_lang):
#     if detected_lang == "en":
#         return response_text
#     tokenizer, model = load_translation_model("en", detected_lang)
#     tokens = tokenizer(response_text, return_tensors="pt", padding=True)
#     translated = model.generate(**tokens)
#     return tokenizer.decode(translated[0], skip_special_tokens=True)

# def get_best_response(user_input_in_english):
#     input_embedding = sentence_model.encode(user_input_in_english, convert_to_tensor=True)
#     response_embeddings = sentence_model.encode(response_texts, convert_to_tensor=True)
#     similarities = util.cos_sim(input_embedding, response_embeddings)
#     best_match_idx = similarities.argmax().item()
#     return response_texts[best_match_idx]

# def process_user_query(user_input):
#     detected_lang = detect_language(user_input)
#     user_input_in_english = translate(user_input, detected_lang)

#     user_input_key = user_input_in_english.lower().replace(" ", "_")
#     if user_input_key in responses:
#         response_text = responses[user_input_key]
#     else:
#         response_text = get_best_response(user_input_in_english)

#     final_response = get_response_in_language(response_text, detected_lang)
#     return final_response

# # Serve index.html at the root URL
# @app.route('/')
# def index():
#     return app.send_static_file("index.html")

# @socketio.on('user_input')
# def handle_user_input(data):
#     user_input = data['input']
#     response = process_user_query(user_input)
#     emit('response', {'response': response})

# if __name__ == "__main__":
#     socketio.run(app, host='0.0.0.0', port=5000)


from flask import Flask
from flask_socketio import SocketIO, emit
from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer
from sentence_transformers import SentenceTransformer, util
import sentencepiece

app = Flask(__name__, static_folder=".", static_url_path="")
socketio = SocketIO(app, cors_allowed_origins="*")

# Load the sentence transformer model
sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "how_are_you": "I'm good, thank you! How about you?",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure, I'm here to help. What do you need?",
    "who_is_prime_minister_of_india": "The Prime Minister of India is Narendra Modi.",
    "how_many_countries_are_there_in_world": "There are 195 countries in the world.",
    "what_is_your_name": "I am Nora, a chatbot.",
    "what_is_my_favourite_color": "My favourite color is white and black."
}

response_texts = list(responses.values())
response_keys = list(responses.keys())

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
        return response_text
    tokenizer, model = load_translation_model("en", detected_lang)
    tokens = tokenizer(response_text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def get_best_response(user_input_in_english):
    input_embedding = sentence_model.encode(user_input_in_english, convert_to_tensor=True)
    response_embeddings = sentence_model.encode(response_texts, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, response_embeddings)
    best_match_idx = similarities.argmax().item()
    return response_texts[best_match_idx]

def process_user_query(user_input):
    detected_lang = detect_language(user_input)
    user_input_in_english = translate(user_input, detected_lang)

    user_input_key = user_input_in_english.lower().replace(" ", "_")
    if user_input_key in responses:
        response_text = responses[user_input_key]
    else:
        response_text = get_best_response(user_input_in_english)

    final_response = get_response_in_language(response_text, detected_lang)
    return final_response

@app.route('/')
def index():
    return app.send_static_file("index.html")

@socketio.on('user_input')
def handle_user_input(data):
    user_input = data['input']
    response = process_user_query(user_input)
    emit('response', {'response': response})

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)

