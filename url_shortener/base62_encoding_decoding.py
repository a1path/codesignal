# base62 encoding
# import string

# CHARS =  string.digits + string.ascii_lowercase + string.ascii_uppercase
CHARS="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(CHARS)

def base62_encode(num):
    """Encodes a number using Base62 encoding."""
    if num == 0:
        return CHARS[0]
    encoding = ''
    while num > 0:
        num, remainder = divmod(num, 62)
        encoding = CHARS[remainder] + encoding
        print(f"num:{num}, remainer:{remainder}, encoding:{encoding}")
    return encoding

def base62_decode(s):
    """Decodes a Base62 string back into a number."""
    num = 0
    for char in s:
        value = CHARS.index(char)
        num = num * 62 + value
        print(f"char:{char}, value:{value}, num:{num}")
    return num

# Demo
num = 10000000
encoded = base62_encode(num)
print("Encoded:", encoded)

decoded = base62_decode(encoded)
print("Decoded:", decoded)


# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# num:161290, remainer:20, encoding:k
# num:2601, remainer:28, encoding:sk
# num:41, remainer:59, encoding:Xsk
# num:0, remainer:41, encoding:FXsk
# Encoded: FXsk
# char:F, value:41, num:41
# char:X, value:59, num:2601
# char:s, value:28, num:161290
# char:k, value:20, num:10000000
# Decoded: 10000000