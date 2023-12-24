def format_list(x):
    if len(x) == 0:
        return ""
    elif len(x) == 1:
        return x[0]
    else:
        last_item = "and " + x[-1]
        other_x = ", ".join(x[:-1])
        return other_x + ", " + last_item

# Ejemplo de uso
spam = ['apples', 'bananas', 'tofu', 'cats']
formatted_string = format_list(spam)
print(formatted_string)