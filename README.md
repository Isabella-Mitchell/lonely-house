# Lonely House

## Milestone Project 4 - Full Stack Development

* Lonely House is a fictional holiday letting website that allows users to browse and book holiday lettings.

* This is my Milestone Project 4 submission for Code Institute's Diploma in Web Application Development course. Lonely House is built using Django full stack framework and uses a Relational Database. Technologies used include HTML, CSS, Javascript, Python, Google Maps API and Stripe payments.

* Key features include:
  - Filters: Users can apply filters to quickly and easily find options
  - Real-time Availability: Users can browse and select available dates (unavailable dates from exisiting bookings will be disabled).
  - Cart & Stripe Checkout: Users can add multiple bookings to their cart and proceed to checkout with Stripe.
  - User Profile : Users can create an account to save their contact information and view their order history
  - Reviews: Users can create, read, update and delete reviews within their User Profile

## Live Project

[View the live project here.](https://lonely-house.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/Isabella-Mitchell/lonely-house)

# Table of Contents

## Contents
- [Overview](#overview)
- [User experience](#user-experience)
  * [User Stories](#user-stories)
    + [First-time Users](#first-time-users)
    + [Returning Users](#returning-users)
    + [Business Owner](#business-owner)
- [Design](#design)
  + [Overview](#overview)
  + [Colour Scheme](#colour-scheme)
  + [Typography](#typography)
  + [Imagery and Aesthetics](#imagery-and-aesthetics)
  + [Icons](#icons)
  + [Cards](#cards)
- [Wireframes](#wireframes)
- [Features](#features)
- [Future Features](#future-features)
  + [User Experience Features](#user-experience-features)
  + [Development Features](#development-features)
- [Data Model](#data-model)
- [Technologies used](#technologies-used)
  + [Languages Used](#languages-used)
  + [Frameworks Libraries and Programs](#frameworks-libraries-and-programs)
- [Testing](#testing)
- [Deployment](#deployment)
  + [Creating a Gitpod Workspace](#creating-a-gitpod-workspace)
  + [GitHub Pages](#github-pages)
  + [Forking the GitHub Repository](#forking-the-github-repository)
  + [Making a Local Clone](#making-a-local-clone)
  + [Creating an application with Heroku](#creating-an-application-with-heroku)
- [Credits](#credits)
  + [Code](#code)
  + [Media](#media)
  + [Content](#content)
  + [Acknowledgements](#acknowledgements)

# Overview

The purpose of 

The key features include

Database 



# User Experience

## User stoires

| User Story ID | As a/an | I want to be able to... | So that I can... |
| --- | ----------- | ----------- | ----------- |
 | Viewing and Navigation | 
| 1 | Customer | View a list of accomodation | Quickly compare and select different accomodation options | 
 | 2 | Customer | View individually accomodation details | Find out further information about and see further images of the listing | 
 | 3 | Customer | See an embedded google maps map | Plan my journey to the site from my location | 
 | 4 | Customer | Quickly identify key features of accomodation through icons and keywords | Decide if it's appropriate for type of stay I want | 
 | 5 | Customer | See the  price update automatically when I enter my stay length | To help me not overspend | 
 | 6 | Customer | See available dates | Know I'll have the cabin when I book it due to a responsive date picker | 
 | 7 | Customer | See ratings and reviews | To help me make my desision | 
 | Registration and User Accounts | 
 | 8 | Site User | Easily register for an account | Have a personal account and be able to see my profile | 
 | 9 | Site User | Easily login or logout | Access my personal info | 
 | 10 | Site User | Easily recover my password | Access my account even if I've forgotten my password | 
 | 11 | Site User | Recieve an email confirmation after registering | Verify that my email was correctly entered | 
 | 12 | Site User | Have a personalised user profile | With my personal order history and be able to update my default billing address | 
 | 13 | Site User | Be able to make an account after checkout | To be able to see my booking if I haven't made one before | 
 | 14 | Site User | Make an account to leave ratings and reviews | Comment on my stay and help others make a choice | 
 | 15 | Site User | See my ratings and reviews in my user profile | So I can see what reviews/ ratings I have left easily | 
 | Sorting and Searching | 
 | 16 | Customer | Sort/ Filter listings by dedicated filters. e.g. number of people | Easily identify suitable options with features I want for my stay | 
 | 17 | Customer | Be able to edit my filters even after page refresh | To make it quicker and easier to apply filters | 
 | 18 | Customer | Search for a product by name, description or key feature | Find a specific accomodation I'd like to book | 
 | 19 | Customer | Easily see what I've searched for and the number of results | Be able to see which options match my search | 
 | 20 | Customer | See if there are no search results | Quickly see there is nothing that matches my search | 
 | Purchasing and Checkout | 
 | 21 | Customer | Be able to select the stay I want and book through the product page | Start the booking process | 
 | 22 | Customer | Be able to review my cart and add multiple bookings | So I don't have to go through the checkout process multiple times, or go to checkout before I am ready | 
 | 23 | Customer | Be able to review my order details | So I can double check I have booked the right accomodation for the right dates with the right number of people | 
 | 24 | Customer | Easily enter my payment information | Check out quickly with no hassles | 
 | 25 | Customer | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | 
 | 26 | Customer | View an order confirmation after checkout | Know my order has gone throigh and I haven't made any mistakes | 
 | 27 | Customer | Recieve an email confirmation after checkout | Keep a confirmation for my records | 
 | Landing Page | 
 | 28 | Store Owner | Showcase featured listingd | Give website visitors a quick sense of the types of listings available on my website | 
 | 29 | Store Owner | Showcase featured categories | Give website visitors a quick sense of the types of categories available on my website | 
 | 30 | Store Owner | Showcase featured reviews | Show social proof and build trust with websitevisitors | 
 | Ratings & Reviews | 
 | 31 | Customer | To be able to add a Rating/ Review | In case I wish to add a rating and or a written review | 
 | 32 | Customer | To be abl to delete a Rating/ Review | In case I wish to delete a rating and or a written review | 
 | 33 | Customer | to be able to edit a Rating/ Review | In case I wish to edit a rating and or a written review | 

## Design

### Overview

- The website design is simple yet characterful. As the name 'Lonely House' suggests, the website's USP is that it offers holiday lettings that are remote and situated in nature. They offer a chance for people to escape busy lives, relax in nature and slow down. The aesthic of the website, with its soft edges and rounded corners, warm colours and rich visual references to nature, was inspired by this idea.

### Colour

- Lonely House uses a limited colour scheme of warm creams, greys and greens. Inspiration for the colour scene came from nature and imagery I sourced in preparation for the project.

- I used the Material Design Colour Tool to help me decide on colour choices. I used the [WebAim Contrast Checker](https://webaim.org/resources/contrastchecker/) to ensure my colour choices had a high enough colour ratio.

### Typography

- Headings are in...

### Imagery 

- There is a large emphasis placed on imagery and icons. 

### Icons

- I have used icons on ...

### Cards

- I have used ...

# Wireframes

- [View my wireframes in PDF form here](#).

# Features

## All Pages

### Header & Navigation

- The website title 'Lonely House' is a H1 heading in the top left hand side of the website. It's easy to read and visible on every page of the website.

- The navigation is clean and minimal. I took inspiration from holiday and estae agent listing website which direct users to one 'all listings' page where they can apply filters.

- There is a 'Search & Book' button which takes the user to the all listings page. This appears as a banner on smaller screens to keep it visible and easily-accessible, without making the website header too large.

- There is a search bar icon. Users can click this to get the search bar to drop down. This makes it easily accessible without cluttering up the screen.

- Users can use a dropdown to access their account, log in or sign up.

- There is a cart link, making it easy for users to view and edit their cart, or proceed to checkout.

### Footer

- 

### Messages

## Homepage

### Splash Image

### Featured Listings

### Featured Categories

### Featured Reviews

### Call To Action Buttons

## All Listing Page

### Splash Image

### Listing Cards
- Featured Image/ Fallback Image
- Feature 'toasts'
- Average Rating

### Filters

## Listing Detail Page

### Image Carousel

### Date Picker/ Availability Checker

### Description

### Google Map

### Reviews

## Cart

### Table

## Checkout

## Checkout Confirmation

## Register/ Log In Pages

## Profile Page

## Reviews Page

## Add/ Edit/ Delete a Review

# Future Features

## User Experience Features 

## Development Features

# Data Model

EXPAND - go into in depth detail

- [View my Database structure in PDF form here](#).

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks Libraries and Programs

- [Heroku](https://id.heroku.com/login)
  - Heroku is the deployment source I used for this project. I'm also using it for the Postgres relational database

- [MongoDB](https://www.mongodb.com/)
    - I'm using MongoDB for my non-relational database.

- [Flask](https://flask.palletsprojects.com/en/2.2.x/templating/)
  - Templating language I've used with Python to add logic to my html templates.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language I've used with Python to add logic to my html templates.

- [Materialize CSS](https://materializecss.com/)
  - Front-end library with HTML, CSS and Javascript based componants. I used features including Nav bar, Cards, Buttons and Forms.

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to MaterialiseCSS componants.

- [Google Fonts](https://fonts.google.com/)
  - Two fonts are imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome on buttons.

- [Git](https://git-scm.com/)
  - Git was used as a version control in the terminal.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

- [Gitpod](https://gitpod.io/)
  - Gitpod was used to create my files and where I wrote the code.

- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to create Wireframes for the project during the initial planning stage.

- [Techsini](https://techsini.com/multi-mockup/)
  - Techsini was used to help check responsiveness and take screenshots of the page at different screen sizes.

- [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html)
  - Photoshop was used to resize images for the website.

- [TinyPNG](https://tinypng.com/)
  - TinyPNG was used to compress images for a faster loading time.

- [WebFormatter](https://webformatter.com/html)
  - WebFormatter was used to help beautify the code.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.

- [dbdiagram](https://dbdiagram.io/)
  - Tool used to mock up database structure diagram.

- [Unsplash](https://unsplash.com/)
  - Unsplash was used to source the jumbatron imager.

# Testing

- Please refer [here](TESTING.md) for more information on testing of the Gather website

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

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/Isabella-Mitchell/gather-recipe-website)
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
> Cloning into `gather-recipe-website`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a requirements.txt file by typing ``` pip3 freeze --local > requirements.txt ``` into the Gitpod CLI. Ensure this is added to your .gitignore file.
2. Create a Procfile by typing ```echo web: python app.py > Procfile```. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - MONGO_DBNAME : Your MongoDB database name
  - MONGO_URI : This can be found on MongoDB by going to Clusters, Connect, Connect to your application
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right and select run console. Enter ```python3``` to access the python intepreter.
13. Then type ```From gather import db```. Then type ```db.create_all()```. You can then exit the console.

# Credits

## Code

- Bootstrap

- Code Institute:

- Stack Overflow: 

- W3Schools: 

- Geekflare: 

- Documentation:

## Content

- 

## Media

- Credit 

## Acknowledgements

- Thank you to my Mentor Akshat Garg for helpful feedback, industry insights and recommended tools.

- Thank you to ... for participating in the peer code review on the Code Institute Slack channel. Thank you to my family for manually testing the website and for feedback.

- Thank you to the Code Institute London Community for their encouragement and technical support.

- Thank you to the tutors and staff at Code Institute for their support.

- Thank you to Ben Smith and Pasquale Fasulo at City of Bristol College for their support.

Please note this is a personal project. This website is purely for the sake of the developer's portfolio and not for public consumption.

Isabella Mitchell, 2022.