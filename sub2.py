import re

# Sample text
sample_text = "The rain in Spain"

# Replace the first two whitespace characters with '9'
sub_results = re.sub(r"\s", "9", sample_text, count=2)

# Show modified text
print(sub_results)