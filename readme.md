# Mircoservices and Monolithic Architectures

## For Monolithic based Application
---
## For Running the BackEnd-Service in localhost

**Move to backend directory** : cd monolithic_backend/

Go to .env.dev (development environment) file :
1. Make sure to assign a MONGODB URI Link. You can generate your own cluster from [here](https://www.mongodb.com) 
2. Feel free to use your custom port


Download the node modules in each working directory using **npm install** 


**To run the project** : npm run dev


## For Running this service in ec2

Push this codebase to the created ec2 instance and run the same command as mentioned above in the working directory of folder

------ 

## For Running the FrontEnd-Service in localhost


**Move to frontend directory** : cd monolithic_frontend/

Download the node modules in each working directory using **npm install** 

**To run the project** : npm start (if root permissions are required, use **sudo**)


## For Running this service in ec2

Push this codebase to the created ec2 instance and run the same command as mentioned above in the working directory of folder

> In ec2, you can not directly run an application on PORT 80. Make sure to Setup an Nginx Reverse Proxy for running the frontend-service. (Refer [AWS Docs](https://aws.amazon.com/tutorials/setup-an-nginx-reverse-proxy/) [Stackoverflow](https://stackoverflow.com/questions/17413526/nginx-missing-sites-available-directory))


-------

## For Microservices based Application
-----
## For running the application on localhost

In each service folder, Go to .env.dev (development environment) file :
1. Make sure to assign a MONGODB URI Link. You can generate your own cluster from [here](https://www.mongodb.com)
2. MSG_QUEUE_URL should be replaced with your Amazon MQ broker service endpoint
3. Feel free to use your custom port. Make sure to expose the same Port numbers in the Docker files also.

Download the node modules in each working directory using **npm install** 

**For running gateway-service** : node index.js
**For running customer-service** : npm run dev
**For running product-service** : npm run dev
**For running shopping-service** : npm run dev
**For running Frontend-service** : npm start (use **sudo** if required)

-------

## For running the application on AWS

In gateway directory,

1. Run **docker build -t gateway-service .**
2. This creates a docker image and then push this docker image to AWS ECR service using **docker push**
3. For this, We have exposed PORT 8000

In product directory,

1. Run **docker build -t product-service .**
2. This creates a docker image and then push this docker image to AWS ECR service using **docker push**
3. For this, We have exposed PORT 8002

In customer directory,

1. Run **docker build -t customer-service .**
2. This creates a docker image and then push this docker image to AWS ECR service using **docker push**
3. For this, We have exposed PORT 8001

In shopping directory,

1. Run **docker build -t shopping-service .**
2. This creates a docker image and then push this docker image to AWS ECR service using **docker push**
3. For this, We have exposed PORT 8003
   
In microservice_frontend directory,

1. Run **docker build -t frontend-service .**
2. This creates a docker image and then push this docker image to AWS ECR service using **docker push**
3. For this, We have exposed PORT 80

Finally,
1. Create a cluster using AWS ECS service
2. Create task definitions for these.
3. Run new tasks in the cluster based on the newly created task definitions.
4. Make sure to use the PORT number you have exposed in the Docker files.
5. You can directly run the frond-end service task on PORT 80. No need to add any extra configurations.

-------

# Testing the architectures

Move to **Testing_Archs** directory

## Installation:
1. Ensure that Python version 3 and pip are installed on the system.
2. Install the required libraries with the following command:
3. pip install -r requirements.txt

## To run load testing:

1. Assign the correct URLs to the variables **monolithic_url** and **microservices_url** in the **load_testing.py** file.
2. Configure the number of concurrent users and total requests in the **load_testing.py** file.
3. Run the **load_testing.py** file to visualize the results.

## To run product testing:

1. Assign the correct product URL to the variable **product_details_url** in the **retrieve_product.py** file.
2. Configure the number of concurrent users and total requests in the **retrieve_product.py** file.
3. Run the **retrieve_product.py** file to visualize the results.

-------
# Requirements

1. Python3 (with pip)
2. Node.js (with npm)
3. MongoDB cluster
4. Docker
5. AWS account