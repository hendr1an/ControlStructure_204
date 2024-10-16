def fibbonacci(n):
    a, b = 0, 1
    result = []
    for _ in range (n): 
        result.append(a)
        a, b = b, a + b
    return result

n = int (input("Masukkan Nilai N: "))
print("Bilangan Fibonacci sampai ke", n, ":", fibbonacci(n))