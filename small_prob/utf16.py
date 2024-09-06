def utf16_value(str_input):
    utf16_value = 0
    
    for char in str_input:
        char_value = ord(char)
        utf16_value += char_value
        
    return utf16_value
    
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)