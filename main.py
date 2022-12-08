from Server import Server
# This is the template code for the CNE335 Final Project
# Nathaniel Stevens
# CNE 335 Fall

def print_program_info():
    print("Server Automator v0.1 by Nathaniel Stevens")

# This is the entry point to our program
print_program_info()

# TODO - Create a Server object
S_object = Server("35.89.172.138")
# TODO - Call Ping method and print the results
S_object.ping()
