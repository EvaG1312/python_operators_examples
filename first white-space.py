import re

# Sample text
sample_text = "The rain in Spain"

# Search for the first whitespace character
match_result = re.search(r"\s", sample_text)

# Check if a match was found
if match_result:
    print(f"The first white-space character is located at position: {match_result.start()}")
else:
    print("No white-space character found.")