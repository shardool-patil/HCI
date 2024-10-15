class GOMSModel:
    def __init__(self, goal, methods, selection_rules):
        self.goal = goal
        self.methods = methods
        self.selection_rules = selection_rules

    def execute(self):
        print(f"Goal: {self.goal}\n")
        
        # Apply selection rules to pick the most efficient method
        selected_method = self.selection_rules(self.methods)
        print(f"Selected Method: {selected_method['name']}\n")
        
        # Execute the selected method
        self.run_method(selected_method)

    def run_method(self, method):
        print("Executing steps:")
        for operator in method['operators']:
            input(f"Performing: {operator} (Press Enter to continue...)")

# Example Methods for Logging In
methods = [
    {
        'name': 'Login via Form',
        'operators': [
            '1. Click login button',
            '2. Type username',
            '3. Type password',
            '4. Click submit'
        ]
    },
    {
        'name': 'Login via Social Media',
        'operators': [
            '1. Click login with Google button',
            '2. Authenticate with Google'
        ]
    }
]

# Selection Rules: Pick the method based on the number of operators (i.e., fewer steps)
def selection_rules(methods):
    return min(methods, key=lambda method: len(method['operators']))

# Define a GOMS Model for "Login"
goms_login_model = GOMSModel(
    goal="Log in to the website",
    methods=methods,
    selection_rules=selection_rules
)

# Main interactive loop
def main():
    while True:
        print("1. Execute GOMS Model")
        print("2. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            goms_login_model.execute()
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
