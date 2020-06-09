from flask import Flask, request
from flask import Response
import socket
fs=Flask(__name__)
register_info={
        'hostname': 'fibonacci.com',
        'ip': '127.0.0.1',
        'as_ip': '127.0.0.1'}

@fs.route('/register', methods=['PUT'])
def register():
    register_info=request.get_json()
    as_address = (register_info['as_ip'], 53533)
    dns_register = '''
    TYPE=A
    NAME={}
    VALUE={}    
    TTL=10
    '''.format(register_info['hostname'], register_info['ip'])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(dns_register.encode(), as_address)
    return Response("Registation Succeeded", status=200)

@fs.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args['number']
    return Response(str(fib(int(number))), status=200)

def fib(num):
    a, b=0, 1
    if num<=0:
        return a
    for i in range(num):
        a, b = b, a+b
    return b

if __name__=='__main__':
    fs.run(host='0.0.0.0', debug=True, port=9090)