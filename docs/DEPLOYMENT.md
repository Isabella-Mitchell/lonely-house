# Deployment

## Creating a Gitpod Workspace

The project was created in Gitpod using the Code Institute Gitpod Full Template using these steps:

1. Log in to GitHub and go to the [Code Institute student template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Add a repository name and click 'Create reposiory from template'.
4. This will create a copy of the template in your own repository. Now you can click the green 'Gitpod' button to open a workspace in Gitpod.

## Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/Isabella-Mitchell/gather-recipe-website)
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/Isabella-Mitchell/lonely-house)
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `lonely-house`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating a database

You will need to create a database, unless you wish to pay for a Heroku database.

1. Go to [ElephantSQL.com](https://elephantsql.com/) and select to create a database
2. Select the free database plan
3. Select “Log in with GitHub” and authorise with GitHub
4. Create new team form. You can use your name, read and agree to the T&C's, select yes for GDPR, provide your email address and click Create Team. Your account will be created 
5. From your dashboard, click “Create New Instance”
6. Set up your plan. Give it the same name as your project, select the free plan. Select "select region" and select a region close to you.
7. Click review, and if the details are correct, click create instance.
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, clicking the copy icon will copy the database URL to your clipboard

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a Heroku account and log in.
2. Create a new app. When you do so, select the closest region to you and give it an appropriate name. Note Heroku names must be unique
3. In your app Settings, add the config var DATABASE_URL, and for the value, paste in your database url from ElephantSQL.
4. In your app Settings, add the config var DJANGO_SECRET_KEY. Generate a DJANGO_SECRET_KEY and paste it in. Keep this secret.

## Project preparation in Gitpod - Connect to your external database

1. In Gitpod, install dj_database_url and psycopg2 by running this command in the terminal
```pip3 install dj_database_url==0.5.0 psycopg2```
2. Update your requirements.txt file with the newly installed packages by running this command in the terminal
```pip freeze > requirements.txt```
3. In the project settings.py file, paste the following lines of code underneath the import for os
 ```import os```
 ```import dj_database_url```
4. Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated. Do not commit this as it will reveal sensitive information.
```# DATABASES = {...}```
 ```DATABASES = {'default': dj_database_url.parse('your-database-url-here')}```
5. In the terminal, run the showmigrations command to confirm you are connected to the external database. You should see a list of all migrations printed to the terminal
 ```python3 manage.py showmigrations```
6. Migrate your database models to your new database by running:
```python3 manage.py migrate```
7. Create a superuser for your new database with the following command (Follow the steps to create a your superuser username and password. The email address can be left blank.):
```python3 manage.py createsuperuser```
8. Now you can delete the code you copied in step 4 and uncomment out the original Database code.
```DATABASES = {...}```

## Deploying to Heroku

1. In Gitpod, install Gunicorn by running: 
```
pip3 install gunicorn
```
2. Update your requirements.txt file to include this:
```
pip freeze > requirements.txt
```
3. Create a Procfile. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
4. In your Procfile, enter:
```
web: gunicorn lonely_house.wsgi:application
```
5. In the terminal, run the following and log into Heroku:
```
heroku login
```
6. Temporarily disable collect static by running:
```
heroku config:set DISABLE_COLLECTSTATIC=1
```
7. Update the hostname of your Heroku app to ALLOWED_HOSTS in settings.py
8. Commit your changes and push to Github.
9. Go back to your app on Heroku
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. Your app should be deployed without any static files.

## Connecting to AWS

### Creating a S3 Bucket

1. Create an AWS account if you don't already have one
2. Go to your AWS account, and go to S3
3. Create a new bucket. Uncheck block all public access and set the Object Ownership settig with ACLs enabled. Click Create Bucket
4. On the properties tab, scroll down to 'static website hosting' and 'use this bucket to host a website'. Set the home/default page to 'index.html' and error link as 'error.html', then save.
5. On the permissions tab, go to 'CORS configuration' and copy in the below.
``` 
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
```  
6. On the permissions tab, go to Bucket Policy and copy the ARN
7. Select generate policy. Select S3 Bucket Policy under policy type. Enter * for all Principals, and the action will be GetObject. Paste in the copied ARN into the ARN field.
8. Click add statement then generate policy, and copy this policy into the Bucket policy editor.
9. Before you press save, enter a star after the slash in Resource to allow access to all resources in this bucket. Click save
10. Go to the Access control list (ACL) tab, click edit and enable List for Everyone under the public access section.

### Setting up IAM

1. Go to your AWS account, and go to IAM
2. Click groups and create a new group. Call it something like manage-your-site-name.
3. Go to Policy and create policy. Go to the JSON tab and select import managed policy.
4. In the dialogue box, search for S3 and import the S3 Full Access Policy.
5. Get the ARN from your S3 bucket and paste it into the resources with and without the trailing *. It should look like this:
```
"RESOURCE": [
   "arn:aws....",
   "arn:aws..../*",
]
```
6. Click review policy. Give it a name and description. Click create policy.
7. Go back to groups and click your group to manage it. Go to the permissions tab, open Add Permissions and click Attach Policy. Search for your policy by it's name and select it. Click Add Permissions.
8. Go to Users and click Add User. Name your user something like your-site-name-static-files-user. Give them programmatic access. Select next.
9. Add the user to your group. Click through to the end and click Create User.
10. Download the CSV to get the users access key and secret access key. Ensure you download it now, because you won't be able to access it again.

## Connecting Django to S3.

1. Go to Gitpod. We will need to install 2 packages with the following commands:
pip3 install boto3
pip3 install django-storages
2. Update your requirements.txt file to include this:
```
pip freeze > requirements.txt
```
3. Add ```'storages',``` to your INSTALLED_APPS in settings.py.
4. In settings,py, update the AWS storage bucket name, region key and custom domain to match your own.
5. Go to Heroku. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
6. Add in the following variables with the relavant values. (Get the Keys from the CSV file). Set USE_AWS to Tue.
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
USE_AWS
```
7. Remove the disable collect static config var from Heroku.
8. Back on Gitpod, git add, commit and push your changes.
9. If your set up was correct, you should see a static folder in your S3 bucket, and your static files being rendered on the live site.

## Adding Media Files & Connecting Stripe & Emails

1. In AWS, add a folder called media. Inside it upload any photos you want rendered. In this project, it will be the background splash image, and the holding image.
2. Click next, manage public permissions and select manage public read access to these objects. Click next and upload.
3. In your Stripe account, add the Heroku app URL with a new webhook endpoint.
4. In Gitpod, update 'settings.py' with the new Stripe environment variables and email settings.
5. In Heroku, under your project settings, add the following CONFIG_VARS with your variables:
```
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
```
6. In your desired email provider, create an app password to allow Django to create and send emails.
7. In Heroku, under your project settings, add the following CONFIG_VARS with your variables:
```
EMAIL_HOST_PASS
EMAIL_HOST_USER
```


Back to [README.md](/README.md#deployment)