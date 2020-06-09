How to run:
1. Open a command prompt window in this directory
2. docker network create dns
3. cd AS
4. docker build -t ytp27/as:latest .
5. docker run --network dns --name as -p 53533:53533/udp -it ytp27/as:latest

6. Open another command prompt window in this directory
7. cd FS
8. docker build -t ytp27/fs:latest .
9. docker run --network dns --name fs -p 9090:9090 -it ytp27/fs:latest

10. Open another command prompt window in this directory
11. cd US
12. docker build -t ytp27/us:latest .
13. docker run --network dns --name us -p 8080:8080 -it ytp27/us:latest

14. Open another command prompt window in this directory
15. docker inspect dns
16. Check the ip address of three container: us, fs, as

17. change the ip address in register_info in sendPutRequest.py to send PUT request to fs to register.
18. Open an browser and visit the following url to get the result (change X). http://0.0.0.0:8080/fibonacci?hostname=fibonacci.com&number=13&as_ip=X&as_port=53533

How to deploy the whole system on Kubernetes (extra credit):
Be sure that the ibm cloud and kubectl is correctly set.
19. kubectl apply -f deploy_dns.yml
get the external ip address on ibm cloud to get the result.
