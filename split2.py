import re

# Sample text
sample_text = "The rain in Spain"

# Splitting the text at the first whitespace only
split_results = re.split(r"\s", sample_text, maxsplit=1)

# Showing split text
print(split_results)