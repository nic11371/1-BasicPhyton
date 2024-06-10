def is_palindrome(word):
    word_receive = ""
    count = len(word) - 1
    while count >= 0:
        word_receive += word[count]
        count -=1
    if word == word_receive:
        return True
    else:
        return False




print(is_palindrome('radar'))