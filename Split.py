import re
# sample text
sample_text = "The rain in Spain"
# spliting the text into each word
split_results = re.split(r"\s", sample_text)
#showing split text 
print(split_results)