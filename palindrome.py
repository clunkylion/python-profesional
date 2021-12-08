
def isPalindrome(string : str) -> bool:
    #Delete whitespaces
    string = string.replace(" ", "").lower()
    return string == string[::-1]
    
def main():
    print(isPalindrome("ana"))
    
if __name__ == "__main__":
    main()