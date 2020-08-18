import urllib.request
import json, requests

# only need to change this!
register_info={
        'hostname': 'fibonacci.com',
        'ip': '172.18.0.3',
        'as_ip': '172.18.0.2',
        'as_port': '53533'
}
url = 'http://0.0.0.0:9090/register'
data = json.dumps(register_info)
req = requests.put(url, data, headers = {'content-type': 'application/json'})
print(req)

#http://127.0.0.1:8080/fibonacci?hostname=fibonacci.com&number=12&as_ip=127.0.0.1
