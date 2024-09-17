def are_anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    if len(string1) != len(string2):
        return False
    
    return sorted(string1) == sorted(string2)

string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
print(are_anagrams(string1, string2))
