# Network-and-Port-Scanner

# Tool Overview:
This Python tool is designed to identify live and non-live hosts while simultaneously scanning
their ports and reporting whether the ports are open or closed.

# Output:
For example, when scanning the host "google.com," the tool determines that it is live. It
proceeds to scan the range of ports, and in this case, ports 1 to 10 are found to be closed.
The tool conducts scan up to port 65,535, which represents the full range of potential ports
available on a server.

# Development Procedure:

Step 1: Begin by importing the necessary libraries, including "socket" for network
connectivity and "sys" for managing command-line arguments at runtime.

Step 2: Obtain the target hostname from the provided command-line argument.

Step 3: Utilize the "gethostbyname" function from the socket library to attempt resolution of
the target's IPv4 Address. If this resolution fails, a "gaierror" exception is raised, indicating
that the server is not currently live.

Step 4: Implement a loop that iterates through all 65,535 port numbers. For each port, use
the socket library to establish a connection. If a connection is established, it signifies that the
port is open; otherwise, it is considered closed.

This tool streamlines the process of identifying live hosts and determining the status of their
ports, offering a valuable resource for network analysis and security assessments.
