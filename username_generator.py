import random

# Enhanced word lists with Indian-themed additions
adjectives = [
    "Cool", "Happy", "Brave", "Wild", "Silent", "Quick", "Clever", 
    "Gentle", "Fierce", "Loyal", "Veer", "Divya", "Anokha", "Shanti",
    "Royal", "Desi", "Adbhut", "Tejasvi", "Mahan", "Sundar"
]

nouns = [
    "Tiger", "Dragon", "Wolf", "Eagle", "Phoenix", "Lion", "Hawk", 
    "Bear", "Panther", "Fox", "Garuda", "Naga", "Yali", "Kamal", 
    "Rangoli", "Diya", "Mayur", "Bagha", "Vajra", "Rishi"
]

special_chars = ['!', '@', '#', '$', '%', '&', '★']

def get_user_preferences():
    """Collect and validate user preferences for username generation."""
    print("=== Random Username Generator ===")
    
    # Validate number of usernames (1-100)
    while True:
        try:
            num = int(input("How many usernames do you want to generate? (1-100) "))
            if 1 <= num <= 100:
                break
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Enter a valid number.")
    
    # Number configuration
    include_numbers = input("Include numbers? (y/n): ").lower().strip() == 'y'
    num_digits = 3
    if include_numbers:
        while True:
            try:
                num_digits = int(input("Number of digits (e.g., 3 → 100-999): "))
                if num_digits >= 1:
                    break
                print("Digits must be at least 1.")
            except ValueError:
                print("Invalid input. Enter a valid number.")
    
    # Special characters configuration
    include_special = input("Include special characters? (y/n): ").lower().strip() == 'y'
    num_special = 1
    if include_special:
        while True:
            try:
                num_special = int(input("Number of special characters (1-3): "))
                if 1 <= num_special <= 3:
                    break
                print("Special characters must be 1-3.")
            except ValueError:
                print("Invalid input. Enter a valid number.")
    
    return num, include_numbers, num_digits, include_special, num_special

def generate_username(include_numbers, num_digits, include_special, num_special):
    """Generate a unique username with specified features."""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    # Add numbers
    if include_numbers:
        min_num = 10 ** (num_digits - 1)
        max_num = (10 ** num_digits) - 1
        username += str(random.randint(min_num, max_num))
    
    # Add unique special characters
    if include_special:
        chars = random.sample(special_chars, k=num_special)  # Unique characters
        username += ''.join(chars)
    
    return username

def save_to_file(usernames):
    """Save usernames with flexible filename and append mode."""
    filename = input("\nSave as filename (press Enter for 'usernames.txt'): ") or "usernames.txt"
    mode = "a" if input("Append to existing file? (y/n): ").lower() == 'y' else "w"
    
    # Fix: Add encoding='utf-8'
    with open(filename, mode, encoding='utf-8') as f:
        for name in usernames:
            f.write(f"{name}\n")
    print(f"Saved {len(usernames)} usernames to '{filename}'.")

def main():
    # Get preferences
    num_usernames, include_numbers, num_digits, include_special, num_special = get_user_preferences()
    
    # Generate unique usernames
    usernames = set()
    while len(usernames) < num_usernames:
        username = generate_username(include_numbers, num_digits, include_special, num_special)
        usernames.add(username)
    usernames = list(usernames)
    
    # Display results
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    # Save to file
    save_to_file(usernames)

if __name__ == "__main__":
    main()