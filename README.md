# Boston house Price Prediction


### AWS Deployment

Perform action in local directory
- Create a folder in local project directory .ebextension 
- Create a file inside the folder "python.config"

Perform actions on AWS account
- Search Elastic beanstalk and click it
- Create application and provide a name
- Follow the instructions and launch the application in the end.

- Search for codepipeline
- create a new codepipeline and give name
- select role > new service role
- source provider > github > select repository > branch > github webhooks > buid provider:skip > 
- Deploy provider > aws elastic beanstalk > select application > selected environment 
- Create pipeine
- Deployment DONE
- Click AWS Elastic Beanstalk
- Find application and click URL


### Azure Deployment
- Create a new Web app
- Provide a name to the app > publish : code > runtime stack : Python 3.8 > region : > link plan: 
- click Next: deployment
- Github action setting : Enable
- Configur github action
- Configure github account
- Select organization
- Select repository
- Click [Review + Create] 
- CREATE
- DONE 

Go to Hithub action tab of the repository > click on URL.
