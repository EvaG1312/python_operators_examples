import re

# Sample text
sample_text = "The rain in Spain"

# Searching for a word starting with 'S' and its position
search_result = re.search(r"\bS\w+", sample_text)

# Show results only if a match is found
if search_result:
    print(search_result.span())
else:
    print("No match found.")