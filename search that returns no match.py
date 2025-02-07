import re
# sample text
sample_text = "The rain in Spain"
# search for Portugal in sample text
match_result = re.search(r"Portugal", sample_text)
#check if it was found
if match_result:
    print("Portugal was found in sample")
else: 
    print("Portugal was not found in sample")