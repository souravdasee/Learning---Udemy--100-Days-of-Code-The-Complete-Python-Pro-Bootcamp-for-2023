def format_name(f_name, l_name):
    formatted_f_name = f_name.title()   #know more about .title() at > https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("sOuRAv", "dAS"))