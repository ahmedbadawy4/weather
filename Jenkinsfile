pipeline {
	agent any                      // or you can use any agent in your case, make sure it can build docker image
	
	environment {
    	DOCKER_REPO=<docker-hub-user>	//add your docker repository name
	}
	
	options {
   		buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))  //to keep latest 10 build in jenkins history
 	}

    stages {
		stage('build in Docker') {
        	steps {
                        //add docker hub credentials in jenkins credentiald with the below name in ID
                    	withDockerRegistry([credentialsId: Docker_CREDENTIALS_ID, url: "https://hub.docker.com"]) {
          					sh """
				                docker build -t ${DOCKER_REPO}/weather:{BUILD_NUMBER} .            
				                docker push ${DOCKER_REPO}/weather:{BUILD_NUMBER}
			     			"""
                    	}
            		}
				}
			}
        
        stage('Deploy dev') {
	    	agent {
				label "kubectl"  // you can use k8s master agent and mention it's name
			}
	     	steps {
					deployImage('dev');  // we can specify any environment and deploy from any branch, for now we will use dev enviroment 
				}
	       	}
   	 	}
	}
}

def deployImage(environmentName){
    sh """
		sed -i 's~DOCKER_REPO~${DOCKER_REPO}~' kubernetes/deployment.yml   ## add variable in deployment file
		sed -i s/BUILD_NUMBER/${BUILD_NUMBER}/ kubernetesdeployment.yml    ## add variable in deployment file 
		kubectl -n $environmentName apply -f kubernetes
	"""
}