import socket

# Replace with the port you want to forward
PORT_TO_FORWARD = 8080

# Replace with the target host and port
TARGET_HOST = "localhost"
TARGET_PORT = 8000

def forward_port(source_port, target_host, target_port):
  """
  Forwards a port from the local machine to a target host and port.

  Args:
      source_port: The port to listen on on the local machine.
      target_host: The hostname or IP address of the target host.
      target_port: The port on the target host to forward to.
  """
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("", source_port))
    sock.listen()
    while True:
      client_socket, client_address = sock.accept()
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as target_socket:
        target_socket.connect((target_host, target_port))
        while True:
          data = client_socket.recv(1024)
          if not data:
            break
          target_socket.sendall(data)

if __name__ == "__main__":
  forward_port(PORT_TO_FORWARD, TARGET_HOST, TARGET_PORT)
