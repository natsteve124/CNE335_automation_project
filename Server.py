import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """
    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 5 %s" % self.server_ip)
        return result 

    def ssh(self, ec2_username, path, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server_ip, username = ec2_username, key_filename = path)

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode("utf-8").split("\n")
        for message in output:
            print(message)
        
        ssh.close()
