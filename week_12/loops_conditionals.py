
# ask user for quiz scores from a group of students
scores = int(input("What are quiz scores from the students?")) 
#asking the user for their test scores

for i in range(scores):
    if 90 <= scores <= 100: #if scores are 90 or above, print excellent
        print("Excellent!")
    elif 50 <= scores < 90: # if score is less then 90 but greater then or equal to 50 print good
        print("Good")
    else:
        print("Failing") #below a score of 50, print failing


Observations:
The problem requires inputting multiple quiz scores and counting how many are "excellent" (≥90) and "failing" (<50).
Your code currently asks for the number of scores but then uses that value as a score in the loop, which is not correct.
Revised Solution:
To address the problem accurately, you need to:

Collect multiple scores.
Use a for loop to iterate over each score.
Count the number of "excellent" and "failing" scores.
Print the counts at the end.
# Ask the user how many quiz scores they will enter
num_scores = int(input("How many quiz scores will you enter? "))

# Initialize counters for excellent and failing scores
excellent_count = 0
failing_count = 0

# Loop to collect and process each score
for i in range(num_scores):
    score = int(input(f"Enter score {i + 1}: "))

    if 90 <= score <= 100:
        print("Excellent!")
        excellent_count += 1
    elif 50 <= score < 90:
        print("Good")
    else:
        print("Failing")
        failing_count += 1

# Print the counts of excellent and failing scores
print(f"Number of excellent scores: {excellent_count}")
print(f"Number of failing scores: {failing_count}")
Explanation:
num_scores is the number of quiz scores the user plans to enter.
A loop runs for num_scores iterations, collecting and processing each input score.
Counters for excellent and failing scores (excellent_count and failing_count) keep track of the counts.
The code prints feedback for each score and displays the final counts at the end.
