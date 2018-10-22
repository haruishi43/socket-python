# Creating HTTP-Server using Python Socket:

### References:

- [Emalsha's blog](https://emalsha.wordpress.com/2016/11/22/how-create-http-server-using-python-socket/)
- [Socket documentation](https://docs.python.org/3/library/socket.html)

## Overview:

What is a server?

> a computer program that provides services to other computer programs in the same or other computers

What is a socket?

> a network socket is one endpoint in a communication flow between two programs running over a network.

- Sockets are created and used with a set of programming requests or 'function calls' sometimes called socket application programming interface (API)
    - Most comman example: Berkeley UNIX C interface for sockets

### Python `sockets` module:

| Class method                      | Description                                                              |
|-----------------------------------|--------------------------------------------------------------------------|
| `Socket`                          | Low-level networking interface (per the BSD API)                         |
| `socket.socket(family, type)`     | Create and return a new socket object                                    |
| `socket.getfqdn(name)`            | Convert a string quad dotted IP address to a fully qualified domain name |
| `socket.gethostbyname(hostname)`  | Resolve a hostname to a string quad dotted IP address                    |
| `socket.fromfd(fd, family, type)` | Create a socket object from an existing file descriptor                  |

| Instance method                    | Description                                                                                                        |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| sock.bind( (adrs, port) )          | Bind the socket to the address and port                                                                            |
| sock.accept()                      | Return a client socket (with peer address information)                                                             |
| sock.listen(backlog)               | Place the socket into the listening state, able to send backlog outstanding connection requests                    |
| sock.connect( (adrs, port) )       | Connect the socket to the defined host and port                                                                    |
| sock.recv( buflen[, flags] )       | Receive data from the socket, up to buflen bytes                                                                   |
| sock.recvfrom( buflen[, flags] )   | Receive data from the socket, up to buflen bytes, returning also the remote host and port from which the data came |
| sock.send( data[, flags] )         | Send the data through the socket                                                                                   |
| sock.sendto( data[, flags], addr ) | Send the data through the socket                                                                                   |
| sock.close()                       | Close the socket                                                                                                   |
| sock.getsockopt( lvl, optname )    | Get the value for the specified socket option                                                                      |
| sock.setsockopt( lvl,optname,val)  | Set the value for the specified socket option                                                                      |



### Code!

[Socket Documentation](https://docs.python.org/3/library/socket.html#example) for Python has some detailed examples.

Notes:

- Server must perform the sequence `socket()` -> `bind()` -> `listen()` -> `accept()`.
- Client needs the sequence `socket()` -> `connect()`



```Bash
$ python main.py
```
