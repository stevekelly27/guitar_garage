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


### Add Post:
The add post feature will only be available if the user is registered to the site and logged in.
On the add post page the user is asked for a title, to choose a category, to upload a featured image, an excerpt and the main content of the post using the included SummernoteWidget.


![8800CE23-966F-4D64-B6DF-203A3FB75D1F](https://user-images.githubusercontent.com/93382818/209195197-22b46f59-ecd6-46b9-8c10-213059f76b3f.jpeg)



### Post Detail:

Once the user has clicked on a post, the user is redirected to the post detail page. This page concists of the full contents of the post that has been selected. If the user is staff/admin you are able to edit or delete your post from here.


![651703F0-56E2-4CAD-B46B-3AE304817862](https://user-images.githubusercontent.com/93382818/209020091-2181ea40-1f75-4cc2-a9f9-4bb67c326493.jpeg)


### Edit Post:
The edit post page is very similar to the add post page but it is prepopulated with the existing post, the user is able to edit any text/category and once clicked submit is redirected to the home page.


![A1F7871E-3FD0-4CCB-ABBD-58117ABAE091](https://user-images.githubusercontent.com/93382818/209196034-c16fd8c1-c679-416b-b649-b041c8769876.jpeg)


### Delete Post:
If the user clicks the delete button on the post detail page they are redirected to the delete post page where it is asking you to confirm that you do want to delete the post. This is a saftey measure so a post is not deleted by accident. If the delete post button is clicked the post will be deleted and the user will be redirected to the home page.


![14ACC1D2-77F3-44F2-AAC4-1D47DB8F671C](https://user-images.githubusercontent.com/93382818/209196717-d4bd462c-b4c8-42ed-b2f2-3dee132df34b.jpeg)



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


### Django Admin Page:

To manage the blog content of the site, a superuser account was created. This allows a superuser to administer the site. The admin page can be easily be accessed by logging in to the /admin URL with the superuser account. From the admin the superuser will have the ability to delete any post, comment or user. This functionalityis necessary to maintain the blog and remove unwanted content.


![DDE2E734-73D2-446C-ABE0-231BE33C9074](https://user-images.githubusercontent.com/93382818/209199616-b6424974-cf6a-4060-ba3c-0f1a502eab58.jpeg)


## Design

### Wireframes

As part of the palnning phase wireframes were created using Balsmaiq.
The wireframes were used to get a basic idea on how the site might look when finished.

Wireframes were created for the following features:

Home Page:

![A17A2517-8CF5-4227-AFF7-CAE268F3A61D_1_105_c](https://user-images.githubusercontent.com/93382818/209250275-fa7ad577-a6a3-4b5b-8154-3b55400b058c.jpeg)

Post Detail:

![85855846-997A-48E4-960A-4EF885CEB1FD](https://user-images.githubusercontent.com/93382818/209250503-8a3f1a11-b743-4b0b-bf84-d9bbc5a35c22.jpeg)

![C6C9306C-A0CB-44C3-89C1-27DC01CB3559_1_105_c](https://user-images.githubusercontent.com/93382818/209250526-3ccfa834-c15e-4e2f-b4e7-5694707a6a7e.jpeg)

Add Post:

![7752BA2C-9245-45A8-BA7A-767845E3AC2C](https://user-images.githubusercontent.com/93382818/209251429-4bf28473-0b91-4503-83f0-0c8470000caa.jpeg)



## Testing:

### Browser Testing:

I have tested that this application worksusing a Macbook Pro, with macOS Monteray version 12.0.1 installed, using the following browsers:

- Safari
- Google Chrome
- Firefox browser

I have tested that the application works on the following iOS devices:

- iPhone 13 Pro with iOS 15.5 installed
- iPad pro with iOS 15.6 installed

### Validator Testing:

#### W3C Markup Validator:

![2238ECE4-B51F-4191-A70D-BF9204316043](https://user-images.githubusercontent.com/93382818/209262216-ec21ea1b-e236-4b0a-b984-3c274765ecba.jpeg)

#### W3C CSS Validator:

![74501764-1669-47BA-B478-73C4A8D71B13_4_5005_c](https://user-images.githubusercontent.com/93382818/209262620-36dc8383-1821-4685-a4c1-e73223ce1a3e.jpeg)


#### PEP8 Online:





## Deployment
The application was deployed to Heroku. The steps to deploy are as follows:
#### Create Heroku App
- Login to Heroku dashboard to get an overview of installed apps.
- Click on New then Create new app.
- Choose a name for your application (must be unique) and enter your location.
- Click on Create app.
- After creating your new application, navigate and click on the Resources tab.
- In the Add-ons search bar enter Heroku Postgres then Select Heroku Postgres.
- A pop-up window till appear, choose Plan name Hobby Dev - Free.
- Click on Submit order form.
- Navigate to the Settings tab then click on Reveal Config Vars.
- Copy the DATABASE_URL url value to the clipboard.
- In GitPod, create a new env.py file on top level directory.
- In the env.py file:
  - Set environment variables: os.environ[”DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link”
  - Add in secret key: os.environ[”SECRET_KEY"] = "Make up your own randomSecretKey”
- In Heroku Navigate to the Settings tab then click on Reveal Config Vars.
- Add SECRET_KEY to Config Vars with the randomSecretKey value previously chosen.
- In the settings.py file:
  - Delete the insecure secret key and replace it with: SECRET_KEY = os.environ.get(’SECRET_KEY')
  - Update to use the DATABASE_URL: dj_database_url.parse(os.environ.get(”DATABASE_URL"))
- Save all files and Make Migrations: python3 manage.py migrate
- Login to Cloudinary and go to the Cloudinary Dashboard.
- Copy your CLOUDINARY_URL API Environment Variable to the clipboard.
- In the env.py file:
  - Add Cloudinary URL: os.environ["CLOUDINARY_URL"] = ”cloudinary://paste in API Environment Variable”
- In Heroku, go to the Settings tab then click on Reveal Config Vars.
- Add ’CLOUDINARY_URL’ to Config Vars with the in API Environment Variable value.
- Add ’DISABLE_COLLECTSTATIC’ 1 to Heroku Config Vars (temporary, must be removed before final deployment).
- In the settings.py file:
  - Add Cloudinary Libraries to installed apps (note: order is important) ’cloudinary_storage',  ’django.contrib.staticfiles', ’cloudinary',
  - Add the following code below STATIC_URL = ’/static/' to use Cloudinary to store media and static files:
    - STATICFILES_STORAGE = ’cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    - STATICFILES_DIRS = [os.path.join(BASE_DIR, ’static')]
    - STATIC_ROOT = os.path.join(BASE_DIR, ’staticfiles')
    - MEDIA_URL = '/media/'
    - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
  - Link file to the templates directory in Heroku: TEMPLATES_DIR = os.path.join(BASE_DIR, ’templates')
  - Change the templates directory to: TEMPLATES_DIR: 'DIRS': [TEMPLATES_DIR],
  - Add Heroku Hostname to ALLOWED_HOSTS: ALLOWED_HOSTS = [”Your_Project_name.herokuapp.com”, ”localhost”]
- Create 3 new folders on top level directory: media, static, templates
- Create a Procfile on the top level directory
- In the Procfile file:
  - Add the following code with your project name: web: gunicorn PROJ_NAME.wsgi
- In the terminal: Add, Commit and Push.
#### Deploy
- In Heroku go to the Deploy tab then click on Deploy Branch.
- When the build process is finished click on Open App to visit the live site.


## Frameworks/ Libraries/ Programs Used:

- Django: Main python framework used in the development of this project
- Django-allauth: authentication library used to create the user accounts
- PostgreSQL was used as the database for this project.
- Heroku - was used as the cloud based platform to deploy the site.
- Summernote: A editor to allow users to edit their posts
- Crispy Forms used to manage Django Forms
- Cloudinary: the image hosting service used to upload images
- Bootstrap 4.6: CSS Framework for developing responsiveness and styling
- W3C - Used for HTML & CSS Validation.
- PEP8 Online - used to validate all the Python code
- Jshint - used to validate javascript
- Responsinator - Used to verify responsiveness of website on different devices.
- Balsamiq - Used to generate Wireframe images.
- Chrome Dev Tools - Used for overall development and tweaking, including testing responsiveness and performance.
- Font Awesome - Used for icons in the footer.
- GitHub - Used for version control and agile tool.
- Google Fonts - Used to import and alter fonts on the page.
- Grammerly - used to proof read the README.md
