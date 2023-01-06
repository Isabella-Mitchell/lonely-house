# Lonely House

## Milestone Project 4 - Full Stack Development

<h2 align="center"><img src="docs/README/mockup.jpg"></h2>

* Lonely House is a fictional holiday letting website that allows users to browse and book holiday lettings.

* This is my Milestone Project 4 submission for Code Institute's Diploma in Web Application Development course. Lonely House is built using Django full-stack framework and uses a Relational Database. Technologies used include HTML, CSS, Javascript, Python, Google Maps API and Stripe payments.

* Key features include:
  - Filters: Users can apply filters to quickly and easily find options
  - Real-time Availability: Users can browse and select available dates (unavailable dates from existing bookings will be disabled).
  - Cart & Stripe Checkout: Users can add multiple bookings to their cart and proceed to checkout with Stripe.
  - Authentication: Users can create an account to save their contact information and view their order history
  - Reviews: Registered users can create, read, update and delete reviews

## Live Project

[View the live project here.](https://lonely-house.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/Isabella-Mitchell/lonely-house)

# Table of Contents

## Contents
- [User experience](#user-experience)
  * [User Stories](#user-stories)
- [Design](#design)
  + [Overview](#overview)
  + [Colour Scheme](#colour-scheme)
  + [Typography](#typography)
  + [Imagery](#imagery)
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
  + [Frameworks Libraries](#frameworks-libraries)
  + [Storage & Hosting](#storage-hosting)
  + [Payments](#payments)
  + [APIs](#apis)
  + [IDE & Version Control](#ide-version-control)
  + [Other Tools](#other-tools)
  + [Testing & Code Validation](#testing-code-validation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  + [Code](#code)
  + [Media](#media)
  + [Content](#content)
  + [Acknowledgements](#acknowledgements)

# User Experience

## User stories

| User Story ID | As a/an | I want to be able to... | So that I can... |
| --- | ----------- | ----------- | ----------- |
 | Viewing and Navigation | 
| 1 | Customer | View a list of accomodation | Quickly compare and select different accomodation options | 
 | 2 | Customer | View individual accomodation details | Find out further information about and see further images of the listing | 
 | 3 | Customer | See an embedded google maps map | Plan my journey to the site from my location | 
 | 4 | Customer | Quickly identify key features of accomodation through icons and keywords | Decide if it's appropriate for the type of stay I want | 
 | 5 | Customer | See the  price update automatically when I enter my stay length | To help me not overspend | 
 | 6 | Customer | See available dates | Know I'll have the cabin when I book it due to a responsive date picker | 
 | 7 | Customer | See ratings and reviews | To help me make my decision | 
 | Registration and User Accounts | 
 | 8 | Site User | Easily register for an account | Have a personal account and be able to see my profile | 
 | 9 | Site User | Easily login or logout | Access my personal info | 
 | 10 | Site User | Easily recover my password | Access my account even if I've forgotten my password | 
 | 11 | Site User | Easily access my user profile | Access my account quickly | 
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
 | 26 | Customer | View an order confirmation after checkout | Know my order has gone through and I haven't made any mistakes | 
 | 27 | Customer | Recieve an email confirmation after checkout | Keep a confirmation for my records | 
 | Landing Page | 
 | 28 | Store Owner | Showcase featured listings | Give website visitors a quick sense of the types of listings available on my website | 
 | 29 | Store Owner | Showcase featured categories | Give website visitors a quick sense of the types of categories available on my website | 
 | 30 | Store Owner | Showcase featured reviews | Show social proof and build trust with website visitors | 
 | Ratings & Reviews | 
 | 31 | Customer | To be able to add a Rating/ Review | In case I wish to add a rating and or a written review | 
 | 32 | Customer | To be able to delete a Rating/ Review | In case I wish to delete a rating and or a written review | 
 | 33 | Customer | to be able to edit a Rating/ Review | In case I wish to edit a rating and or a written review | 

## Design

### Overview

- The website design is simple yet characterful. As the name 'Lonely House' suggests, the website's USP is that it offers holiday lettings that are remote and situated in nature. They offer a chance for people to escape busy lives, relax in nature and slow down. The aesthetic of the website, with its soft edges and rounded corners, warm colours and rich visual references to nature, was inspired by this idea.

### Colour Scheme

- Lonely House uses a limited colour scheme of warm creams, greys and greens. Inspiration for the colour scene came from nature and imagery I sourced in preparation for the project.

- I used the Material Design Colour Tool to help me decide on colour choices. I used the [WebAim Contrast Checker](https://webaim.org/resources/contrastchecker/) to ensure my colour choices had a high enough colour ratio.

<h2 align="center"><img src="docs/README/colours-swatches.jpg"></h2>

### Typography

- Headings are in Josefin Slab, with serif as a fallback font. With slight typewriter style attributes, Josefin Slab brings a subtle sense of character to the website. The body copy is in Jost with sans-serif as a fallback font. The choice of simple, easily-legible typefaces means that the text will be easy to read on all device sizes. 

### Imagery 

- Imagery is a very important feature of the website, as users need to be able to see listings to be encouraged to book a holiday.

- Images are mostly displayed in Bootstrap Carousels. These allow the admin to add multiple photos without worrying about them taking up lots of space on the page.

- The admin can choose to set a featured image. This is the image that appears first by default on the all listings and listing detail page. There is a fallback 'holding' image if the admin does not set an image.

- Consistent aspect ratios have been used to bring visual harmony to the site across different page layouts.

### Icons

- I used icons from Font Awesome extensively on the website. They are used within the nav bar to reduce the need for verbose descriptions such as 'search. I have used them on buttons to reinforce the action of the button. They are also used within listings to visually represent different facilities, ratings, location pin etc. I have added screen reader alternatives where I felt it was necessary and appropriate.

### Cards

- I have used Bootstrap cards to visually organise content. These include content that appears as multiples on a page such as listings and reviews. I have also used single cards as containers for content such as the cart, checkout form and checkout confirmation.

# Wireframes

- [View my wireframes in PDF form here](#docs/README/wireframes/wireframes.pdf).

## Changes to Wireframes

Due to time constraints and decisions made during the project, there are some differences between the live site and my initial wireframes

- Added add/edit/delete reviews page within the User Profile
  * I initially was going to add the review CRUD functionality to the listing page. But during the project I realised it may be more intuitive for users to be able to see all their reviews in one place, instead of scattered on different pages.

- Added Cart step and cart button to nav
  * Originally I wasn't planning on adding a cart step, as many of the holiday letting websites I looked at for research did not have one. However, my mentor suggested it would be a good idea as additional 'add-ons' such as insurance and car rental could be introduced as a future feature.

- Added 'Search and Book' button to nav and as a banner on smaller screen sizes
  * As I was building the website, I realised it wasn't very easy for users to get to the 'all listings' page. I therefore added a button to the navigation making it easier and more intuitive for users to browse listings.

- Didn't include map view on listing page
  * I set coordinates for listings and made it a required field so that I could show a google map on each listing page, and also let users see a map view of all listings. However, due to time constraints I was not able to realise the latter feature.

- Didn't add back to top button at bottom of pages
  * This feature wasn't a priority during development, so I omitted it due to time constraints. However in reality the all listings page would need some way to manage a lot of listings, whether that's infinite scroll or pagination.

# Features

## All Pages

- Responsive design
- Semantic HTML
- Custom CSS to give the website a cohesive and user-friendly appearance

### Header & Navigation

- Website H1 Heading
- Navigation, including links to:
  - Search & Book (all listings page)
  - Search (search bar)
  - User Profile Options (register/ login/ view profile/ view reviews)
  - Cart (changes colour if cart is not empty)

### Footer

- About
- Social Links 

### Messages

- Success message (including cart link when applicable)
- Info message
- Error message
- Warning message

## Homepage

- Jumbotron
- Featured Listings
- Featured Categories
- Featured Reviews
- 'Call to action' buttons

## All Listings Page

- Splash Image
- Filters, featuring:
  - Collapse on smaller screens
  - Checkbox dropdown
  - Applied filters shown to user
  - Ability for user to edit applied filters even after page refresh
  - Shown listing count
  - Reset filters button
- Listing Cards, featuring:
  - Featured Image or Fallback Image
  - Image carousel if multiple images
  - Facility tooltips
  - Average Rating
  - Book button

## Listing Detail Page
  - Featured Image or Fallback Image
  - Image carousel if multiple images
  - Date range picker, featuring:
    - Greys out unavailable dates
    - Check availability button
    - Messages if user selects invalid dates
    - If dates are valid, total price is shown to user
    - Book now button (adds to cart)
  - Key features
  - Description with line breaks
  - Location
  - Google Maps API
  - Reviews
  - Average rating

## Cart Page
- Booking details for each listing added to cart, featuring:
  - Checkout date is not counted as a night
  - Confirmation of dates selected
  - Subtotal
- Remove from cart option
- Cart Total
- Secure Checkout button
- Back button

## Checkout Page
- Order summary
- Checkout form, featuring:
  - Option to save information to profile
  - Auto populates with content saved to user profile
  - Stripe payment

## Checkout Confirmation Page/ Email
- Checkout confirmation page
- Sends booking confirmation email

## Authentification Pages
- Register/ Log In/ Log Out/ Reset Password Pages
- Features largely provided by Django allauth

## User Profile Page
- Default information form
- Order history
- Users must be logged in
- Users can only access their own User Profile

## Reviews Pages
- Users can view all their reviews
- Users must be logged in
- Users can only access their own reviews

## Add/ Edit/ Delete Reviews
- Add Review Page
- Edit Review Page
- Delete Review
- Users must be logged in
- Users can only access their own reviews

# Future Features

## User Experience Features

### Datepicker

#### Users would be able to book their Check In date on an existing Check Out date.

* The datepicker and booking logic means that a Check out date is not reflected as a night on the datepicker, while the Check In date counts as a night. This is ok if users book consecutive dates, as the later booking can check-in on the same day that the initial booking's check out date. E.g. 5th-7th June and 7th-9th June. However if the trips are not booked consecutively, the later booking cannot select the initial booking's Check-in date. E.g. 7th-9th June means that 5th-7th of June cannot be booked, instead they could book 4th-6th June. 

* A future feature would be a more complex datpicker that allows this.

#### Date range picker that does not allow users to select a range that includes an unavailable date.

* Currently, if a user selects a date range that includes on or more unavailable date. E.g. a user tries to book 1st-10th June when 5th June is booked, then they will be notified and informed to select new dates.

* A future feature would be to improve the date range picker functionality so that the user can't select unavailable dates within a range of dates.

#### Optimise date range picker appearance on smaller screens

* I think the date range picker could be larger on smaller screens, making it more accessible.

### Filters

#### Make applied filters act like 'tags' with a close button to remove filter

* When users apply filters, they can see the filters applied appear as text on the screen

* A future feature would be to add a close icon to applied filters, making them easier to close. Currently users have to open up the dropdown menu and unselect the checkbox, else reset filters.

#### Optimise filters appearance on smaller screens

* I think the filter drop downs could have better spacing on smaller screens, making them more accessible.


### Listings Pages

#### Map View

* In my initial wireframes, I intended to create a map view of listings, which would allow users use a map to browse listings, rather than a list view as I currently have.

* Due to time contrainsts I was unable to add this feature

#### Curate Listing Order

* A future feature would be to include a 'ranking' field on Listings so that the admin can choose the order that the listings appear on the All Listings page.

#### Add ordering options for users

* A future feature would be to make it possible for users to customise the order of listings. E.g. cheapest first.

#### Category 'Collections'

* A future feature would be to create collections. I noticed that when a user selects a 'featured category' from the homepage, they do not see what Category is being applied. One way around this would be to make category collections so these featured links could navigate there.


### Cart & Checkout

#### Amend Booking/ Cart

* If a user returns to a listing page from the cart, they do not have a clever way to amend their booking.

* The user can select new dates and add the property to cart to amend their booking, however this is not intuitive. I could add a toast/ alert warning the user they already have a booking in their cart, and if they select new dates they will lose their existing booking.

* A future feature would be, if users navigate to a listing which is currently in their cart, then their existing booking dates would populate the datepicker.

#### More descriptive 'Add to Cart' toasts

* If a user adds a booking to cart, they can see more information in the success toast.

#### Check in and Checkout date being reflected in Order Confirmation

* Users cannot currently see their check in and check out date once they have placed their order. They currently only see the nights they have booked. In my own experience of booking holiday lets, it's very important that the user is clear on these dates. There is a chance, by only reflecting the nights, that users might think the final date is the checkout date, when in fact it is the night after.

* Ideally, these dates would be calculated from the line items. E.g. if a line item is deleted (like the user is cutting their trip shorter by one day), then the checkout date automatically calculates itself and updates.

* A future feature would be to reflect the user's check-in and check-out dates in their order confirmation.

#### Update dates shown to user format to be dd-mm-yyyy 

* The format is yyyy-mm-dd due to the default date format on the Python order model. I'm sure this could be changed but it is low priority. I also realised I could use a date picker within the line item to select and change the date. This was ideal as it would mean invalid dates could not be entered by the admin. The default format for this is yyyy-mm-dd, so I have also used this on my datepicker. I feel a more user-friendly format would be dd-mm-yyyy, but updating this is a low priority.

* A future feature would be to present dates to the user in a more human-friendly fashion.

#### Further Listing Information in Order Confirmation

* Users cannot currently see any address or contact information for their listing in their checkout confirmation.

* A future feature would be to add more fields to the Listing model, or create a new model called ListingInformation, which could include more information about listings to be provided to the user such as Address, contact details and travel information.

### Reviews

#### Implicitly associate reviews with listings

* On the add or edit review form, users can select any listing to leave a review for. This is not very good UX, and also might cause a review to be associated with the wrong listing, and allow unvalidated reviews and spam.

* A future feature would be to only permit users who have made a booking on a listing to leave a review about that listing.

### Further Apps

#### Admin area

* A future feature would be to create an admin area within the website, so admins can easily add, edit or delete content without needing to open up the website admin.

#### Contact Form

* A possible future feature would be a contact form to let customers easily contact the website admin

#### Newsletter Subscribe

* A possible future feature would be a newsletter subscription form to let customers easily subscribe to Lonely House Newsletters

#### Wishlist

* A possible future feature would be a wishlist for logged in users. It would encourage users to register, as they could save lisitngs to their wishlist, making them quick and easy to find.

## Development Features

#### Use Jest for Javascript testing and replace jQuery where possible

* I've had issues in previous projects with using Jest on .js files that include jQuery. I think the cause of the issue is the fact that I'm using a CDN to import jQuery.

* As the focus of this project is Python and I have written Unittests, I decided to not refactor my Javascript to allow me to use Jest to test my Javascript code.

* A future feature would be to replace jQuery with Javascript in my scripts, and write tests for my scripts.

#### More tests for checkout

* Due to time constraints, I have not written many tests for much of the Stripe payment functionality in my checkout app. This is a future feature I would prioritise.

#### Check if item is a reservation in Checkout views

* I included a reservation field in my OrderLineItem to allow me to offer add-ons in checkout, e.g. an insurance add on. However, I have not included logic in my Checkout Views that checks for this. This would need to be rectified before further product types are added.

#### Add in a nights calulator to Cart Contexts.

* I am currently taking this data from the listing_detail page via a hidden field. A future feature could be to add in a nights calulator to ensure the user cannot manipulate this number.

#### Sleeps could be a model like categories and filters

* Currently the sleeps filter is populated by a Constant. This means that if a listing was added that slept 18, a new number would have to be applied to the Constant.

* A future feature would be to refactor the necessary views, create a sleeps model and amend the listing model, so that this works similarly to Categories. This makes it easy for admins to add new listings, and the number automatically appears in the Sleeps filter.

# Data Model

## Considerations

A few of the key points I had to consider when designed my database schema was:
- How booked dates would be recorded in the order model
- How booked dates would be 'passed' into the listings page reflected by the datepicker
- How I could add multiple facilities to my listings, while keeping the listing model streamlined.
- How I could make it easy for Admin to add and edit facilities and categories.
- How listings could have multiple images, one image or no images

## Database Schema

The following Data models were used:

- Listings - stores information for each holiday let
- Category - stores information about Listing category
- Facility - stores information about Listing facilities
- Image - stores multiple images for listings
- Order - stores order information
- OrderLineItem - stores booking information (one is created for each date)
- UserProfile - stores user information (relates to Django Allauth User model, not included in this schema)
- Review - stores rating and review information

This diagram outlines each model's fields and illustrates the relationship between the models:

<h2 align="center"><img src="docs/README/db-schema.png"></h2>

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks & Libraries

- [Django](https://www.djangoproject.com/)
  - This website is built using Django, a high-level Python web framework. Lonely House features multiple apps with model, view and template layers. I have also used Django to provide an admin view, create forms and test my website. Further features used include [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) for user authentification, Pillow for uploading images, and Crispy Forms.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language I've used with Python to add logic to my html templates.

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to Bootstrap components and within my scripts.

- [Bootstrap 4](https://getbootstrap.com/) 
  - I used bootstrap throughout the site to make it responsive. The website uses Bootstrap's Containers, Grid System, Flexbox and Spacing utilities. I sourced code from the Bootstrap documentation when building the Navbar, Image Carousels, Cards and Buttons.

- [Google Fonts](https://fonts.google.com/)
  - Fonts are imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome across the website

- [Bootstrap Date Picker](https://bootstrap-datepicker.readthedocs.io/en/latest/index.html)
  - I used this CDN to provide the date range picker on the listing detail page.

## Storage & Hosting

- [Heroku](https://id.heroku.com/login)
  - Heroku is the deployment source I used for this project.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

- [Amazon Web Services](https://aws.amazon.com/)
  - AWS is used to host and store static files and media.

- [ElephantSQL](https://www.elephantsql.com/)
  - ElephantSQL is used to host the website's PostgreSQL database.

## Payments

- [Stripe](https://stripe.com/gb)
  - Stripe is used to handle website payments.

## APIs

- [Google Maps API](https://developers.google.com/maps/)
  - I used Google MAPS API to show the listing's location on a google map via coordinates.

## IDE & Version Control

- [Git](https://git-scm.com/)
  - Git was used as a version control in the terminal.

- [Gitpod](https://gitpod.io/)
  - Gitpod was used to create my files and where I wrote the code.

## Other Tools

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
  - Unsplash was used to source the website imagery.

- [ChatGPT](https://openai.com/blog/chatgpt/)
  - OpenAI's ChatGPT was used in part to generate Listing Descriptions and user Reviews.

## Testing & Code Validation

The following tools were used for testing and code validation. You can see results in the Testing section of this README.

- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [Coverage](https://coverage.readthedocs.io/en/7.0.1/)
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en)
- [Python Linting on Gitpod](https://open-vsx.org/extension/ms-python/python)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Web Accessibility Evaluation Tools](https://wave.webaim.org/)
- [Chrome Screen Reader](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en)

# Testing

- Please refer [here](docs/TESTING.md) for more information on testing of the Lonely House website

# Deployment

- Please refer [here](docs/DEPLOYMENT.md) for more information on the deployment of the Lonely House website

# Credits

## Code

### Code Institute:
  - I sourced the framework for this project from the Code Institute Boutique Ado walkthrough. I have customised my website wherever possible. My checkout, Stripe payments, webhooks and email verification are very similar to the walkthrough as I desired to focus more on making my website fit for my users goals, rather than adding any further checkout or payment functionality.

### Django:
  - I referred to the Django documentation whilst building my project. I found articles on [testing](https://docs.djangoproject.com/en/4.1/topics/testing/) and [making database queries](https://docs.djangoproject.com/en/4.1/topics/db/queries/) particularly useful.

### Bootstrap:
  - I have used Bootstrap classes throughout my project, including for layout utilities and cards. I sourced code from the Bootstrap documentation when building the navbar, image carousels, and dropdowns. These were sourced through the [Bootstrap documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

### Bootstrap Datepicker:
  - I referred to [Bootstrap Datepicker documentation](https://bootstrap-datepicker.readthedocs.io/en/latest/markup.html#date-range) for the initial set up of my Bootstrap Date Picker

### Stack Overflow: 
  I used and/ or referenced code from the following Stack Overflow articles. Most relate to my datepicker and filters scripts.
- Datepicker
  - https://stackoverflow.com/questions/21146382/bootstrap-datepicker-restrict-available-dates-to-be-selected
  - https://stackoverflow.com/questions/62493468/date-range-not-selected-in-calendar-after-value-changed-programmatically 
  - https://stackoverflow.com/questions/39469538/bootstrap-datepicker-date-range-from-and-to 
  - https://stackoverflow.com/questions/14409779/bootstrap-datepicker-how-to-set-the-start-date-for-tomorrow 
  - https://stackoverflow.com/questions/16681875/how-to-get-the-selected-date-value-while-using-bootstrap-datepicker 
  - https://stackoverflow.com/questions/4413590/javascript-get-array-of-dates-between-2-dates?page=1&tab=scoredesc
  - https://stackoverflow.com/questions/55746578/gray-out-all-but-certain-dates-on-bootstrap-datepicker
  - https://stackoverflow.com/questions/3605214/javascript-add-leading-zeroes-to-date
- Filters
  - https://stackoverflow.com/questions/14544104/checkbox-check-event-listener
  - https://stackoverflow.com/questions/68588423/local-storage-isnt-storing-the-value-in-input-field-on-refresh
  - https://stackoverflow.com/questions/15044340/jquery-set-checkbox-checked
  - https://stackoverflow.com/questions/54249017/distinct-on-fields-is-not-supported-by-this-database-backend
- Linking admin button to main menu
  - https://stackoverflow.com/questions/1022236/linking-to-the-django-admin-site
- Text area line breaks
  - https://stackoverflow.com/questions/1894930/django-allow-line-break-from-textarea-input
    
### Meetanshi Blog
  - I referred to [this blog post](https://meetanshi.com/blog/reload-current-page-without-losing-any-form-data-in-javascript) for help on using local storage (for Filters)

### W3Schools: 
  - I referred to [this article](https://www.w3docs.com/snippets/css/how-to-set-the-size-of-a-checkbox-with-html-and-css.html) for help on styling checkboxes (for Filters)

### GeeksForGeeks:
  - I referred to [this article](https://www.geeksforgeeks.org/datefield-django-models/) for help using a Datefield in my orderlineitem model

### Youtube:
  - I watched [this video](https://www.youtube.com/watch?v=8ptKpzW-KLo) by Frontend Paathshala to help me set up the CDN for bootstrap date picker v4.6
  - I followed [this tutorial](https://www.youtube.com/watch?v=pRiQeo17u6c) by Traversy Media to set up the Google Maps Geocoding Service API.

## Content

- As the listings are fictitious, I used [ChatGPT](https://openai.com/blog/chatgpt/) to generate listing descriptions.

- I took inspiration from the [Landmark Trust](https://www.landmarktrust.org.uk/) website for the listings names, locations and facilities.

- I looked at the following websites for inspiration on branding and functionality
  - [Landmark Trust](https://www.landmarktrust.org.uk/)
  - [Air BnB](https://www.airbnb.co.uk/)
  - [Center Parcs](https://www.centerparcs.co.uk/)
  - [The Modern House](https://www.themodernhouse.com/)
  - [Brickworks](https://www.brickworkslondon.com/)
  - [Suitcase Magazine](https://suitcasemag.com/)

## Media

- As I sourced all the imagery for the Lonely House website from Unsplash, there is an extensive list of media credits.

- Please refer [here](docs/README/CREDITS.md) for full Media credits for the Lonely House website.

## Acknowledgements

- Thank you to my Mentor Akshat Garg for helpful feedback, industry insights and recommended tools.

- Thank you to Shahidul Islam for participating in the peer code review on the Code Institute Slack channel.

- Thank you to the Code Institute London Community for their encouragement and technical support.

- Thank you to the tutors and staff at Code Institute for their support.

- Thank you to Ben Smith and Pasquale Fasulo at City of Bristol College for their support.

Please note this is a personal project. This website is purely for the sake of the developer's portfolio and not for public consumption.

Isabella Mitchell, 2023.