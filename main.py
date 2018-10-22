import socket
import time

class Server(object):

    def __init__(self, host, port):
        super(Server, self).__init__()
        self.port = port     # Define given port
        self.host = host        # This '' means all the active interfaces
        self.host_dir = 'src'     # Web page store in here

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.socket.bind((self.host, self.port))
            print(f'HTTP Server Running on: {self.host}:{self.port}')

        except Exception as e:
            print(f'ERROR, PORT: {self.port} is already in use.')
            import sys
            sys.exit(1)
        print('Server waiting for requests...')
        print('-'*60)
        self.get_connection()

    def header_gen(self,status):
        '''Generate header for response'''
        
        head = ''
        if status == 200:
            head = 'HTTP/1.1 200 OK\n'
        elif status == 404:
            head = 'HTTP/1.1 404 Not Found\n'

        if self.req_file.endswith(".html"):
            mimetype='text/html'
        elif self.req_file.endswith(".jpg"):
            mimetype='image/jpg'
        elif self.req_file.endswith(".gif"):
            mimetype='image/gif'
        elif self.req_file.endswith(".js"):
            mimetype='application/javascript'
        elif self.req_file.endswith(".css"):
            mimetype='text/css'
        else:
            mimetype='text/html'

        # Additional header content
        date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        head += 'Date: ' + date + '\n'
        head += 'Server: simple-HTTP-server\n'
        head += 'Content-Type: ' + str(mimetype) + '\n'
        head += 'Connection: Close\n\n'

        return head

    def get_connection(self):

        # Loop to get connections
        while True:
            self.socket.listen(1) # Set number of queued connection  

            conn, addr = self.socket.accept() 
            #conn => Connected socket to client
            #addr => Client address

            print(f'Client connected on {addr}')

            request = conn.recv(1024).decode('utf-8')  # get request data from client 
            temp = request.split(' ')

            if len(temp) <= 1:
                # shut down connection when request has no method or file
                conn.close()
                continue

            method = temp[0]
            req_file = temp[1]
            self.req_file = req_file

            print(f'Client request: [{req_file}] using {method}')

            if method == 'GET':

                r_file = req_file.split('?')[0]
                if r_file == '/':
                    r_file = '/index.html'

                request_file = self.host_dir + r_file 

                # Read file 
                try:
                    file = open(request_file,'rb') # open file , r => read , b => byte format
                    response = file.read()
                    file.close()

                    header = self.header_gen(200) # Generate header
                except Exception as e:
                    print(f'File not found {request_file}')
                    header = self.header_gen(404)
                    response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
                
                final_res = header.encode('utf-8')
                final_res += response

                conn.send(final_res)
                conn.close()

            else:
                print(f'HTTP request {method} not valid.')

            # close connection when not in use
            conn.close()

            print('')


if __name__ == '__main__':

    sv = Server('127.0.0.1', 8081)
    sv.run()
