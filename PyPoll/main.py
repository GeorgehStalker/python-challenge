import csv

# Path to the CSV file
csv_file_path = "C:/Users/georg/git repositories/Module 3/python-challenge/PyPoll/Resources/election_data.csv"

# Counting the total number of votes cast
total_votes = 0

# Open the CSV file and count the number of rows (excluding the header)
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        total_votes += 1

print("Total number of votes cast:", total_votes)

# Creating a list of candidates who received votes
candidates = set()

# Open the CSV file and extract the candidate names
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        candidates.add(row['Candidate'])

print("Complete list of candidates who received votes:")
for candidate in candidates:
    print(candidate)

# Calculating the percentage of votes each candidate won
candidate_votes = {}

# Total number of votes
total_votes = 0

# Open the CSV file and count the votes for each candidate
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        candidate = row['Candidate']
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
        total_votes += 1

# Calculating and printing the percentage of votes for each candidate
print("Percentage of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}%")

# Determining the total number of votes each candidate won
candidate_votes = {}

# Open the CSV file and count the votes for each candidate
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        candidate = row['Candidate']
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Printing the total number of votes each candidate won
print("Total number of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")

# Determining the winner of the election based on popular vote
candidate_votes = {}

# Open the CSV file and count the votes for each candidate
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        candidate = row['Candidate']
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Finding the winner based on the highest number of votes
winner = max(candidate_votes, key=candidate_votes.get)

# Printing the winner of the election based on popular vote
print("Winner of the election based on popular vote:", winner)