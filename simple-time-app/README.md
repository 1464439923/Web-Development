<h1> simple-time-app </h1>
how to run locally:
<ul>
<li>docker build --tag my-python-app .
<li>docker run -d --name python-app -p 8080:8080 my-python-app
<li>in browser open: http://0.0.0.0:8080/
</ul>

Push the image to Docker hub:
i. First login with: “docker login” 
ii. Push the image: docker push USERNAME/sample-time-app:latest
iii. Check in dockerhub profile to see the image

c. Now deploy your image to the IBM Cloud K8s instance.
i. Create a deployment: “kubectl create deployment sample-time-app --
image=docker.io/USERNAME/sample-time-app:latest”
ii. Expose your app’s port: “kubectl expose deployment/sample-time-app --
type="NodePort" --port 8080”
iii. Check the exposed port: kubectl get services
iv. Check the IP of your worked node from IBM Cloud
v. Access the http://IP:NodePort and confirm your app works
