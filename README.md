# weather

 weather is a web API to get the weather forecast, it has 2 endpoints `/weather` and `/version`, it's able to handle hundreds of millions of requests and the output will be in JSON.


## try it on the fly

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
git clone https://github.com/ahmedbadawy4/weather.git
pip install -r requirements.txt
python app.py
```
in your browser type 
* <machine_IP>:5000/weather
* <machine_IP>:5000/version  

## weather in:

* ### Docker

```bash
export DOCKER_REPO=<docker-hub-user>
docker build $DOCKER_REPO/weather_api .
docker run -p 5000:5000 $DOCKER_REPO/weather_api
curl <machine_ip>:5000/weather          
curl <machine_ip>:5000/version
```
* ### Vagrant
Step 1: [Download and Install Vagrant](https://www.vagrantup.com/downloads.html)

Step 2: [Download and Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)

```bash
git clone https://github.com/ahmedbadawy4/weather.git
vagrant up      
#Waiting for machine to boot and applying configurations. This may take a few minutes...
```
The network configurations set as public, bridged and port forwarding configuration uses port `8080` in host and ```5000``` in guest you can change it from `Vagrantfile`. see more in [Vagrant Networking](https://www.vagrantup.com/docs/networking/)

In your local browser type 
* localhost:8080/weather
* localhost:8080/version 

* ### kubernetes
```bash
```




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)