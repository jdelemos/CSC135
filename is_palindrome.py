def is_palindrome(words):
    a = 1
    for i in range(len(words)//2):
        if words[i] == words[len(words)-1-i]:
            a = 0
        else:
            return False
    return True

words = ["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"]
result = is_palindrome(words)
print(result)
