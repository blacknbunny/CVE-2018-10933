import socket, argparse
from sys import exit

parser = argparse.ArgumentParser(description="libSSH Authentication Bypass Server Version Check")
parser.add_argument('--host', help='Host')
parser.add_argument('-p', '--port', help='libSSH port', default=22)

args = parser.parse_args()

def test(host, port):
  try:
    sock = socket.create_connection((str(host), int(port)))
    recv = sock.recv(1024)
    sock.close()
  except socket.gaierror:
    parser.print_help()
    exit(1)
  return recv

def main():
  try:
    hostname = args.host
    port = args.port
  except:
    parser.print_help()
    exit(1)
  print(test(hostname, port))
  print("0.6 <= 0.7.5 and lower versions of 0.7.5 vulnerable, 0.7.6 <= 0.8.* patched.")
if __name__ == '__main__':
  exit(main())
