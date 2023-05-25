# MCQs_Generation

Step 1 : A PDF is taken as input.

Step 2 : Text from the pdf is extarcted using PyMuPDF.

Step 3 : Text pre_processing Steps are done using regex (Regular Expression):
    1) Punctuation Removal
    2) Un_necessary spaces removal
    3) New lines removes
    4) Un_necessary text which are the footer of the pages have been removed.
    5) Converted all the string to lower case.
    
Step 4 :Followed by sentence tokenization - To extract sentences from the paragraph.

Step 5 : Next in the line is providing the prompt text as input to the model text-davinci-003 which is a GPT 3.5 series LLM model using Completion API
          and get back the response.
  



