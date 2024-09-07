def longest_palindrome_divide_conquer(s: str) -> str:
    if len(s) <= 1:
        return s
    
    def find_longest_palindrome(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    
    for i in range(len(s)):
        # Caso 1: Palíndromo de longitud impar (como "aba")
        odd_palindrome = find_longest_palindrome(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Caso 2: Palíndromo de longitud par (como "bb")
        even_palindrome = find_longest_palindrome(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

# Ejemplos:
print(longest_palindrome_divide_conquer("babad"))  # Salida: "bab" o "aba"
print(longest_palindrome_divide_conquer("cbbd"))   # Salida: "bb"
print(longest_palindrome_divide_conquer("marasrrsaiana"))   # Salida: "ana"

