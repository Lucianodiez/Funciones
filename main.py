def double_letter(str):
    result = ''
    for letter in str:
        result += letter 
    print(result)
    return result

def secret_function(a, b):
    print(a,b)
    return " "

print(double_letter("Hola"))
print(secret_function(1,2))
print(secret_function("¡Hola, ", "Mundo!"))
