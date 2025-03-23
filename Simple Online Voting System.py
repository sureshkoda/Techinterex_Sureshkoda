# Simple Online Voting System

# Dictionary to store candidates and their vote counts
candidates = {'Candidate 1': 0, 'Candidate 2': 0, 'Candidate 3': 0}
# Set to store users who have voted
voters = set()

def get_input(prompt):
    try:
        return input(prompt)
    except OSError:
        print("Input is not supported in this environment.")
        return None

# Function to display candidates and votes
def display_candidates():
    print("\nCandidates and their votes:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

# Function to allow users to vote
def vote():
    user_id = get_input("Enter your user ID: ")
    if user_id is None:
        return
    
    if user_id in voters:
        print("You have already voted. You cannot vote again!")
        return
    
    print("\nAvailable Candidates:")
    for candidate in candidates:
        print(candidate)
    
    choice = get_input("Enter the candidate's name you want to vote for: ")
    if choice is None:
        return
    
    if choice in candidates:
        candidates[choice] += 1
        voters.add(user_id)
        print("Thank you for voting!")
    else:
        print("Invalid candidate name! Please try again.")

# Function to view voting results (Admin only)
def view_results():
    admin_password = get_input("Enter admin password: ")
    if admin_password is None:
        return
    
    if admin_password == "admin123":
        display_candidates()
    else:
        print("Incorrect password! Access denied.")

# Function to reset votes (Admin only)
def reset_votes():
    admin_password = get_input("Enter admin password to reset votes: ")
    if admin_password is None:
        return
    
    if admin_password == "admin123":
        global candidates, voters
        candidates = {candidate: 0 for candidate in candidates}
        voters.clear()
        print("Voting system has been reset!")
    else:
        print("Incorrect password! Reset denied.")

# Main program loop
def main():
    while True:
        print("\nSimple Online Voting System")
        print("1. Vote")
        print("2. View Results (Admin only)")
        print("3. Reset Votes (Admin only)")
        print("4. Exit")
        
        choice = get_input("Enter your choice: ")
        if choice is None:
            return
        
        if choice == '1':
            vote()
        elif choice == '2':
            view_results()
        elif choice == '3':
            reset_votes()
        elif choice == '4':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
