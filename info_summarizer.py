# Description:
# News summarizer of paragraphs 
import sys                                                   # Arguments parsing
from bs4 import BeautifulSoup                                # Web scraping
from gensim.summarization.summarizer import summarize        # Summirizer 
from gensim.summarization import 

# Exception handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error! Bad URL")

# Extracting text from paragraph -> <p> tag
def get_paragaph(url):
    # Returning the title of the article
    page = get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    title = ' '.join(map.title.stripped_strings)
    return title, text

# Printing the content 
print ("Title : " + text[0])        
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))

# Print length of the text
print("\n\nLength of the summarized text: " + str(len(str.split((summarize(repr(text[1]), word_count=100)))))

# Summirizing with a ratio
summarized_text = summarize(repr(text[1], ratio=0.1))