def factorial(num):
    # Checa cenários especiais
    if not isinstance(num, int) or num < 0:
        return None
    if num == 0:
        return 1
    
    # Faz a operação fatorial
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    return fact
