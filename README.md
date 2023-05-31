
# Holiday booking 

If you're looking to book a holiday online, there are several options available to you. Here are the steps you can follow to book your holiday online:
Decide on your destination and dates of travel. 
Holiday Booking platform that includes a time-off tracking system for employees. It allows you to request vacation time, view your remaining balance, and see who else on your team has scheduled time off.


# 375 x 1180
![375x1180](https://github.com/ocimar84/holidays/assets/79640465/d8d3814d-b5eb-4534-a8cb-b1ce760cdfc9)
# 768 x 1180
![768x1180](https://github.com/ocimar84/holidays/assets/79640465/4e0bd822-223a-4a64-8fc4-13e6b842679a)
# 1024 x 1180
![1024x1180](https://github.com/ocimar84/holidays/assets/79640465/72adf66e-0045-44b5-8308-7112915980f4)
# 1440 x 1180
![1440x1180](https://github.com/ocimar84/holidays/assets/79640465/69aab250-57fd-423f-873b-058f5a960394)



# Live Site

[Holidays](http://holidays-ocimar.herokuapp.com/)

# Content

* [Business Goals](#business-goals)

* [User experience](#user-experience)
    * [User stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [Crud Functionality](#crud-functionality)
    * [Wireframes](#wireframes)

* [Feautres](#features)
    * [Header](#header)
    * [Hero image](#hero-image)
    * [Most popular rooms](#most-popular-rooms)
    * [About us](#about-us)
    * [Footer](#footer)
    * [Rooms](#rooms)
    * [Make a booking sign up/Login](#make-a-booking-message)
    * [Create an account](#create-an-account)
    * [Sign in](#sign-in)
    * [Log out](#log-out)
    * [Place your booking](#place-your-booking)
    * [Time slot unavailable message](#time-slot-unavailable-message)
    * [Email confirmations](#email-confirmations)
    * [Manage booking](#manage-booking)
    * [Update booking](#update-booking)
    * [Updated message](#updated-message)
    * [Admin panel](#admin-panel)
    * [404 Page](#404-page)
    * [Responsive](#responsive)
    * [Future features](#future-features)

* [Testing](#testing)
    * [Lighthouse](#lighthouse)
    * [HTML Validator](#html-validator)
    * [CSS Validator](#css-validator)
    * [Python Validator](#python-validator)
    * [Javascript](#jshint-validator)
    * [Defects](#defects)
    * [Manual](#manual)

* [Security Features](#security-features)

* [Bugs](#bugs)
    * [Solved](#solved)
    * [Left to solve](#left-to-solve)

* [Credits](#credits)
    * [Code](#code) 
    * [Images](#images)
    * [Technology used](#technology-used)

* [Deployment](#deployment)
    * [Local deployment](#local-deployment)
    * [Production Deployment](#production-deployment) 
        * [Create heroku app](#create-heroku-app)
        * [Connect Postgres database](#connect-postgres-database)
        * [Deploy app on heroku](#deploy-app-on-heroku)
        * [PostgreSql](#postgresql)

* [Acknowledgements](#acknowledgements)

# Business goals

The objective of a holiday booking company in this context would be to provide an exceptional service that meets the needs of employees and companies, leading to a positive experience for the corporate group. This can help build long-term relationships. In addition, it can help the company to organize itself better with the help of this site.

# User experience

As an unauthorized user:
* Ability to access all the features and functions available to an authorized user, such as booking holidays, changing or canceling bookings, and viewing personal information.
* A user-friendly interface that makes it easy to navigate the site and find the desired information or features.
* Clear and concise instructions on how to use the site's features and functions, including any necessary steps for booking or modifying a holiday.
* A reliable and secure system for booking holidays, changing bookings, and canceling bookings.
* Prompt and effective customer support, including email or phone support, for any questions or issues that may arise during the booking process or during the holiday itself.

As an authorized user:
* Navigate the site easily and efficiently to view all the content you need.
* Create an account with a simple and easy process.
* Book a holiday for a specific time and date, choosing from available options and making payment through the site's secure payment gateway.
* Receive a confirmation email once the booking is complete, which includes all the relevant details about the holiday.
* Change the day of your holiday to a different date or time, if the website offers this feature. This may be subject to availability and may require additional payment if the new dates are more expensive than the original booking.
* Cancel your holiday, if the website offers this feature. The cancellation policy would typically be outlined in the terms and conditions.

As an administrator, I can:
* Viewing all available holidays and managing the booking system to ensure that the website's inventory is up-to-date and accurate.
* Reviewing and authorizing holiday requests from users, based on criteria such as availability, employee schedule, and other factors.
* Creating new user accounts if necessary, in order to provide access to the site's features and functions for new employees or customers.
* Managing user accounts and permissions, including setting access levels, resetting passwords, and monitoring activity on the site.
* Troubleshooting technical issues and providing support to users, including responding to inquiries and resolving any problems that arise.

## User stories
* Provide a registration option for users to create an account and access the booking features.
* Offer a clear option to opt out of sharing personal information for those who value their privacy.
* Be designed with easy navigation and user-friendly interface to make it easy for users to find information and take actions.
* Send a confirmation email after booking to ensure that users have a record of their reservation information.
* Allow users to cancel their reservation to provide flexibility in their travel plans.
* Display users' booking information clearly for easy reference.
* Have a secure login system to ensure the privacy and security of user information and booking details.
* Provide a prominent "book" button on the homepage to make it easy for users to initiate the booking process.
* Implement appropriate security measures to ensure that only authorized users can make updates to their reservations.
* By meeting these user requirements, a holiday booking site can offer a positive user experience that is easy to use, secure, and meets the needs of its customers.


## Admin stories
* User Account Approval:
As an administrator, you may receive a notification that a new user has registered on the site. You would then review the user's account details, such as name, email, and other information, to verify that they are a legitimate user. You would also check that their account has been created with the appropriate level of access and permissions, based on their role and responsibilities. Once you have confirmed that the user's account is valid and complete, you would approve their account and notify them that they can now log in to the site.

* Holiday Request Approval:
As an administrator, you would receive notifications when a user has requested a holiday booking. You would review the request details, such as the dates and location of the holiday, and check that the requested dates are available and that the user has sufficient vacation time or other permissions to take the holiday. You would also check that the user's account is in good standing, with no outstanding balances or other issues that would prevent them from booking a holiday. If the request is valid and meets all the necessary criteria, you would approve the holiday request and notify the user that their booking has been confirmed.

* Holiday Inventory Management:
As an administrator, you would have access to the site's inventory management system, which allows you to view all available holidays and make updates as necessary. You would check that all the holidays listed on the site are up-to-date and accurate, with correct pricing, availability, and other details. You would also monitor the inventory levels to ensure that there are enough holidays available to meet user demand, and make adjustments as necessary to avoid overbooking or underbooking. If there are any issues or discrepancies with the inventory, you would investigate and resolve them promptly, to ensure that users have a positive experience when using the site.

## Agile Methodology

Using Github projects to track user stories and organize tasks based on their level of importance is a key aspect of Agile methodology. By breaking down development into smaller, more manageable tasks, and prioritizing them based on user needs and feedback, developers can ensure that the app meets user expectations and delivers value in a timely and efficient manner. The use of Agile methodology can also help developers to adapt to changes in user requirements or market conditions, and to continuously improve the app over time based on user feedback and usage data.

* MUST HAVE
* SHOULD HAVE

By using AGILE methodology in this project I was able to deliver a site which had all required functionality and was able to give even more extra detail when going through the project.

I used GitHub projects board to create the user stories and keep track of my tasks. Here is the link to my board - [Project board](https://github.com/users/ocimar84/projects/2/views/1))

Here is also a screenshot overview

![Project](https://github.com/ocimar84/holidays/assets/79640465/e403d30a-45cc-434d-b9bd-42cfbe726837)


## CRUD functionality

Holiday Booking data with full CRUD Functionality:

**Create** - Users can create a new account and make a booking for their specific requirements. This involves creating a new record in the database that contains information about the user and their booking details, such as the date and time of the booking, the number of people in the group, and any special requests or requirements.

**Read** - Users can view their booking details in the "Manage Booking" section of the app. This involves querying the database for the relevant record(s) based on the user's login credentials or booking ID, and displaying the information in a user-friendly format.

**Update** - Users can update their booking by changing any of the details within the booking form. This involves updating the relevant record(s) in the database with the new information, and notifying the user that their changes have been saved.

**Delete** - Users can delete their booking from the database. This involves removing the relevant record(s) from the database and notifying the user that their booking has been cancelled.


## Wireframes

It's great that you're considering responsive design for smaller devices like tablets and mobile phones. Adapting the layout to stack the columns, providing a single-column navigation menu, and using a dropdown for smaller screens are all good practices for mobile responsiveness.

![image-2](https://github.com/ocimar84/holidays/assets/79640465/10a27f6a-8cdc-4cc1-97e8-8da64d8ea8e6)


![image-1](https://github.com/ocimar84/holidays/assets/79640465/179d51e4-81b5-4732-a585-f19746aedbb6)

![image](https://github.com/ocimar84/holidays/assets/79640465/b132d905-1cac-4ffb-bdfe-151b52c7fd4e)

![9f033a7b-b0c9-4aeb-bed8-921036e5b8b1](https://github.com/ocimar84/holidays/assets/79640465/0b419123-40db-4fa8-b114-0919d53f683a)

![image-4](https://github.com/ocimar84/holidays/assets/79640465/09c30b90-d7e6-4cd3-97c4-9c2b590ec7b2)

![image-3](https://github.com/ocimar84/holidays/assets/79640465/dee33e82-f441-41d7-9487-8581d03483c3)


# Features

## Header
Header based on login and sign Up and dark mode.
Login to enter your email and password.
Sign Up to register.

![image](https://github.com/ocimar84/holidays/assets/79640465/7c0d46de-bdcb-4755-8076-81d1389b4d1f)

## Hero image
A hero image, also known as a banner image or header image, refers to a large, prominent image displayed at the top of a webpage. It typically spans the full width of the page and is designed to grab the user's attention and convey the main message or theme of the website.

![image](https://github.com/ocimar84/holidays/assets/79640465/9d64a815-cb15-4e68-a8fb-3b7f674a795c)

## Login
A login tool, also known as a login form or login module, is a user interface component on a website or application that allows users to authenticate themselves and access restricted or personalized content. It typically consists of fields for entering a username or email and a password, along with a "Login" button. 

![image](https://github.com/ocimar84/holidays/assets/79640465/8ff7c958-199c-407e-a45a-eccc9cf4caf3)

## Add time off
Adding a time off booking feature to a holiday website can provide users with a convenient way to request and manage their vacation time. Here are some key considerations for implementing a time off booking feature on a holiday website:

![image](https://github.com/ocimar84/holidays/assets/79640465/c28c2200-6ccd-4fe5-8711-d02ee4bdc2f5)

## Add Department
It will add department right after the reason with the start date and end date.

![image](https://github.com/ocimar84/holidays/assets/79640465/5ec04b02-d9d3-4495-bbe1-bad43fe4f410)

## Reason
Determine the reason for requesting the holiday.

![image](https://github.com/ocimar84/holidays/assets/79640465/45d36a95-5355-4578-b0cc-1107ec306aa4)

## Start and end date
Determines the start and end date of the holiday, you cannot put the dates retroactively, before today.

![image](https://github.com/ocimar84/holidays/assets/79640465/37dd77a0-7fb3-4a13-8c35-f61db3ae8844)

## ADMIN
Django admin can manage 5 parameters:

![image](https://github.com/ocimar84/holidays/assets/79640465/d60829fc-0118-469b-87fd-6825909e7138)

## Accounts
Where the super user can delete registered emails

![image](https://github.com/ocimar84/holidays/assets/79640465/1e1789d2-c349-46ea-acfa-8cddede04cf2)

## User
Where it displays user name and email information.

![user](https://github.com/ocimar84/holidays/assets/79640465/f68bb808-2e81-49f6-aa97-eb154e2dd68a)


## Departmens
Here is where the super user can create the departments that are used in the company.

![image](https://github.com/ocimar84/holidays/assets/79640465/99d580d3-c2fc-4a52-b971-3c91d752c95a)

## Time offs
Where it shows the movement of requests created by users.

![image](https://github.com/ocimar84/holidays/assets/79640465/08829025-cd54-4c84-9a40-e5ea1f8233c3)

## Change time off
On this page there is all the information about the user's request:
* User - User name;
* Department - Which department the applicant works in;
* Holiday Start - Start date;
* Holiday end - End date;
* Hours - Amount of hours the user will spend on their holiday;
* Reason - What is the reason for requesting the holiday.

![image](https://github.com/ocimar84/holidays/assets/79640465/e19936d8-eabc-4fbd-83bf-6d514919ff1f)

## Status
To approve the basque holiday write something in the status the holiday will be approved.

![image](https://github.com/ocimar84/holidays/assets/79640465/43d7ff9a-7347-46b5-a617-b49bf4ea3177)

## Disapproval
To disapprove the holiday request, the super user just delete the request, so it will disappear from the history, For the future thinking about developing some other tool

![image](https://github.com/ocimar84/holidays/assets/79640465/398a7a73-e895-4e21-a436-3ef4fe50ee12)

![image](https://github.com/ocimar84/holidays/assets/79640465/bde72c00-0f12-4044-9bfb-475c59fbb62c)


If they do not have any booking they will be shown this screen. Here there is a button they can click to take them to the booking form to make one if they want to.

![no booking](static/readme/escaperoom-nobooking.jpg)

## Update booking
If the user wants to update their booking they will be taken back to the form. All of their previous information will already be here in place. The user can then update anything they need to. They will get the prompt if the slot is already taken again. Once they are happy with their new details they can submit and the changes will be shown in the manage bookings area.

![Update booking](static/readme/escaperoom-updatebook.jpg)

## Updated message
Once they submit the update. This message will appear to confirm their changes and they will also get a confirmation email with their new booking.

![Update message](static/readme/escaperoom-message.jpg)

## Cancel confirmation
If the user want to cancel their booking they can. Once they press the red cancel button they will be prompted by this alert. This is where they can confirm that they want to delete their booking and give double confirmation.

![Cancel confirmation](static/readme/escaperoom-cancel.jpg)

Once they confirm they will be shown this message and the changes will reflect in the manage bookings area.

![Cancel message](static/readme/escaperoom-cancel-message.jpg)

## Admin panel
The admin can access this panel by logging in with the superuser details. They will be able to get an overview of all of the information about the website. Including the information of the users, the rooms and the bookings.

![Admin panel](static/readme/escaperoom-admin.jpg)

Here the admins can see the bookings that have been placed. They will see all of the important information about the booking such as time, date, name of the booker, room name and email. The admin has an option to delete bookings from the system from this panel.

![Admin booking](static/readme/escaperoom-adminbooking.jpg)

Here the admin can alter any of the information about the rooms including the name, price, duration, capacity, description or image. They can also add new rooms if they wish to expand of even remove rooms.

![Admin rooms](static/readme/escaperoom-adminrooms.jpg)

## 404 Page
This is the page the users will be shown if they have an incorrect url for whatever reason. they will have a link they can press to take them back to the home page.

![404 page](static/readme/escaperoom-404.jpg)

## Responsive

To prove my responsiveness of my page, I have screenshots of what the main features look like on a mobile.

* Header
    * Here the navbar links form into a dropdown making it good UX.

![Header](static/readme/responsive-header.jpg)

* Most popular rooms
    * The imagery and description goes into a column order

![Most popular rooms](static/readme/responsive-popular.jpg)

* About us
    * The imagery and description goes into a column order

![About us](static/readme/responsive-about.jpg)

* Footer
    * It takes order in a column form

![Footer](static/readme/responsive-footer.jpg)

* Rooms
    * * The imagery, description and details goes into a column order

![Rooms](static/readme/responsive-room.jpg)

## Future Features

* Add newsletter to send discounts and room updates
* Have times solved for each room that is updated by each visit
* Automate Top times for each room
* Make emails easier to read
* Phone numbers can accept letters however it is low level as the email is more reliable. Update to allow only numbers

# Testing

## Lighthouse
The application has been tested with Chrome Dev Tools Lighthouse Testing which tests the application for:

* Performance
* Accessibility
* Best Practices
* SEO

### Home Page
![Home page](static/readme/Homepage-lighthouse.jpg)

### Room Page
![Room page](static/readme/room-lighthouse.jpg)

### Booking Page
![Booking](static/readme/book-lighthouse.jpg)

### Account Page
![Account](static/readme/account-lighthouse.jpg)

## HTML Validator

When running my HTML code through the [HTML Validation service](https://validator.w3.org/), I encountered a few minor errors that have now all be corrected.

This is the home page -

![HTML test ](https://github.com/ocimar84/holidays/assets/79640465/6e63ddfd-2e64-404b-8fc9-23f9cc4f50f3)

This is the main page where the user makes the request, there is an error being used in my HTML that is impossible to correct.

![image](https://github.com/ocimar84/holidays/assets/79640465/685bb775-741a-4d59-9e59-32c5d988cb97)



## CSS Validator
When running my CSS code through the [CSS Validation service](https://jigsaw.w3.org/css-validator/).

I used django-crispy-forms to improve all my layouts, I did my best to remove the error but every time I changed something it didn't work.

<img width="1408" alt="CSS test " src="https://github.com/ocimar84/holidays/assets/79640465/4f43e1a0-52eb-4ce3-8582-f8115d2bdf3b">


## Python Vaildator
When running my code through the [CI Python Linter Validation](https://pep8ci.herokuapp.com/) 

![Python test ](https://github.com/ocimar84/holidays/assets/79640465/9da1371c-f96e-42ba-ad96-90b54f8528fa)


## JSHint Validator
When running my JavaScript through [JSHint validator](https://jshint.com/) I had no bugs or erros.

* This is for the datepicker

![Javascript screenshot](static/readme/escaperoom-js.jpg)

* This is for the map. I have a couple undefined variable however I used this website to write the code. [Google maps code](https://developers.google.com/maps/documentation/javascript/adding-a-google-map)

![Javascript maps screenshot](static/readme/escaperoom-jsvalidator.jpg)

## Defects

Phone number allows the user to add letters. This is ok as its low level. The email is more reliable and will be used to contact the user first.

## Manual

Testing has been done manually with the google chrome dev tools to make sure the website is fully responsive. I have checked all pages at all key breakpoints to make sure the layout remains user friendly and nothing clashes.

I manually tested all buttons, forms and links to make sure the correct action took place. Here are tables to show the testing.

### Nav bar

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| logo   | Takes you to the home page     | PASS    | 
| Home link     |   Takes you to the home page     | PASS      |
| Rooms link   | Takes you to the rooms page     | PASS    | 
| Book link     |   Takes you to the booking page or sign in/sign up page     | PASS      |
| login/sign up link   | Takes you to the sign in page     | PASS    | 

### Footer

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| google maps   | allows you to see the location     | PASS    | 
| Facebook link     |   Takes you to the facebook page     | PASS      |
| Instagram link   | Takes you to the instagram page     | PASS    | 
| Twitter link     |   Takes you to the twitter page     | PASS      |

### Home page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| hero button   | Takes you to the booking page or sign in/sign up page     | PASS    | 
| popular room link     |   Takes you to the booking page or sign in/sign up page     | PASS      |

### Rooms page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| rooms book button   | Takes you to the booking page or sign in/sign up page     | PASS    |

### Create an account or Sign in to make a booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| sign in button   | Takes you to the  sign in   | PASS    | 
| sign up button     |   Takes you to the sign up page     | PASS      |

### Create an account form page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| sign in link   | redirects to login form   | PASS    | 
| All inputs   | make sure they're all valid   | PASS    | 
| sign up button     |   Creates your account and redirects to home page     | PASS      |

### Sign in form page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Sign up link   | redirects to create an account form   | PASS    | 
| All inputs   | make sure they're all valid   | PASS    | 
| sign in button     |   Sign in to your account and redirects to home page     | PASS      |

### Nav bar dropdown once logged in

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Dropdown   | brings a dropdown for two options   | PASS    | 
| booking link   | redirects to manage booking page   | PASS    | 
| logout link     |   takes you to confirm logout     | PASS      |

### Booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| All inputs   | make sure all inputs are valid before submitting   | PASS    | 
| datepicker   | datepicker should appear   | PASS    |
| timepicker   | timepicker should appear   | PASS    | 
| submit button   | submit form and a confirmation message appears on new page   | PASS    | 

### Manage booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Update button   | takes you to the booking form   | PASS    | 
| Cancel button   | bbrings up an alert to confirm cancel   | PASS    |

### Manage booking bo booking page

| What is being tested | Whats supposed to happen | Pass/Fail |
| --- | --- | --- |
| Book button   | takes you to the booking form   | PASS    | 



# Security Features

* Users cannot deduce the delete url and delete others bookings, they get a custom 500 error page if they do this when not logged in and a warning message if they are authenticated

* Users cannot deduce the update ulr and update others’ bookings, they get a custom 500 error page if they attempt to do this.

* Booking Update: Message Failure trying to book a time already booked
* Booking Update: Message failure if not logged in
* Booking Update: Message failure if they dont own booking
* Booking Cancel: Message Failure if not logged in
* Booking Cancel: Message failure if they dont own booking
* Place Booking: User not logged in
* Place Booking: Time & room already booked
* 500 Page: This can be activated for many reasons, but you are able to get there if you try to delete a booking that you don’t own, or if you try to access a booking that doesn’t exist

## User authentication
* Django's all auth was used for login and sign up functionality.
* Django's superuser is used to limit access to admin panel.

## Form Validation
* Extensive form validation is used on front end as well as backend.

## Database Security
* All secret keys connecting the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

# Bugs

## Solved

* I had some contrasting issues which I fixed by using devtools and using their recommended colours

![Contrast](static/readme/readme-contrast1.jpg)

* I had two main bugs in my project. These two bugs would allow hackers to delete and update someone else's bookings. I first had to check if the user that was trying to update or cancel the booking, owned that booking. I done that through this code - 

![Bug](static/readme/escaperoom-bug.jpg)

* Then I had to write an if statement to allow the authenticated user to continue their action. If not they get a custom 500 error page.

![500](static/readme/escaperoom-bug500.jpg)

* I had an issue when refresing on thank you booking page, it sends user another email. I had my email in the wrong section of my code and was a simple fix with a quick move. 

![Email code](static/readme/escaperoom-bugemail.jpg)

* I also had a bug with my messages. If a user were to sign in and sign out, then sign in to another account you would get a long list of messages appear on the my bookings page.

![Message bug](static/readme/escaperoom-bugmessage.jpg)

* To fix this I moved my for message loop out of my_booking.html into the base.html. This meant that the message would appear one at a time instead of a build up of messages once you opened the my_booking.html.

## Left to solve

There are no more bugs to solve as of 18/01/2023

# Credits

## Code 

* I used [this website](https://timepicker.co/?fbclid=IwAR2OiqEuDfKTM7438Gk72GFZjP0l4ze-A7aRiBSfE4FAJeH0Q8jIjk_-EcY) to make the datetime picker.
* I used [this website](https://opensource.com/article/22/12/django-send-emails-smtp) to send emails to the users.
* I used [this website](https://developers.google.com/maps/documentation/embed/get-api-key) to help me create the google maps API.
* I used [this website](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for-empty) to help me with for loops on my_booking.html

## Images

I used the following website to get my free stock images from -

* [Pexels](https://www.pexels.com/)
* [Unsplash](https://unsplash.com/)

## Technology used

* [Django](https://www.djangoproject.com/) - A model-view-template framework used to create Locksmith Booking
* [Bootstrap](https://getbootstrap.com/) - A CSS framework used for the front end development.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [JavaScript](https://www.javascript.com/) - Provides interactive elements of the website
* [Python](https://www.python.org/) - Provides the functionality of the website.
* [Gitpod](https://www.gitpod.io/) - Used to create and edit the website.
* [GitHub](https://github.com/) - Used to host the repository.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to test responsiveness and debug.
* [Am I Responsive](https://ui.dev/amiresponsive) - Used to generate mockup of my webpage.
* [Cloudinary](https://cloudinary.com/) - Used to host all static files and images.
* [Heroku](https://id.heroku.com/login) - Used to deploy the website.
* [ElephantSQL](https://www.elephantsql.com/) - Used to host my database
* [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate Python code.
* [HTML Validation](https://validator.w3.org/) - Used to validate HTML code.
* [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code.
* [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code.

# Deployment

## Local deployment
To test the app locally, the terminal within VScode was used. The steps to run this:

* Start from installing the chrome extension then clicking the green gitpod button in YOUR forked repository
* Include the pip3 install -r requirements.txt
* Creating env.py
    * EMAIL_HOST_PASSWORD=<YOUR_VALUE>
    * DEFAULT_FROM_EMAIL=<YOUR_VALUE>
    * EMAIL_USERNAME=<YOUR_VALUE>
    * SECRET_KEY=<YOUR_VALUE>
    * CLOUDINARY_URL=<YOUR_VALUE>
    * DEV=TRUE
* Migrate so the database starts up python3 manage.py migrate
* Create a super user so you can make the rooms in the admin and other things  python3 manage.py createsuperuser
* Start the server python3 manage.py runserver
* Use the website as usual.

A local database was used for most of the local deployment usage, since it was necessary for the automated tests to run. However, the switch to using the production database could be easily made, in case migrations needed to be performed or otherwise. Furthermore, in the development version, DEBUG was set to False, so error messages would show.

## Create a Fork

* On GitHub.com, navigate to the repository.
* In the top-right corner of the page, click Fork.
* Select an owner for the forked repository.
* By default, forks are named the same as their upstream repositories. You can change the name of the fork to distinguish it further.
* Optionally, add a description of your fork.
* Choose whether to copy only the default branch or all branches to the new fork. For many forking scenarios, such as contributing to open-source projects, you only need to copy the default branch. By default, only the default branch is copied.
* Click Create fork.

## Production delpoyment 
Escape room is deployed to Heroku, using an ElephantSQL Postgres database. To duplicate deployment to Heroku, follow these steps:

After you have forked the project for your own, continue these steps as follows -

* You will need a Cloudinary account to host user images and static files.
* Login to [Cloudinary](https://cloudinary.com/).
* Select the 'dashboard' option.
* Copy the value of the 'API Environment variable' from the part starting cloudinary:// to the end. You may need to select the eye icon to view the full environment variable.Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
* Log in to [Heroku](https://id.heroku.com/login).
* Select 'Create new app' from the 'New' menu at the top right.
* Enter a name for the app and select the appropriate region.
* Select 'Create app'.
* Select 'Settings' from the menu at the top.
* Login to [ElephantSQL](https://www.elephantsql.com/).
* Click 'Create new instance' on the dashboard.
* Name the 'plan' and select the 'Tiny Turtle (free)' plan.
* Select 'select region'.
* Choose the nearest data centre to your location.
* Click 'Review'.
* Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
* Copy the ElephantSQL database URL to your clipboard (this starts with postgres://).
* Return to the Heroku dashboard.
* Select the 'settings' tab.
* Locate the 'reveal config vars' link and select.
* Enter the following config var names and values:
* CLOUDINARY_URL: your cloudinary URL as obtained above
* DATABASE_URL: your ElephantSQL postgres database URL as obtained above
* PORT: 8000
* SECRET_KEY: your secret key
* Select the 'Deploy' tab at the top.
* Select 'GitHub' and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
* Find the 'Connect to GitHub' section and use the search box to locate your repo.
* Select 'Connect' when found.
* Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed site to be automatically redeployed every time you push changes to GitHub.
* Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
* Your site will shortly be deployed and you will be given a link to the deployed site when the process is complete.

# Acknowledgements

A huge thanks to my mentor Malia for going through my project and helping me with any issues I had to deal with.
