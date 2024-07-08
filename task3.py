import re
def normalize_phone(phone_number):
    pattern = r"[^+\d]"
    clean_text = re.sub(pattern, "", phone_number)

    have_code = r"^\+38\d*"
    start_with_plus = r"^\+"
    if not re.search(start_with_plus, clean_text):
        clean_text = '+' + clean_text

    if not re.search(have_code, clean_text):
        clean_text = clean_text.replace("+", "+38")
    
    return clean_text



print(normalize_phone("38050-111-22-22"))




