def StringChallenge(str):
    # Convert the string to lowercase
    str = str.lower()
    
    # Create a set of all the unique letters in the alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Create a set of all the unique letters in the string
    letters = set(c for c in str if c.isalpha())
    
    # Check if all the letters in the alphabet are in the string
    return 'true' if alphabet.issubset(letters) else 'false'


print(StringChallenge("abcdefghijklmnopqrstuvwxyyyy"))  # Output: false
print(StringChallenge("abc123456kmo"))  # Output: false
print(StringChallenge("zacxyjbbkfgtbhdaielqrm45pnsowtuv"))  # Output: true
