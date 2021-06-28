# Neat

![alt text](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/mockup.png "Neat Screenshot")

Neat is an e-commerce site, built using HTML, CSS, JavaScript, Python, and Django. The shop sells a range of planners and accessories. 

DISCLAIMER: This website is for educational purposes only and uses products and content from an existing brand. Please see the credits section for full information.

The live project can be viewed [here](https://fourth-milestone-project-neat.herokuapp.com/).

Test card details:
* **credit card:** 4242 4242 4242 4242
* **expiration date:** 04 / 24
* **CVC:** 111
* **ZIP:** 1111

## Table of Contents
1. [Project Summary](#project-summary)
1. [Ux](#ux)
    1. [User stories](#user-stories)
        1. [Site Owner Goals](#site-owner-goals)
        1. [Site User Goals](#site-user-goals)
    1. [Design](#design)
        1. [Wireframes](#wireframes)
        1. [Final Pages](#final-pages)
        1. [Colour Scheme](#colour-scheme)
        1. [Typography](#typography)
    1. [Architecture](#architecture)
        1. [Database](#database)
        1. [Structure](#structure)      
1. [Technologies](#technologies-used)
   1. [Languages](#languages)
   1. [Frameworks, Libraries & Programs](#frameworks-libraries-programs)
1. [Testing](#testing)
    1. [Site Goals](#site-goals)
   1. [User stories](#user-stories)
   1. [Additional Functionality](#Additional-Functionality)
   1. [Compatibility](#compatibility)
   1. [Validation](#validation)
1. [Deployment](#deployment)
1. [Credits](#credits)

## Project Summary

This project is my fourth and final milestone project (Full Stack Frameworks With Django) for the Code Institute Diploma in Software Development. 

The purpose of the project is to build a full-stack site based around business logic used to control a centrally-owned dataset
, setting up an authentication mechanism and providing paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

I have created an e-commerce site where customers can purchase items and user engagement is encouraged through blog posts and
the ability to leave reviews and comments.

The site has a responsive design so that it can be viewed easily on mobile and desktop.

## UX

### User Stories

#### Site Owner Goals
As a site owner I want to be able to:

1. Create a visually appealing site with a strong brand identity.
1. Add products on the website so I can add new items to my stores
1. Edit existing products in my store so I can change product prices, descriptions, iamges and other product information.
1. Delete products on the website so I can remove items from my store
1. Create new blog posts so that I can engage with customers and add new content to the site
1. Edit existing blog posts in case I've made a mistake and what to make a change to it
1. Delete blog posts if I no longer what them on the site
1. Have links that direct users to our social sites for further engagement

#### Site User Goals
As a site user I want to be able to:

*Viewing and Navigation*

1. Be able to easily navigate the site so that I can quickly find what I am looking for
1. View a list of all products available so that I can purchase them
1. View specific categories of products so that I can filter for products that I'm interested in.
1. View individual product details so that I can decide if I want to make a purchase
1. Get feedback on the site when actions are performed so that I know if they have been successful or not

*Sorting and Searching*

1. Search the site so that I can quickly and easily find what I'm looking for.
1. Filter products that I am viewing so that I can identify products that fit my budget or that have been recommended

*Registration and User Accounts*

1. Easily sign up, log in and log out of an account so that I have a personal account and be able to view my profile
1. Recover my password if I forget it so that I can regain access to my account
1. Receive an email confirmation after registering so I can verify my account registration was successful
1. Have a personalised user profile so that I can view my order history and save default payment information

*Purchasing and Checkout*

1. Select the quantity of a product I want to buy
1. View the items in my cart so that I can confirm the items that I am purchasing along with the total cost
1. Adjust the quantity of products in my cart in case i've make a mistake when adding them
1. Remove an item from my cart if I no longer what to purchase it
1. Easily enter my payment information so that I can check out quickly
1. Get an order confirmation after checkout to verify I haven't made any errors

*Reviews*

1. See previous reviews so that I can make an informed purchase
1. Leave a review on a product so that I can inform other shoppers about whether it was a good purchase or not
1. Edit my review in case I've made a mistake and what to make a change to it
1. Delete my review if I no longer want it on the site

*Blog*

1. Leave comments on blog posts so that I engage with the store owners and other customers

### Design

- #### Wireframes

  - [Home](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/indexpagewireframe.png)
  - [Products](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/browsepagewireframe.png)
  - [Product Detail](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagewireframe.png)
  - [Cart](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagewireframe.png)
  - [Checkout](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagewireframe.png)
  - [Profile](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagewireframe.png)
  - [Blog](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagewireframe.png)
  - [About](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagewireframe.png)

- #### Final Pages 

  - [Home](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/indexpagescreenshot.png)

  - [Products](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/browsepagescreenshot.png) -
Shows list of products

  - [Product Detail](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/resultspagescreenshot.png) -
Shows details about an individual product

  - [Cart](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/stockpagescreenshot.png) -
This is a page that shows users all of the products in their cart

  - [Checkout](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/loginpagescreenshot.png) -
This is a checkout page where users input their payment information

  - [Profile](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/signuppagescreenshot.png) -
Page where users can see their default information and order history

  - [Blog](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/feedpagescreenshot.png) -
Show blog posts

  - [Amount](https://github.com/yipmunallen/Third-Milestone-Project/blob/master/static/images/readme/feedpagescreenshot.png) -
Shows information about the site

-  #### Colour Scheme
    -   The colour scheme for this site rendered on [__Coolor__](https://coolors.co/) and can be seen below:

    ![alt text](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/colour-scheme.png "Colour Scheme")


 -   #### Typography
      -   The font used for headings throughout the site is "Bodoni Moda". "Arimo" is used for the remainder of text. Sans-serif has been used as the fallback font throughout.

## Architecture

### Database

The database used for the deployed project is [__PostgreSQL__](https://www.postgresql.org/), but during development used [__SQLite__](https://www.sqlite.org/index.html) 

### Structure

This project consists of the following 7 Django apps:

- **Home** - Displays the store home page

- **Products** - Handles product display and individual product views
    - Category Model - Stores the product categories

    	```
        name = models.CharField(max_length=100)
        friendly_name = models.CharField(max_length=100, null=True, blank=True)
        ```
    - Product Model - Stores individual product information

    	```
        category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
        sku = models.CharField(max_length=150, null=True, blank=True)
        name = models.CharField(max_length=254)
        description = models.TextField()
        price = models.DecimalField(max_digits=6, decimal_places=2)
        recommend_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0, null=True, blank=True)
        image = models.ImageField(default='')
        image_2 = models.ImageField(default='')
        ```        

- **Cart** - Handles CRUD operations for items in cart

- **Checkout** - Display checkout page and handles payments
    - Order Model - Stores order information

    	```
        order_number = models.CharField(max_length=32, null=False, editable=False)
        user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name='orders')    
        full_name = models.CharField(max_length=50, null=False, blank=False)
        email = models.EmailField(max_length=254, null=False, blank=False)
        phone_number = models.CharField(max_length=20, null=False, blank=False)
        country = CountryField(blank_label='Country *', null=False, blank=False)
        postcode = models.CharField(max_length=20, null=True, blank=True)
        town_or_city = models.CharField(max_length=40, null=False, blank=False)
        street_address1 = models.CharField(max_length=80, null=False, blank=False)
        street_address2 = models.CharField(max_length=80, null=True, blank=True)
        county = models.CharField(max_length=80, null=True, blank=True)
        date = models.DateTimeField(auto_now_add=True)
        delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
        order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
        grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
        original_cart = models.TextField(null=False, blank=False, default='')
        stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
        ```
    - Order Line Model - Stores individual items within an order

    	```
        order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
        product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
        quantity = models.IntegerField(null=False, blank=False, default=0)
        lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
        ```    
- **Profiles** - Displays user profile and stores user profile information and order history
    - UserProfile Model - Stores user profile information

    	```
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        default_full_name = models.CharField(max_length=50, null=True, blank=True)
        default_phone_number = models.CharField(max_length=20, null=True, blank=True)
        default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
        default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
        default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
        default_county = models.CharField(max_length=80, null=True, blank=True)
        default_postcode = models.CharField(max_length=20, null=True, blank=True)
        default_country = CountryField(blank_label='Country', null=True, blank=True)
        ```
- **Reviews** - Handles CRUD operations for product reviews
    - Review Model - Stores the review for the product

    	```
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        title = models.CharField(max_length=50)
        description = models.TextField()
        would_recommend = models.BooleanField(default=False, null=False, blank=False)
        date_created = models.DateTimeField(auto_now_add=True)
        ```

- **Blog** - Displays blog posts and handles CRUD operations for posts and comments form
    - Post Model - Stores blog post

    	```
        title = models.CharField(max_length=100, unique=True)
        slug = models.SlugField(max_length=200, unique=True)
        author = models.CharField(max_length=60)
        summary = models.TextField(max_length=300)
        content = models.TextField()
        image = models.ImageField(default='')
        created_on = models.DateTimeField(auto_now_add=True)
        status = models.IntegerField(choices=STATUS, default=0)
        ```

    - Comment Model - Stores comment relating to blog post

    	```
        post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        comment = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)
        ```        

## Technologies Used

### Languages

- [__HTML5__](https://en.wikipedia.org/wiki/HTML5) - Used to structure and present the website.
- [__CSS__](https://en.wikipedia.org/wiki/CSS) - Used to style the website.
- [__JavaScript__](https://en.wikipedia.org/wiki/JavaScript) - Used to collapse navbars and dynamically show the edit comment forms.
- [__Python__](https://en.wikipedia.org/wiki/Python_(programming_language)) - Used for the backend development.

### Frameworks, Libraries & Programs

- [__Django__](https://www.djangoproject.com/) - Framework used to build the site

- [__Heroku__](https://heroku.com/) - Used to deploy the site.

- [__Stripe__](https://stripe.com/en-gb) - Used to handle payments

- [__PostgreSQL__](https://www.postgresql.org/) - Database used for deployed site

- [__Mockflow__](https://www.mockflow.com/) - Used to create the wireframes during the planning stage of the project.

- [__Bootstrap Framework__](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Used for the site design, forms, modals, toasts and dropdowns.

- [__JQuery__](https://jquery.com/) - Used to manipulate HTML and CSS properties.

- [__Google Fonts__](https://fonts.google.com/) - Used to import the "Bodoni Moda" and "Arimo" fonts used throughout the site.

- [__Font Awesome__](https://fontawesome.com/) - Used to import the icons used for the watchlists.

- [__Favicon__](https://favicon.io/) - Used to created the favicon used on the site. 

- [__Git__](https://git-scm.com/) - Used for version control.

- [__Github__](https://github.com/) - Used to store all website code once pushed from Git.

- [__Google Chrome Developer Tools__](https://developers.google.com/web/tools/chrome-devtools) - Used to inspect page elements, test different CSS styles and debug site issues using the console.

## Testing

<!-- In order for the website to pass testing, the following have been tested both whilst in development and on the live website:

1. Functionality in line with user stories
1. Additional functionality required for website
1. Compatibility with multiple devices and browsers

In addition: 

1. The HTML, CSS, Javascript and Python files have been validated using respective online validators.

### User Stories

1. Easily browse available stocks
    1. The browse page is accessible from the sticky navbar at all times to both non logged in and logged in users
    2. On initial entry to the page, all stocks in the stocks collection are successfully shown
1. Easily search for stocks that I am interested in
    1. A functioning search bar has been added on the watchlist and browse pages that allows users to refine their search. If there are no search results, then "no results found" will be displayed
    2. There is also a dropdown filter under the search bar on the browse page that allows users to filter stocks shown, as well as a "Show All" button which removes the filter
1. Be able to comment on stocks
    1. A comment form is available to logged in users on the stocks page
    2. Upon submittion of the form, a new document is added to the comments collection, with it's id added to the corresponding stock's comments array
    3. The comment form is unavailable to non-logged in users, with a prompt to sign up / login
1. Be able to edit comments I have submitted
    1. The edit comment button is shown if the logged in user is the one that submitted the comment
    2. Once the edit button is clicked, a form opens up allowing the user to either edit their comment, or cancel the form
    3. Once the comment is submitted, the comment in the comments collection is updated
1. Be able to delete comments I have submitted
    1. The delete comment button is shown if the logged in user is the one that submitted the comment
    2. Once the delete button is pressed, the comment is removed from the comments collection as well as it's id removed from the stock's comments array
1. Build my own watchlist so that I can have easy access to my favourite stocks
    1. Watchlist functionality is available to logged in users only, who can access their watchlist from the sticky navbar at all times
    2. Users can see easily add stocks to their watchlist from the browse and stock pages. 
1. Be able to remove stocks from my watchlist
    1. Users can remove stocks from their watchlist on the watchlist, browse and stock pages. 
1. Be able to see comments across a range stocks
    1. A feed page is available to logged in users and can be accessed from the sticky navbar at all times
    2. The page displays the most recent 100 comments across all stocks.
    3. There is a toggle button that allows users to only see comments on their watched stocks. 

### Additional Testing

  - __Defensive Programming__- Tests have been conducted to ensure users cannot perform actions or access pages they shouldn't be able to:
    1. If a logged in user:
        1. Tries to access the sign up page, they will be redirected to their feed and a message "You already have an account" will be shown. 
        2. Tries to access the log in page, they will be redirected to their feed and a message "You are already logged in" will be shown. 
    2. If a non logged in user:
        1. Tries to access a feed, they will be redirected to the index page. 
        2. Tries to add to a watchlist, they will be prompted to log in or sign up
    3. A comment cannot be deleted unless the user is logged in and the comment was written by them. If this is attempted using the url, the stock page will reload and no comment is deleted.

  - __Flash Messages__-  Flash messages are used to confirm actions and convey messages to users. There are successfully shown:
    1. If a login attempt is unsuccessfull , "Incorrect username and/or password" shows
    2. If a user tried to sign up with an existing username, "username already exists" shows.
    3. If a new user signs up, they will be directed to the feed page where "Welcome to Ticker, Username. This feed shows recent comments on stocks" shows.  
    4. If a user logs in, they will be directed to the feed page where "Welcome, Username" shows.
    5. If a user creates a new comment, "Comment successfully added" shows.
    5. If a user edits a comment, "Comment successfully edited" shows.
    5. If a user deletes a comment, "Comment successfully deleted" shows.

  - __Form Validation__- Form validation has been tested to ensure that:
    1. If a user attempts to sign up with a username or password that does not conform to the requirements stated on the form, "please match requested format" is shown and the form is not sent.
    2. If a user attempts to sign up without filling in BOTH the username and password form, they will be prompted to fill out the missing field(s)
    3. If a user attempts to submit a blank comment on a stocks page, they will be prompted to fill out the missing field

  - __404 Error__- This has been tested to ensure that the custom 404 error page will show if the error occurs, with a link that redirects to the home page.

  - __405 Error__- This has been tested to ensure that the custom 405 error page will show if the error occurs, with a link that redirects to the home page. -->

### Compatibility

  - __Devices__ - The website has been viewed and tested on a range of devices including Desktop, Laptop, Iphone 6/7/8/X, Ipad and Samsung Galaxy Tab, retaining structure and functionality.

  - __Browsers__ - The website has been viewed and tested on a range of browsers including Google Chrome, Internet Explorer and Firefox, retaining structure and functionality.

### Validation

  - __CSS__ - Validated using [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) with no errors found.

  - __HTML__ - Validated using [W3C](https://validator.w3.org/#validate_by_input). Other than errors related to the user of the Jinja templating language, no errors found.

  - __Javascript__ - Validated using [JSHint Validator](https://jshint.com/) with no errors found.

  - __Python__ - Validated using [PEP 8](https://jshint.com/) with no errors found.
  

## Deployment

This project is hosted by Github and deployed using heroku.

### Clone this project

In order to clone this project:

1. Log in to Github and find the Github Repository.
2. Click the "code" button and copy the HTTPS link
3. Open Git terminal and type ```git clone``` followed by the link and hit "enter".

### Setting up a database

In order to set up a database in MongoDB:

1. Signup or login to MongoDB
2. Create a cluster as well as a database.
3. Create three collections within your database following this [data structure](#data-structure)

### Deploy to Heroku

1. Add an env.py file to your workspace containing the following variables:
    1. ``` os.environ["PORT"] = "5000"```
    2. ``` os.environ["IP"] = "0.0.0.0"```
    3. ``` os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"``` 
    4. ```os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"``` 
    5. ```os.environ["MONGO_DBNAME"]= "DATABASE_NAME" ```
2. Create an application:
    1. Log in or sign up to [__Heroku__](https://heroku.com/)
    2. Click on the "New" button and "Create new app"
3. Connect to Github
    1. Click on the "Deploy" tab and "Connect to GitHub"
    2. Enter the name of your Github repository and click "Connect"
    3. Go to the "Settings" tab and create config vars based on variables created in env.py previously
    4. Once all your Github files are pushed, navigate back to the "Deploy" tab, select "Enable automatic deploys" and deploy branch to Heroku

## Credits

### Content

- [STIL](https://stilclassics.com/) - All of the products, product details and blog posts have been taken from STIL
- [Unsplash](https://unsplash.com/@stilclassics) - Some images used on the site are from Unsplash
    1. [STIL](https://unsplash.com/@stilclassics) - Product images
    1. [Jess Bailey](https://unsplash.com/photos/q10VITrVYUM) - Hero image used on home page
    1. [Joanna Kosinska](https://unsplash.com/photos/RE-8WswW95o) - Background image used on AllAuth pages
    1. [Brooke Cagle](https://unsplash.com/photos/g1Kr4Ozfoac) - Image at top of About page
- [Techsini](https://techsini.com/multi-mockup/index.php) - Used to create the website mockup at the top of the ReadMe file

### Code

- [Code Institute](https://www.codeinstitute.net/) - Code learnt during the Full Stack Web Developer course (specifically the Boutique-Ado project) has been implemented in this project.

- [MDBootstrap](https://mdbootstrap.com/snippets/jquery/ascensus/135500) - Used for product detail pages image carousel

- [Stack Overflow](https://stackoverflow.com/questions/7643308/how-to-automatically-close-alerts-using-twitter-bootstrap) - Used for automatically closing flash messages.

- [Sirv](https://sirv.com/help/articles/hover-change-image/) - Change image on hover on product detail page

### Acknowledgements
- Spencer Barriball - Mentor at Code Institute

