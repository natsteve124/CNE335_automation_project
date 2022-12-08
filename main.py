from Server import Server
import os.path
# This is the template code for the CNE335 Final Project
# Nathaniel Stevens
# CNE 335 Fall

def print_program_info():
    print("Server Automator v0.1 by Nathaniel Stevens")

# This is the entry point to our program
print_program_info()

# TODO - Create a Server object
ec2_ip = "{INSERT IP HERE}"
S_object = Server(ec2_ip)
# TODO - Call Ping method and print the results
print("pinging ec2 instance")
S_object.ping()
print("\nfinished pinging ec2 instance")

P_filepath = os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa")
username = "ubuntu"
command = "sudo apt update && sudo apt upgrade -y"
print("\nssh to ec2 instance\n")
S_object.ssh(username, P_filepath, command)
print("finished ssh to ec2 instance")
