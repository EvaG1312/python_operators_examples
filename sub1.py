import re
# sample text
sample_text = "The rain in Spain"
# Replace each whitespace character with '9'
sub_results = re.sub(r"\s", "9",sample_text)
# show sub text
print(sub_results)