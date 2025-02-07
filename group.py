import re

# Sample text
sample_text = "The rain in Spain"

# Searching for a word starting with 'S' in the text
search_result = re.search(r"\bS\w+", sample_text)

# Show original group if match found
if search_result:
     print("Original groups:", search_result.group())
else:
    print("No match found.")