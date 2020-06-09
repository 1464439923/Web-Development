<h1> simple-time-app </h1>
<p>how to run locally:</p>
<ul>
  <li>docker build --tag my-python-app .
  <li>docker run -d --name python-app -p 8080:8080 my-python-app
  <li>in browser open: http://0.0.0.0:8080/
</ul>

<p>Push the image to Docker hub:</p>
<ul>
  <li>Login with: “docker login”
  <li>Push the image: docker push USERNAME/sample-time-app:latest
  <li>Check in dockerhub profile to see the image
</ul>

<p>Now deploy your image to the IBM Cloud K8s instance.</p>
<ul>
  <li>Create a deployment: “kubectl create deployment sample-time-app --
image=docker.io/USERNAME/sample-time-app:latest”
  <li>Expose your app’s port: “kubectl expose deployment/sample-time-app --
type="NodePort" --port 8080”
  <li>Check the exposed port: kubectl get services
  <li>Check the IP of your worked node from IBM Cloud
  <li>Access the http://IP:NodePort and confirm your app works:
    <img src = "res.jpg">
<ul>
