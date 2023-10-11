# flask-docker-helloworld
Sample project to build a flask hello-world application with docker

Build Docker Image 

```bash
$> sudo  docker build -t application:latest .
```

Run Docker Container
```bash 
$> sudo  docker run -p 80:80 application:latest
```

Open http://<your_vm_ip>
