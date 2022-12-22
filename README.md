# The Guitar Garage

The Guitar Garage is a Django blog application built for people who are interested in guitars, pedals, amps and gear in general.
The purpose of this site is to allow users to add a post of gear you are in the market for or gear you have just bought to get feedback from the guitar community at large. Users can also comment on a post if they are logged in to give their input on the post at hand. 

![012147B1-B82D-4253-AA14-9E958E2B85E9](https://user-images.githubusercontent.com/93382818/208962646-cdb9c6a7-ce3e-4df0-8772-5f11b43f79ee.jpeg)

# User Expierence (UX)

## Project Goals:

The primary goal for this project is to create a guitar discussion blog that enables full CRUD functionality.
The user should be able to login, add a post, edit a post, delete a post and be able to click into individual posts and get the full post content and the ability to add a comment.


# Features

## Existing Features

### Navigation Bar:

The navbar is present on all pages of the site. it is built using bootstraps existing built in classes.
On the left side of the navbar there is the Guitar Garage logo and when clicked redirects the user back to the home page.
On the right side of the navbar there are three links when logged in and four links when logged out. Home, About, Register and Login are the links present when the user is logged out. 


![6497CA57-7240-4F68-A88B-8B167F5BDC1C_4_5005_c](https://user-images.githubusercontent.com/93382818/208984418-89002982-7345-45f1-8b48-dc504bd6b6fa.jpeg)


Home, About and Logout are the links present when the user is logged in.


![CB5E4628-8866-4989-87FE-A9B61A128F21_4_5005_c](https://user-images.githubusercontent.com/93382818/208984462-00caa25d-07c4-445b-8f56-d01d43d8bcc5.jpeg)


### Footer:

The footer consists of the links to the social media accounts related to the Guitar Garage.
The icons were sourced from Font Awsome.


![6167D7E7-27AA-4644-8E85-2C5F8E9A8FFE_4_5005_c](https://user-images.githubusercontent.com/93382818/209021672-b25097e7-1f26-4d88-9b68-581e5ef86760.jpeg)


### Home Page:

On the Home Page if the user is logged in there will be a button at the top of the page under the navbar to Add A Post. Underneath the Add A Post there is a categories button with a drop down list to help the user navigate between Guitars, Pedals and Amps.


![FD5230BA-6355-41EF-AB21-DD270168F0F3_4_5005_c](https://user-images.githubusercontent.com/93382818/208986488-ec223d32-47ba-4b85-94e0-574c025a5df1.jpeg)


![485DDF95-62DE-404B-9887-115CB2B4ED82](https://user-images.githubusercontent.com/93382818/208986897-2d1c462e-10cc-4695-b085-a3141d897dff.jpeg)


below these two buttons are the list of posts showing an excerpt, a featued image, the author of the post and the time the post was created.


![BC5570E4-AC7B-40B1-B20E-FD56C8F8F0BB](https://user-images.githubusercontent.com/93382818/208986548-6ffad5a8-bc75-4a25-85da-b5cb7a2e13d8.jpeg)


### Post Detail:

Once the user has clicked on a post, the user is redirected to the post detail page. This page concists of the full contents of the post that has been selected. If the user is staff/admin you are able to edit or delete your post from here.


![651703F0-56E2-4CAD-B46B-3AE304817862](https://user-images.githubusercontent.com/93382818/209020091-2181ea40-1f75-4cc2-a9f9-4bb67c326493.jpeg)


Under the post content and the edit and delete buttons there is the comments section. The comments section has the comment box at the bottom of the page and comments are above the area to enter your comment. The comment card consists of the comment entery, the author of the comment and the date and time of publishing. The comments are filtered so a new comment is on the bottom of the thread similar to reddit style.


![A9DD2E3B-1EEA-47FF-8BC7-5BAA17F87F3E](https://user-images.githubusercontent.com/93382818/209020933-4d164bc3-98b5-4407-8cc2-53702a962a82.jpeg)

### About Page:

The about page just has a brief description of what the page is about and inviting everyone to register to the site and to follow the social media pages.


![3AB1094C-17B9-4A35-ADF2-8FC0E0FB4730](https://user-images.githubusercontent.com/93382818/209024584-c7528356-634d-4228-a34f-244367f58b7c.jpeg)

### Register Page:

To interact with the site, the user is required to register and login. Registered users are then given access to add, edit and delete a post and are also given access to comment on a post.
To register to the Guitar Garage you must make a username, give your email, enter a password and re-enter your password incase of typo.

![0A4FFB9F-408F-42A9-9AAE-C4072F3C1D1F](https://user-images.githubusercontent.com/93382818/209025999-9fe94770-a7c3-4441-b890-8d8dd0e48e96.jpeg)

When all fields are filled in and the user clicks on sign-up a new account is automatically created and the user is redirected to the home page.

### Login Page:

Again you must register and log in to take advantage of the CRUD functionality.
The user is only required to enter a username and password to login to the site and there is a remember me checkbox to save login details.


![E0ADACF9-AF15-4BC0-AB09-086871C93553](https://user-images.githubusercontent.com/93382818/209026587-e518a037-973d-4f47-a533-d0518ef60f86.jpeg)

When the user enters the correct username and password and clicks on login, they are logged into their account and redirected to the home page.

### Logout Page:

If the user clicks the logout button on the right side of the navbar, they are taken to a page to confirm that theuy do want to sign out of their account. 


![96E415DD-3B81-4361-9C34-F87977055B60](https://user-images.githubusercontent.com/93382818/209027007-db7bf5f9-a0b3-4281-9ed7-8946c0eac951.jpeg)

Once the user has clicked the Sign Out button they are signed out of their account and redirected to the home page and a message will appear on the screen saying that you have been sucsessfully logged out.



