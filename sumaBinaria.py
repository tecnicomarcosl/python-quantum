def decimal_to_binary(decimal_number, n_bits):
    # Convertir el número decimal a binario y eliminar el prefijo '0b'
    binary_string = bin(decimal_number)[2:]
    # Ajustar la longitud del número binario agregando ceros a la izquierda si es necesario
    binary_string = binary_string.zfill(n_bits)
    return binary_string

def binary_addition(a, b):
    max_length = max(len(a), len(b))  # Determinar la longitud máxima de las cadenas binarias
    a = a.zfill(max_length)  # Ajustar la longitud de 'a' agregando ceros a la izquierda si es necesario
    b = b.zfill(max_length)  # Ajustar la longitud de 'b' agregando ceros a la izquierda si es necesario
    
    carry = 0  # Inicializar el acarreo como 0
    result = []  # Lista para almacenar los dígitos del resultado

    # Recorrer las cadenas binarias de derecha a izquierda
    for i in range(max_length - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry  # Sumar los dígitos actuales y el acarreo
        result.append(str(bit_sum % 2))  # Agregar el dígito resultante al resultado
        carry = bit_sum // 2  # Actualizar el acarreo para la siguiente iteración

    if carry:
        result.append('1')  # Agregar un '1' al resultado si hay un acarreo final
    
    result.reverse()  # Revertir el resultado para obtener la suma correcta
    return ''.join(result)  # Convertir la lista de dígitos a una cadena

def binary_to_decimal(binary_string):
    decimal = int(binary_string, 2)
    return decimal

# Definir los números de entrada en formato decimal
a_decimal = 5
b_decimal = 52

# Definir la cantidad de bits para representar los números binarios
n_bits = max(a_decimal.bit_length(), b_decimal.bit_length())  # Obtener el máximo de bits requeridos

# Convertir los números de entrada a binario
a_binary = decimal_to_binary(a_decimal, n_bits)
b_binary = decimal_to_binary(b_decimal, n_bits)

# Realizar la suma binaria
binary_result = binary_addition(a_binary, b_binary)

# Convertir el resultado de la suma de binario a decimal
decimal_result = binary_to_decimal(binary_result)

# Mostrar los resultados
print("Número a (decimal):", a_decimal)
print("Número b (decimal):", b_decimal)
print("Resultado de la suma (binario):", binary_result)
print("Resultado de la suma (decimal):", decimal_result)
