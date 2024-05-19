# Distributed Image Processing App

# Demo
https://www.youtube.com/watch?v=B5E3Z5kLQ74

## Installation
best way to run this is do each step on a seperate machine to avoid port contention

- launch rabbitmq anywhere and keep note of the ip -> you can use our server on ip 104.199.5.58

- launch the master

- clone the repo:
	```bash
	   git clone https://github.com/abdel6602/distributedProject.git
	```
- ensure port 80 is free

- run the master

	```bash
	   cd master && sudo docker build -t master . && sudo docker run -p 80:80 master"
	```
- run the worker
	```bash
	   cd worker && cd workerCode && sudo docker build -t worker . && sudo docker run worker
	```

- clone this repo:
	```bash
	   git clone https://github.com/abdel6602/temp.git
	```
- make sure port 80 is free

- run the following command
	```bash
	   sudo docker build -t server . && sudo docker run -p 80:80 server
	```

- clone the web app
	```bash
	   git clone https://github.com/Zaituny/distributed-frontend.git
	```
- inside the clones repo run
	```bash
	   npm i && npm install -g @angular/cli && ng serve --host 0.0.0.0
	```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.