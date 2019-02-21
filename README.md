# weather ☀️☔️

 This is a Flask (Python) application uses to get the weather forecast, it has 2 endpoints `/weather` and `/version`, it's able to get the weather forecast for any city, the output will be in JSON. 
### prerequisites:
- Add environment variables
  - `API_KEY="###############";`. The weather_key is the API key received from registering at [weather Map](https://openweathermap.org)
```bash
  export API_key="#####################"
```

## local ```for development```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
git clone https://github.com/ahmedbadawy4/weather.git
pip install -r requirements.txt
python app.py
```
in your favorite browser or seb GET from postman
* localhost:5000/weather?city=<CityName>

* localhost:5000/version 

     ### important notes:
- use this [URL](https://openweathermap.org/api) for a wide range of days depending on your project.
## Run weather API on:

* ### Docker

```bash
git clone https://github.com/ahmedbadawy4/weather.git
export DOCKER_REPO=<docker-hub-user>
docker build $DOCKER_REPO/weather_api .
docker run -p 5000:5000 $DOCKER_REPO/weather_api
curl <machine_ip>:5000/weather?city=cairo          
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

* ### kubernetes [Minikube]
Step 1: [instal Virtualbox](https://www.virtualbox.org/wiki/Downloads)

Step 2: [install minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

Step 3:
```bash
git clone https://github.com/ahmedbadawy4/weather.git
kubectl apply -f kubernetes
# wait until you get the pod running and ready
#then:
kubectl get svc  # to get nodeport
minikube ip      # to get minikube ip

check the app
curl -v http://minikube_ip:NodePort/version
curl -v http://minikube_ip:NodePort/weather
```


## CI/CD:

user ```Jenkinsfile``` to deploy this application using Jenkins Pipeline in kubernetes cluster




## local ```for development```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
git clone https://github.com/ahmedbadawy4/weather.git
pip install -r requirements.txt
python app.py
```
in your browser type 
* localhost:5000/weather
* localhost:5000/version 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)