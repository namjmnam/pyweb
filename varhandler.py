import pickle

def save_var(variable, filename):
    """
    Save a variable to a file.

    :param variable: The variable to be saved.
    :param filename: The name of the file where the variable will be saved.
    """
    with open(filename, 'wb') as file:
        pickle.dump(variable, file)

def load_var(filename):
    """
    Load a variable from a file.

    :param filename: The name of the file from which to load the variable.
    :return: The loaded variable.
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Example usage
my_data = {'key1': 'value1', 'key2': 'value2'}
filename = 'saved_data.pkl'

# Save the variable
save_var(my_data, filename)

# Load the variable
loaded_data = load_var(filename)
print(loaded_data)
