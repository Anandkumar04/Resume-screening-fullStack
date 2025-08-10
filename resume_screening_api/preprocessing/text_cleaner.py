import re
import nltk
from nltk.corpus import stopwords
import string

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def clean_resume(resume_text):
    """
    Clean resume text by removing URLs, mentions, hashtags, punctuation, 
    and extra whitespace.
    
    Args:
        resume_text (str): Raw resume text
        
    Returns:
        str: Cleaned resume text
    """
    # Remove URLs
    resume_text = re.sub('http\S+\s*', ' ', resume_text)
    
    # Remove RT and cc
    resume_text = re.sub('RT|cc', ' ', resume_text)
    
    # Remove hashtags
    resume_text = re.sub('#\S+', '', resume_text)
    
    # Remove mentions
    resume_text = re.sub('@\S+', '  ', resume_text)
    
    # Remove punctuations
    resume_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resume_text)
    
    # Remove non-ASCII characters
    resume_text = re.sub(r'[^\x00-\x7f]', r' ', resume_text) 
    
    # Remove extra whitespace
    resume_text = re.sub('\s+', ' ', resume_text)
    
    return resume_text.strip()

def remove_stopwords(text):
    """
    Remove stopwords from text
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text without stopwords
    """
    stop_words = set(stopwords.words('english') + ['``', "''"])
    words = nltk.word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words and word not in string.punctuation]
    return ' '.join(filtered_words)

def preprocess_resume(resume_text):
    """
    Complete preprocessing pipeline for resume text
    
    Args:
        resume_text (str): Raw resume text
        
    Returns:
        str: Fully preprocessed resume text
    """
    # Clean the text
    cleaned_text = clean_resume(resume_text)
    
    # Remove stopwords (optional - might not be needed for TF-IDF)
    # processed_text = remove_stopwords(cleaned_text)
    
    return cleaned_text
