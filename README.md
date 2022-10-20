![Founder Property Logo](https://github.com/BesnikShala/Founder-Property-Ltd/blob/main/static/media/logo1.jpg?raw=true)


# Founder Property Ltd 

View the live site here - [Founder Property L:td](https://founder-property.herokuapp.com/)

Founder Property Ltd is a construction services company which also deals in real estate. Aquisition of land, development of new builds and renovations on existing properties.


## Technologies Used

This project is primarily built using HTML5 semantic markup, CSS stylesheets, Javascript, Python, Django, SQLite and Heroku Postgres.

#### Python

The following Python modules were used on this project:

* asgiref==3.5.2
* backports.zoneinfo==0.2.1
* boto3==1.24.66
* botocore==1.27.66
* click==8.1.3
* dj-database-url==1.0.0
* Django==4.0.5
* django-crispy-forms==1.14.0
* django-storages==1.13.1
* gunicorn==20.1.0
* itsdangerous==2.1.2
* jmespath==1.0.1
* Pillow==9.1.1
* psycopg2==2.9.3
* psycopg2-binary==2.9.3
* s3transfer==0.6.0
* sqlparse==0.4.2
* Werkzeug==2.1.2

* Django was used as the main python framework in the building of this project.

* jQuery

This framework was used to create some of the site's interactive functions.

* Gitpod

This project was built using Gitpod as the IDE.

*Github

Github was used for online version control and storing files and documents.

* Heroku

Heroku was used as a cloud-based platform to deploy this site.

* Google fonts

The font styles used on this website were chosen from Google fonts.

* Fontawesome

The icons used on this page were found in Fontawesome.

* SQLite

SQLite was used as the database for the creation and development of this project.

* Heroku Postgres

Heroku was used as the database for this project in production mode after deployment to Heroku.

* Jinja

Jinja was used for templating.

* AWS-Amazon Web Services

AWS was used to store all media and static files of this site in production mode.


## Deployment

This project was developed using Gitpod IDE and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused. The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institute student template was used to create this project.

Code Institute Full Template

This project was deployed using Heroku and stored in GitHub.

### Project and Repository Creation

* Navigate to Github.
* Create a new repository by first clicking the green button labeled new on the top left of the screen.
* Select the Code Institute template in the templates section.
* Give the repository a name, in this case BeFitness-MS4.
* Click the green 'Create Repository' button at the bottom of the page.
* Inside the repository click the green 'gitpod' button to initialize your repository.
* Future access to this workspace must be gained through gitpod workspaces, clicking the green button in gitpod again will initialize a new workspace.
* Use the git add . command to add all modified and new files to the staging area.
* Use the git commit -m command to commit a change to the local repository.
* Use the git push command to push all committed changes to github.
* Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:

* Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or * modules are installed during project development by using the following command:

* pip freeze --local > requirements.txt
* Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

* Push these files to GitHub.

* Install psycopg2 and dj_datatbase_url in your workspace cli.

* Once those steps are done, the website can be deployed in Heroku using the steps listed below:


#### Deployment Steps


- Log into Heroku .

- Click the New button.

- Click the option to create a new app.

- Enter the app name in lowercase letters.

- Select the correct geographical region.

- Connect Heroku app to Github repository

- In heroku select the deploy tab.

- Click github button.

- Enter the repository name and click search.

- Select the relevant repository and click connect.

- Add Heroku Postgres Database

- Click the resources tab in heroku.

- Under Add-ons search for heroku postgres.

- Click on heroku postgres when it appears.

- Select the Hobby Dev-Free option in plans.

- Click submit order form.

- Setting up environment variables

- In the heroku settings click the reveal config vars button and set the following variables:

- AWS_ACCESS_KEY_ID

- AWS_SECRET_ACCESS_KEY

- DATABASE_URL

- EMAIL_HOST_PASS

- EMAIL_HOST_USER

- SECRET_KEY

- STRIPE_PRICE_ID

- STRIPE_PUBLIC_KEY

- STRIPE_SECRET_KEY

- STRIPE_WH_SECRET

- USE_AWS

- The values of these variables are secret and for security purposes will not be shared here.

- Setting up the AWS s3 bucket

- Create an Amazon AWS account

- Search for S3 and create a new bucket

- Allow public access

- Under Properties > Static website hosting

- Enable

- index.html as index.html

- save

- Under Permissions > CORS use the following:

[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]


- Under Permissions > Bucket Policy:

- Generate Bucket Policy and take note of Bucket ARN

- Chose S3 Bucket Policy as Type of Policy

- For Principal, enter *

- Enter ARN noted above

- Add Statement

- Generate Policy

- Copy Policy JSON Document

- Paste policy into Edit Bucket policy on the previous tab

- Save changes

- Under Access Control List (ACL):

- For Everyone (public access), tick List

- Accept that everyone in the world may access the Bucket

- Save changes

- AWS IAM (Identity and Access Management) setup


- From the IAM dashboard within AWS, select User Groups:

- Create a new group

- Click through and Create Group

- Select Policies:

- Create policy

- Under JSON tab, click Import managed policy

- Choose AmazongS3FullAccess

- Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy

- Click next step and go to Review policy

- Give the policy a name and description of your choice

- Create policy

- Go back to User Groups and choose the group created earlier

- Under Permissions > Add permissions, choose Attach Policies and select the one just created

- Add permissions

- Under Users:

- Choose a user name

- Select Programmatic access as the Access type

- Click Next

- Add the user to the Group just created

- Click Next and Create User

- Download the .csv containing the access key and secret access key.

- THE .csv FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.

- Connecting Heroku to AWS S3

* Install boto3 and django-storages
* pip3 install boto3
* pip3 install django-storages
* pip3 freeze > requirements.txt
* Add the values from the .csv you downloaded to your Heroku Config Vars under Settings:
* Delete the DISABLE_COLLECTSTATIC variable from your Cvars and deploy your Heroku app
* With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any * required media files to it.
* PLEASE MAKE SURE media AND static FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS
* Enable automatic deployment:
* Click the Deploy tab
* In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.
* Connect app to Github Repository
* Click the deploy tab and connect to GitHub.
* Type the name of the repository into the search bar presented.
* Click the Code dropdown button next to the green Gitpod button.
* When the correct repository displays click the connect button.

#### Making a clone to run locally

* It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT and SECRET_KEY which have all been kept secret in keeping with best security practices.

* Log into GitHub.
* Select the respository.
* Click the Code dropdown button next to the green Gitpod button.
* Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
* Open the alternative editor and terminal window.
* Type 'git clone' and paste the copied URL.
* Press Enter. A local clone will be created.
* Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

* -pip install -r requirements.txt
* How to Fork the respository.
* Log into GitHub.
* In Github go to (https://github.com/BesnikShala/Founder-Property-Ltd).
* In the top right hand corner click "Fork".


## Testing

* Passed all testing, no known bugs.

#### Media

* Most images sourced from [unsplash.com](https://unsplash.com/), [Freepik] (https://www.freepik.com/)

* Personal Uploads from projects


