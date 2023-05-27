# Importing needed libraries
import fitz
import openai
import nltk   # natural language took kit
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
#from nltk.tokenize import word_tokenize
import re
import warnings
warnings.filterwarnings('ignore')


# Text summarizer
#import spacy 
#from spacy.lang.en.stop_words import STOP_WORDS
#nlp = spacy.load('en_core_web_sm')
#from string import punctuation
#file = open('chapter-4.pdf')

openai.api_key = "API_Key"

def read_pdf_to_text(input_document):
    text = ''
    document = fitz.open(input_document)  # Enter the document path here
    page_count = document.page_count
    print(page_count)   # prints the total no.of pages in the PDF doc
    
    for i in range(page_count):
        p = document.load_page(i)  
        pages = p.get_text()   # Extract text from the PDF
        text += pages 
        return text    

def preprocess_text(text_string):
    #text = re.sub(r'[!"#$%&\'()*+,-./:;?@[\\]^_{|}~`�]', '', text) # Remove punctuations
    text = re.sub(r'\n+', ' ', text_string)                          # multiple line breaks removal 
    text = re.sub(r'\s+', ' ', text)                                 # multiple spaces removal
    text = re.sub(r'Rationalised 2023-24', '', text)                 # Remove Footer
    text = re.sub(r'Fig. [0-9]', '', text)                           # To remove unwanted text
    text_edited = text.lower()                                       #Convert to all strings to lower case
    return text_edited


def sentence_tokenize(text_edited):
    sent_token = sent_tokenize(text_edited)
    
    # The sent_tokenize returns list. To convert it ro string
    sent_token_string = ''
    for i in range(len(sent_token)):
        sent_token_string += sent_token[i]

    return sent_token_string

#word tokenization:
# word_token = word_tokenize(sent_token_string)
# print(len(word_token))

def chat_with_chatgpt(prompt): 
    response = openai.Completion.create(
        engine = 'text-davinci-003', #'gpt-3.5-turbo'
        prompt = prompt,
        max_tokens=500
        #temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

def get_mca_questions(sent_token_string):
    if isinstance(sent_token_string, str) == True:      # Check for string 
        input_prompt = 'Generate 2 MCQ questions with two correct options as answers and display both the correct answers'
        prompt = sent_token_string + input_prompt
        questions = chat_with_chatgpt(prompt)
    else:
        questions = "The input is String. It is in " + f'{type(sent_token_string)}' 

    return questions

def main():
    
    input_document = 'chapter-4.pdf'  # Enter the input document path 

    #Step 1: Function to read the PDF using PyMuPDF library
    text_string = read_pdf_to_text(input_document)

    #Step 2: Preprocess the text
    text_edited = preprocess_text(text_string)
    
    #Step 3: Sentence tokenization
    sent_token_string = sentence_tokenize(text_edited)

    #Step 4: To get the questions using LLM - GPT-3
    questions = get_mca_questions(text_edited)

    print(questions)
    print(type(questions))

    # questions_edited = re.sub(r'\n\n+', '\n', questions) 
    # questions_edited = questions_edited.splitlines()
    # print(questions_edited)

main()

#--------------------------------------------------------------------------------------------------------------------------------
# Dependencies to be installed while executing this code:
#pip install PyMuPDF
#pip install openai
#pip install nltk
#---------------------------------------------------------------------------------------------------------------------------------




