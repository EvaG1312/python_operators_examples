web_data = ["techresearch", "computervision"]  # Sample web data

# Check if any element contains '@' or digits
if any("@" in item for item in web_data):
    print("e-mail address")
elif any(char.isdigit() for item in web_data for char in item):
    print("phone number")
else:
    print("not e-mail nor phone number")