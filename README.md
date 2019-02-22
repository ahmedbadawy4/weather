# weather API Application☀️☔️

 This is a Flask (Python) application uses to get the weather forecast for any given city, it has 2 endpoints `/weather` and `/version` and the output will be in JSON format with some measured results depending on the given threshold. 
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
to get weather for specific city Hit : 127.0.0.1:5000/weather with the below prameters

 - city,country_code
 - temp_threshold
 - wind_threshold
 - unit

for example:

```html 
127.0.0.1:5000/weather?city=Cairo,EG&temp_threshold=3&wind_threshold=10&units=metric
```

the result should be like:
```json
{
   "cloud status": "haze",
    "humidity": 71,
    "temp": 286.15,
    "temp_state": "high temprature",
    "wind": 1.21,
    "wind_state": "low speed wind"
}
```

to get application version hit:
```html
127.0.0.1:5000/version
``` 

    
 ### important notes:
- use this [URL](https://openweathermap.org/api) for a wide range of days depending on your project.
## Run weather API on:

* ### Docker

```bash
git clone https://github.com/ahmedbadawy4/weather.git
export API_key="#####################"
export DOCKER_REPO=<docker-hub-user>
docker build $DOCKER_REPO/weather_api .
docker run -p 5000:5000 $DOCKER_REPO/weather_api
```

* ### Vagrant
Step 1: [Download and Install Vagrant](https://www.vagrantup.com/downloads.html)

Step 2: [Download and Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)

```bash
git clone https://github.com/ahmedbadawy4/weather.git
vim Vagrantfile
## add your api_key in "{"API_TOKEN" => "api_key from your account"}"
vagrant up      
#Waiting for machine to boot and applying configurations. This may take a few minutes...
```
The network configurations set as public, bridged and port forwarding configuration uses port `8080` in host and ```5000``` in guest you can change it from `Vagrantfile`. see more in [Vagrant Networking](https://www.vagrantup.com/docs/networking/)



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
```
check the app version

```bash
curl -v http://minikube_ip:NodePort/version
```

to get weather for specific city Hit : 
```html
http://minikube_ip:NodePort/weather with the below prameters

 - city,country_code
 - temp_threshold
 - wind_threshold
 - unit

for example:

http://minikube_ip:NodePort/weather?city=LONDON,GB&temp_threshold=3&wind_threshold=10&units=metric

```

## CI/CD:

user ```Jenkinsfile``` to deploy this application using Jenkins Pipeline in kubernetes cluster by:

* allow jenkins to access your dockerhub repository or any other private docker repository.
* allow your agent (or master) has access to your k8s cluster and can run kubectl command.
* depending on docker repository you have to comment one of the image address lines in `kubernetes/deployment.yaml` file.
* you can configure `hpa.yaml` "horizontal pod autoscaler" depending on your project. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## To do list:
* add security layer to authenticate login using user and password.
* configure database to save users credentials and make flexibility in extracting data for many days and split the day to sections like, morning, midday, and night.
* get more information about weather and use it to make this app more efficient.
* add UI layer to make it available to end users.
* add monitoring layer (depending on each environment)  

## License
[MIT](https://choosealicense.com/licenses/mit/)