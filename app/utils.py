import re

def clean_text(text):
    text = re.sub(r'[^>]*?','',text) # for HTML tags
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|www\.[a-zA-Z0-9.-]+','',text) # for removing urls
    text = re.sub(r'[^a-zA-Z0-9\s]','',text) #remove special characters
    text = re.sub(r'\s+',' ',text) #remove multiple sapces
    text = text.strip() # trim leading and tailing spaces
    text = ' '.join(text.split())

    return text
