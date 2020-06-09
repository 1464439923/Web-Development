import socket, fileinput
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# use udp
sock.bind(('', 53533))

while 1:
    try:
        data, client_addr = sock.recvfrom(512)
        sendback_addr=(client_addr[0], 8081)
        data=data.decode().split()
        if len(data)==2:
            for x in data:
                if x[:4]=='NAME':
                    hostname=x
            response=''
            dnsFile=open('dns.txt', 'r')
            for x in dnsFile:
                x=x.split()
                for y in x:
                    if hostname==y:
                        response=x
                        break
                if response!='':
                    break
            if response=='':
                response='Not found'
            response=' '.join(response)
            sock.sendto(response.encode(), sendback_addr)
            dnsFile.close()
        elif len(data)==4:
            new, flag=data[1], 0
            data=' '.join(data)
            for line in fileinput.input("dns.txt", inplace=True):
                old=line.split()[1]
                if new==old:
                    print(data, end='')
                    flag=1
                else:
                    print(line, end='')
            if not flag:
                with open('dns.txt', 'a') as the_file:
                    the_file.write(data+'\n')
    except:
        break