# Step 1 
 # User enters text, .lower() makes the text all lowercase
# User picks random letters to count in the text
text1 = input("Enter text:").lower() 
text2 = input("Three random letters?:").lower()  

# Step 2
#find length of text
print(f"Number of characters in the text: {len(text1)}") 

# Counts how many times the random letters appear in text1 from text2
#count letters
count = {letter: text1.count(letter) for letter in text2}  
print("Count of letters:", count)  

# Step 3
 # Gets the first letter of text1 if it's not empty
first_letter = text1[0] 
print("First letter of the text:",{first_letter})

last_letter = text1[-1]
print("Last letter of the text:", {last_letter})

# Step 4
# Reverses the text
reversed_text = text1[::-1]  
print("Reversed text:", reversed_text)

# Step 5
# Print if 'python' is in the text
if "python" in text1:
    print("Python is in the text.")  
else:
    print("Python is not in the text.")

