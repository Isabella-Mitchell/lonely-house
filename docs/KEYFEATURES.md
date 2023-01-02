# Key Features

## Overview

- Lonely House lets users view and book holiday listings. The main functionality revolves around a booking system that will allow users to use a date picker to pick their check in and checkout dates. The number of nights is calculated and that is timed by the price per night to calculate the order total. The user completes checkout to place their order. These dates become unavailable on the date picker, so other users cannot book the same dates. 

- One key feature of the website is this booking system. The main decisions arose around how to store booked dates in the database (through the Order Model), and then using that to update the datepicker. 

- Another key feature is the filtering system on the ‘All Listings’ page. For my user stories, I knew I wanted an extensive set of filters. However, as an admin, I wanted to make it easy to add listings and to keep my templates as clean as possible. So, I made several decisions based on trying to achieve both things. 

- Another key feature is Reviews. I introduced these towards the end of my project, so their design wasn't intrisic to the planning stages. I have gone into some more detail about the model, as it unique to this project, and how the average rating is calculated.

- I have gone into more detail about these features, following a typical user journey. 

## Key Feature 1 – Making a Booking 

### Listing Detail – Date Picker & Book Button 

- When the page loads, the Date Picker will check an array for booked dates. If a date is ‘booked’ it will be unavailable on the date picker. 

- The user cannot select a check-in or check-out date that is unavailable. However they can select a range of dates that includes an unavailable date. This is not ideal, so as a workaround, I have used a ‘Check  Availability’ button. Once clicked, the dates will be checked to see if any of the dates in the range the user has selected is also present in the booked dates array. If it is, then the user is informed and must select different dates. Else, the selected dates are displayed to the user, along with the number of nights and the total cost. They can then proceed to booking. 

- If at any point the user resets the dates, then the booking button will be hidden. This ensures that only dates that have been checked as available can be booked. 

- I have taken care to use ‘Night’ or ‘Nights’ based on whether the user has selected one or more nights.

- I take care to ensure that the Check Out Date is not counted as a night.

- The booked dates are passed from the Order Model to the Datepicker Javascript via a JSON dump in a hidden field on the product page. I decided to use this method as it was suitable for the scope of this project. I feel like there must be a better system, but as the information is not sensitive (the only information being pulled in from the orders is a list of dates), I do not think there is an immediate problem with this method.

- I have outlined further user and development features I would like to introduce to improve this feature in the Future Features section of my readme. However I feel this solution I have created is well suited for this project.

### Order Model with a Line Item per booked date

- The logic for the order model came before I built the checkout form. As I knew for the date picker I wanted a Python List of dates, I decided to make each date of the booking as a line item. One alternative would be to have a single line item with the check in and checkout date, and then use Python datetime to calulcate the dates in between. However, I felt like this would result in more computing each time a user loads the datepicker. I was also concerned by the fact python datetime uses months 1-12, compared to JavaScript using 0-11. So I felt there would be more room for errors if I was using python logic to calculate the available dates everytime and pass these into the Javascript. 

- I also realised I could use a date picker within the line item to select and change the date. This was ideal as it would mean invalid dates could not be entered by the admin. The default format for this is yyyy-mm-dd, so I have also used this on my datepicker. I feel a more user friendly format would be dd-mm-yyyy, but updating this is a low priority. 

- The Order Line Item Model includes the fields: 
    - Order - Required - Foreign Key to assign line item to order.
    - Listing - Required - Foreign key to assign a line item to a listing. any future purchases would need to be linked to a listing. In the case of insurance and car hire this would be applicable. I would need to consider how this would work if someone is making multiple listing bookings in one checkout 

    - Type – Required. Default is reservation. This could be checked using an if/else statement in future. 

    - Date – Not required – e.g. if not attached to a reservation. 

    - The one issue with this method is that the Check in and Checkout dates are not being passed into the order. These are present on the cart and checkout page (so could be reflected in the confirmation email). However, this may present future issue if the user wants to see their check in and check out date on their account. 

## Key Feature 2 – Filters and Listing Features 

TO FINISH


I knew that this was one part of my project that would vary significantly from the walkthrough, so I will explain my models in detail: 

Category Models 

Each listing has a unique category. In my project, I’ve decided to use this for the setting. E.g. ‘near the coast’. Or ‘in the forest’.  

In reality, I’m not sure how useful this would be to finding a listing, perhaps compared to ‘location’ or ‘dates available’, but I wanted there to be a category option that would suit a minimal amount of listings and also match my website branding and theme. E.g. users who are not sure what they want can get a quick idea of different options, and gives admin ideas of content to surface on the homepage.  

I also wanted this to be ‘unique’ in the sense that every listing can only belong to one category, the equivalent to Shopify’s ‘Product Type’. This can be useful for arbitrarily categorizing product. 

This required a name, and then a friendly name (optional) and a featured checkbox (default false). This will be used by the homepage. And gives the admin the option to change the featured content without having to edit the code. 


Facility Model   

This is set up as a ManyToManyField within the Listing model.  

I did quite a lot of research into this. One option I considered was making these individual tick boxes on the Listing model, however I knew this would make the listing model very large, and it may prove difficult to add or remove facilities in the future. Another option was adding these similar inline items. But in the same way, new facilities would need to be added in the model view. 

I realised the ideal scenario would be for administrators to be able to manage facilities in the admin, and not in the models. So I decided to make these as a Model. The admin needs to add a name, a friendly name (optional) and font awesome class (optional). It’s then easy to select mutliple in the Admin listing view. 

One drawback is that this will make adding facilities more time consuming when I reset the database, but it should prove a better way to futureproof my database. Also this is offset by the speed of creating new listings. 


Listing Model 

This takes it shell from the Product model on the walkthrough. I’ve also added fields relating to location (words and also google maps embed, latitude and longitude coordinates – in preparation for using the google maps API) 

There is a no_sleeps field – relating to how many people it sleeps. This is a filter. I decided to use this after conducted my research. I wasn’t sure whether it’s best to use the logic ‘sleeps at least...’ or ‘sleeps exactly...’ in my filter. But from my research I concluded it was normal to show ‘sleeps exactly’. 

There is featured tickbox for the same reason as the category model. 

Facilties manytomany – explained within the Facilties model section 

Images – 

 So I found images a bit confusing – and I have a lot more testing to do here 

I’m not sure I need the lead image URL field. This seemed useful if you knew the URL of the image and didn’t want to upload a new one to the media library. I should test this, and if it’s redundant, then remove it from my models. 

I knew I wanted to be able to include multiple images. My mentor told me the best way to do this was as line items. 

I then knew I needed to create a ‘featured image’ for use on the cart, checkout etc. 

I need to look more at my views, make some descisions and expand this section. 

Like the walkthrough, I haven’t made many sections required to make writing unittests easier. 

I need to add capacity 


## Key Feature 3 – Reviews