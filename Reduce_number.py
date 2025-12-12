# def reduce_number(number):
#     while number > 9:
#         total = 0
#         for digit in str(number):
#             total += int(digit)
#         number = total
#     return number
# ------------------------------------------- Recursive Version
def reduce_number(n):  
    # Tek hane ise direkt dön
    if n < 10:
        return n
    
    # Basamakları topla
    total = 0
    for digit in str(n):
        total += int(digit)
    
    # Yeni toplam için tekrar fonksiyonu çağır
    return reduce_number(total)

print(reduce_number(19999999999999))        
        
        
    
    