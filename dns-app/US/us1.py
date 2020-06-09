from flask import Flask, request
from flask import Response
import socket, requests
dns_query=Flask(__name__)

@dns_query.route('/fibonacci')
def fibonacci():
    hostname=request.args['hostname']
    number=request.args['number']
    as_ip=request.args['as_ip'] # all arguments are mandatory
    # use request.args.get('number') to receive optional arguments
    if hostname is None or number is None or as_ip is None:
        return Response(status=400)
    else:
        # query AS about the address of hostname
        as_address = (as_ip, 53533)
        req = 'TYPE=A NAME={}'.format(hostname)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('127.0.0.1', 8081))
        sock.sendto(req.encode(), as_address)
        data, addr = sock.recvfrom(512)  # recieve
        data=data.decode().split()
        for x in data:
            if x[:5]=='VALUE':
                target_ip=x[6:]
        url = 'http://{}:9090/fibonacci?number={}'.format(target_ip, number)
        response = requests.get(url).text
        return Response(response, status=201)

if __name__=='__main__':
    dns_query.run(debug=True, port=8080)