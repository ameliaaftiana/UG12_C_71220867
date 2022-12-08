awal=input("Masukkan Kata atau Angka: ")
def reversed_string(text):
    result = ""
    for char in awal:
        result = char + result
    return result

print(reversed_string(awal))
