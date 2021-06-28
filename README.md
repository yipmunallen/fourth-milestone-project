# Neat

![alt text](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/mockup.png "Neat Screenshot")

Neat is an e-commerce site, built using HTML, CSS, JavaScript, Python, and Django. The shop sells a range of planners and accessories. 

DISCLAIMER: This website is for educational purposes only and uses products and content from an existing brand. Please see the credits section for full information.

The live project can be viewed [here](https://fourth-milestone-project-neat.herokuapp.com/).

Test card details:
* **Card Number:** 4242 4242 4242 4242
* **Expiration Date:** 04 / 24
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
1. [Features](#features)
    1. [Common features](#common-features)
    1. [Page Features](#page-features)    
1. [Architecture](#architecture)
    1. [Database](#database)
    1. [Structure](#structure)    
1. [Technologies](#technologies-used)
   1. [Languages](#languages)
   1. [Frameworks, Libraries & Programs](#frameworks-libraries-programs)
1. [Testing](#testing)
   1. [Site Goals Testing](#site-goals-testing)
   1. [User Stories Testing](#user-stories-testing)
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

1. Create a visually appealing site with a strong brand identity
1. Add products on the website so I can add new items to my stores
1. Edit existing products in my store so I can change product prices, descriptions, iamges and other product information.
1. Delete products on the website so I can remove items from my store
1. Create new blog posts so that I can engage with customers and add new content to the site
1. Be able to create draft blog posts which users can't see so that I can make updates and publish posts at chosen times
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

1. See previous comments on blog posts so that I can see other user's thoughts
1. Leave comments on blog posts so that I engage with the store owners and other customers

### Design

- #### Wireframes

  - [Home](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/homewireframe.png)
  - [About](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/aboutwireframe.png)
  - [Products](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/productswireframe.png)
  - [Product Detail](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/productdetailwireframe.png)
  - [Cart](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/cartwireframe.png)
  - [Checkout](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/checkoutwireframe.png)
  - [Profile](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/profilewireframe.png)
  - [Product Management](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/productmanagementwireframe.png)
  - [Blog](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/blogwireframe.png)
  - [Blog Post](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/blogpostwireframe.png)
  - [Login / Register / Signout](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/authorisationwireframe.png)

- #### Final Pages 

  - [Home](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/homescreenshot.png)

  - [About](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/aboutscreenshot.png)

  - [Products](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/productsscreenshot.png) -
Shows list of products

  - [Product Detail](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/productdetailscreenshot.png) -
Shows details about an individual product, including a button that allows the user to add the product to the cart. There is also a
reviews section at the bottom, showing product reviews and including the review form for logged in users.

  - [Cart](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/cartscreenshot.png) -
Shows users all of the products in their cart, as well as their cart total

  - [Checkout](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/checkoutscreenshot.png) -
Page where users input their payment information, place their order and can see an order summary

  - [Profile](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/profilescreenshot.png) -
Page where users can see their default information and order history

  - [Product Management](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/productmanagementscreenshot.png) -
Contains form where site owners can add a product

  - [Blog](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/blogscreenshot.png) -
Show all blog posts

  - [Blog Post](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/blogpostscreenshot.png) -
Show individual blog post

  - [Blog Management](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/blogmanagementscreenshot.png) -
Contains form where site owners can add a blog post

  - [Login / Register / Signout](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/authenticationscreenshot.png) -
Pages for user authentication and profile creation

-  #### Colour Scheme
    -   The colour scheme for this site was rendered on [__Coolor__](https://coolors.co/) and can be seen below:

    ![alt text](https://github.com/yipmunallen/Fourth-Milestone-Project/blob/master/static/images/readme/colour-scheme.png "Colour Scheme")


 -   #### Typography
      -   The font used for headings throughout the site is "Bodoni Moda". "Arimo" is used for the remainder of text. Sans-serif has been used as the fallback font throughout.

## Features

### Common Features

- **Navigation**
    - The navigation bar is sticky to the top of the window so that it can be accessed at all times
    - All of the main pages (other than the individual product and blog pages) can be accessed from the navigation links
    - On smaller screen sizes, all of the navigation links can be accessed via the hamburger button
    - The brand logo will redirect the user back to the homepage when clicked
    - The search icon in the navigation bar opens a full page search bar overlay when clicked. This can be exited using either the close button in the top right of the screen
        or the escape key

- **Footer**
    - The footer is displayed at the bottom of the page for all content sizes
    - It contains links to socials, however these will just redirect to the website home pages for this project. The links open in 
    a new page so as not the close the site page.

- **Toasts**
    - Toasts have been used to provide feedback to users, displaying success, error, info and warning messages. 
    - A toast is also used to display the current cart to the user when items are added to it.
    - The cart toast will fade out automatically or can be dismissed using the close button

- **Admin** - Features that are only available to admin accounts
    - Admin's have two additional options available from the user icon dropdown in the navigation bar:
        - Product Management (used to add a product to the site)
        - Blog Management (user to add a blog post to the site) 
    - On individual product pages, buttons to edit and delete a product from the UI appear for admin users only
    - On individual blog pages, buttons to edit and delete a blog from the UI appear for admin users only
    - Access to all the following are available via the Django admin site:
        - User Profiles
        - Product categories
        - Products
        - Orders
        - Product reviews
        - Blog posts
        - Blog comments

- **AllAuth**
    - The Django AllAuth package provides all the authentication and registration features for signing up, logging in, logging out, changing passwords etc.
    - The links to these features can be found under the user icon dropdown in the navigation bar at all times or under "My Profile"

### Page Features

- **Products Page**
    - Users can select to view specific categories of products from the navigation bar's "SHOP" dropdown link
    - The "All Products" and Product category pages also contain a dropdown that allow users to sort by:
        - Name (A-Z)
        - Name (Z-A)
        - Price (Low - High)
        - Price (High - Low)
        - Recommended
    - The products page will also show any valid product search results
    - The number of results showing on the page will be displayed in the top left of the screen
    - A banner stating the free delivery threshold is at the top of the screen
    - Each product has the product name and product price under it, and an alternative image of the product shows on hover

- **Product Details Page**
    - Product details including the product name, price and description are shown, as well as the percentage of reviewers
        that have recommended the product
    - The quantity selector allow users to select 1-20 of a product
    - An "Add to Cart" button adds the product (with quantity) to the cart
    - There is a link to other products in the product category next to "See more:"
    - The reviews section at the bottom of the page has two tabs:
        - Reviews 
            - Shows the number of reviews that have been left as well as the reviews themselves
            - Each review shows the date created, review title, username of reviewer, the review subject and a badge containing
            "I recommend this product", if the user selected that option when leaving their review
        - Write a review
            - If the site user is not signed in, they will be prompted to log in or sign up
            - If the user is already signed in, this tab will contain a form allowing them to leave a reviewv

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
        price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.00)])
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

- [__HTML5__](https://en.wikipedia.org/wiki/HTML5) - Used to structure and present the website
- [__CSS__](https://en.wikipedia.org/wiki/CSS) - Used to style the website
- [__JavaScript__](https://en.wikipedia.org/wiki/JavaScript) - Used to collapse navbars and dynamically show the edit comment forms
- [__Python__](https://en.wikipedia.org/wiki/Python_(programming_language)) - Used for the backend development

### Frameworks, Libraries & Programs

- [__Bootstrap Framework__](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Used for the site design, forms, modals, toasts and dropdowns.

- [__Mockflow__](https://www.mockflow.com/) - Used to create the wireframes during the planning stage of the project.

- [__Google Fonts__](https://fonts.google.com/) - Used to import the "Bodoni Moda" and "Arimo" fonts used throughout the site

- [__Font Awesome__](https://fontawesome.com/) - Used to import the icons used for the watchlists

- [__Favicon__](https://favicon.io/) - Used to created the favicon used on the site

- [__JQuery__](https://jquery.com/) - Used to manipulate HTML and CSS properties

- [__Django__](https://www.djangoproject.com/) - Framework used to build the site

- [__Stripe__](https://jquery.com/) - Used to facilitate payments

- [__Heroku__](https://heroku.com/) - Used to deploy the site

- [__Heroku__](https://heroku.com/) - Used to deploy the site

- [__SQLite__](https://www.sqlite.org/index.html) - Database used during development

- [__AWS S3__](https://www.sqlite.org/index.html) - Used to store images and static files displayed in the deployed site

- [__Git__](https://git-scm.com/) - Used for version control

- [__Github__](https://github.com/) - Used to store all website code once pushed from Git

- [__Google Chrome Developer Tools__](https://developers.google.com/web/tools/chrome-devtools) - Used to inspect page elements, test different CSS styles and debug site issues using the console

## Testing

In order for the website to pass testing, the following have been tested both whilst in development and on the live website:

1. Functionality in line with user stories
1. Additional functionality required for website
1. Compatibility with multiple devices and browsers

In addition: 

1. The HTML, CSS, Javascript and Python files have been validated using respective online validators.

### User Stories

#### Site Owner Goals

1. Create a visually appealing site with a strong brand identity
    - The brand logo is in the navigation bar at all times
    - The same fonts, colours and image types have been used throughout the site to maintain a consistent brand identity
1. Add products on the website so I can add new items to my stores
    - Admin users can access the "add product" form from the "Product Management" selection in the navbar at all times
    - Mandatory fields are marked with a *
    - The cancel button redirects the user back to the "all products" view
    - When the "Add Product" button is clicked, the user is redirected to the newly created product detail page
        and the new product will show on the all products page, and under it's relevant category.
1. Edit existing products in my store so I can change product prices, descriptions, images and other product information.
    - Admin users can click the edit button on any product detail page to edit the product
    - This button is not shown or available to non-admin users or non logged-in users
    - Upon click, the admin user will be redirect to the "Edit Product" form for that product which is already completed with the current product details
    - Mandatory fields are marked with a *, and a product cannot be edited if any of those fields are missing
    - When the "Add Product" button is clicked, the user is redirected back to the newly updated product detail page   
1. Delete products on the website so I can remove items from my store
    - Admin users can click the delete button on any product detail page to delete the product
    - Upon click, an modal will appear, confirming with the user whether they want to delete the product
        - If cancel is clicked, the modal will close and the product will not be deleted
        - If delete is clicked, the product will be deleted from all product pages and the database
1. Create new blog posts so that I can engage with customers and add new content to the site
    - Admin users can access the "add post" form from the "Blog Management" selection in the navbar at all times
    - Mandatory fields are marked with a *
    - The cancel button redirects the user back to the main Blog page
    - When the "Add Post" button is clicked, the user is redirected to the newly created blog post page
        and the new post will show on the main blog page.    
1. Be able to create draft blog posts which users can't see so that I can make updates and publish posts at chosen times
    - Admin users can set the status of their blog posts to "Draft" or "Publish" in the add post and edit post forms.
    - Draft posts are marked with a "draft" badge in both the main blog page, and individual blog pages
    - Draft posts cannot be seen or accessed by non-admin users
    - When the status of a blog post is changed from "Draft" to "Publish" it can be seen by all users and all "Draft" badges are removed
1. Edit existing blog posts in case I've made a mistake and what to make a change to it
    - Admin users can click the edit button on any blog post page to edit the post
    - This button is not shown or available to non-admin users or non logged-in users
    - Upon click, the admin user will be redirect to the "Edit Post" form for that post which is already completed with the current post details
    - Mandatory fields are marked with a *, and a post cannot be edited if any of those fields are missing
    - When the "Add Product" button is clicked, the user is redirected back to the newly updated product detail page 
1. Delete blog posts if I no longer what them on the site
    - Admin users can click the delete button on any blog post page to delete the product
    - Upon click, an modal will appear, confirming with the user whether they want to delete the post
        - If cancel is clicked, the modal will close and the post will not be deleted
        - If delete is clicked, the post will be deleted from the blog page
1. Have links that direct users to our social sites for further engagement
    - Links are available in the footer of the site at all times. These currently direct to the homepage of that site in a new tab.

#### Site User Goals

*Viewing and Navigation*

1. Be able to easily navigate the site so that I can quickly find what I am looking for
    - The navigation bar is positioned at the top of the screen and is fixed when the site is being scrolled so users can
        access site pages at all times
1. View a list of all products available so that I can purchase them
    - A view of all products can be seen by selecting "All Products" from the Shop dropdown in the navigation bar at all times
1. View specific categories of products so that I can filter for products that I'm interested in.
    - Available categories can selected from the Shop dropdown in the navigation bar at all times
1. View individual product details so that I can decide if I want to make a purchase
    - Product details are displayed on all individual product pages, including product name, price and description
1. Get feedback on the site when actions are performed so that I know if they have been successful or not
    - Toasts have been used to display feedback to user across the site, showing at the top of the screen (see further information in [Additional Testing](#additional-testing))

*Sorting and Searching*

1. Search the site so that I can quickly and easily find what I'm looking for.
    - A search form is available from the navigation bar at all times by clickly on the search icon
1. Sort products that I am viewing so that I can identify products that fit my budget or that have been recommended
    - A "Sort By" selector is available on all product pages allowing users to order by price (low/high), name(a/z) and recommended

*Registration and User Accounts*

1. Easily sign up, log in and log out of an account so that I have a personal account and be able to view my profile
    - Users can sign up for the site at all times by selecting "Sign Up" from the User icon dropdown in the navigation bar
    - Users can sign up for the site at all times by selecting "Log In" from the User icon dropdown in the navigation bar
    - Signed in users can log out of the site at all times by selecting "Log Out" from the User icon dropdown in the navigation bar
1. Recover my password if I forget it so that I can regain access to my account
1. Receive an email confirmation after registering so I can verify my account registration was successful
1. Have a personalised user profile so that I can view my order history and save default payment information
    - All users that sign up to the site have a user profile created for them
    - The User Profile can be accessed at all times by selecting "My Profile" from the User icon dropdown in the navigation bar
    - The User Profile page allows users to set a default delivery address and also view their order history
    - Clicking on an order number will show them the full details of their order

*Purchasing and Checkout*

1. Select the quantity of a product I want to buy
    - There is a quantity selector shown on all individual product pages, as well as on the Cart page for each product in the cart
1. View the items in my cart so that I can confirm the items that I am purchasing along with the total cost
    - When users add an item to their cart, a toast will show the current items in their cart
    - When users have items in their cart, the number of product will appear next to the cart icon in the navigation bar at all times
    - Users can see full detail of all items in their cart, as well as a cart total by clicking on the cart icon in the navigation bar which will redirect them
        to the cart page
1. Adjust the quantity of products in my cart in case i've make a mistake when adding them
    - Users can update the quantity of products in their cart by changing the quantity and clicking "update"
1. Remove an item from my cart if I no longer what to purchase it
    - Users can remove a product from their cart by clicking the trash icon at the end of the product row in the cart
1. Easily enter my payment information so that I can check out quickly
    - Users can input their payment information in the checkout page
    - Logged in users that have set default information in the "My Profile" page will have this information filled in for them automatically
1. Get an order confirmation after checkout to verify I haven't made any errors
    - When an order has successfully been received, the user will be redirected to an order confirmation page
    - The order confirmation page will show all the product purchased, as well as the delivery information that has been inputted

*Reviews*

1. See previous reviews so that I can make an informed purchase
    - All previous product reviews can be seen at the bottom of each product page
    - If users recommend a product, the "I recommend this product" badge will show on their review
    - In addition, the percentage of reviewers that have recommended a product are displayed along with the product details at the top
        of individual product detail pages (unless the percentage is 0) allowing users to see at a glance how popular the product is
    - Users can see the number of reviews that have been left for a product by the number next to the "reviews" tab in brackets
1. Leave a review on a product so that I can inform other shoppers about whether it was a good purchase or not
    - Users can leave a review using the "Write a review" tab at the bottom of each product page
    - This feature is only available to logged in users, and if a user is not logged in they will be prompted to either log in or sign up
    - Upon submission of the review form, the product page will reload and the user will be able to see their review in the reviews tab
1. Edit my review in case I've made a mistake and what to make a change to it
    - If a user has left a review, then an ellipsis button will appear in the right corner of their review. Clicking it will give them the option to edit their review
        and open up an "edit review" modal on the current page
    - The current review details will be filled into the form already, and once they make their change and submit, the page will reload with their updated review
1. Delete my review if I no longer want it on the site
    - If a user has left a review, then an ellipsis button will appear in the right corner of their review. Clicking it will give them the option to delete their review.
    - When the delete review button is clicked, a modal will appear confirming to the user whether they want to delete their review. If "cancel" is clicked, the review will not
        be deleted. If "Delete" is clicked, the review will be deleted and the page will reload, removing their review from the reviews section

*Blog*

1. See previous comments on blog posts so that I can see other user's thoughts
    - All previous blog post comments can be seen at the bottom of each blog page
    - Users can see the number of comment that have been left for a post by the number next to the "comments" tab in brackets
1. Leave comments on blog posts so that I engage with the store owners and other customers
    - Users can leave a comment using the "Write a comment" tab at the bottom of each product page
    - This feature is only available to logged in users, and if a user is not logged in they will be prompted to either log in or sign up
    - Upon submission of the comment form, the blog page will reload and the user will be able to see their comment in the comment tab

### Additional Testing

  - __Defensive Programming__- Tests have been conducted to ensure users cannot perform actions or access pages they shouldn't be able to:
    1. If a logged in user:
        1. Tries to access the sign up page, they will be redirected to their feed and a message "You already have an account" will be shown. 
        2. Tries to access the log in page, they will be redirected to their feed and a message "You are already logged in" will be shown. 
    2. If a non logged in user:
        1. Tries to access a feed, they will be redirected to the index page. 
        2. Tries to add to a watchlist, they will be prompted to log in or sign up
    3. A comment cannot be deleted unless the user is logged in and the comment was written by them. If this is attempted using the url, the stock page will reload and no comment is deleted.

  - __Toasts__-  Toast messages are used to confirm actions and convey messages to users. There are successfully shown:
    1. If a login attempt is unsuccessfull , "Incorrect username and/or password" shows
    2. If a user tried to sign up with an existing username, "username already exists" shows.
    3. If a new user signs up, they will be directed to the feed page where "Welcome to Ticker, Username. This feed shows recent comments on stocks" shows.  
    4. If a user logs in, they will be directed to the feed page where "Welcome, Username" shows.
    5. If a user creates a new comment, "Comment successfully added" shows.
    5. If a user edits a comment, "Comment successfully edited" shows.
    5. If a user deletes a comment, "Comment successfully deleted" shows.

  - __Form Validation__- Form validation has been tested:

    | Product Management Forms                                        | Testing |
    |-----------------------------------------------------------------|---------|
    | User cannot submit the form (add or edit) without a Name        | PASS    |
    | User cannot submit the form (add or edit) without a Description | PASS    |
    | User cannot submit the form (add or edit) without a Price       | PASS    |
    | User cannot submit the form (add or edit) without an Image 1    | PASS    |
    | User cannot submit the form (add or edit) without an Image 2    | PASS    |
    | User cannot submit the form (add or edit) if the Price is < 0   | PASS    |

    | Blog Management Forms                                       | Testing |
    |-------------------------------------------------------------|---------|
    | User cannot submit the form (add or edit) without a Title   | PASS    |
    | User cannot submit the form (add or edit) without a Author  | PASS    |
    | User cannot submit the form (add or edit) without a Summary | PASS    |
    | User cannot submit the form (add or edit) without Content   | PASS    |
    | User cannot submit the form (add or edit) without an Image  | PASS    |
    
    | Reviews Form                                                         | Testing |
    |----------------------------------------------------------------------|---------|
    | If a user is not logged in or signed up, they cannot access the form | PASS    |
    | Users cannot submit the form without a title                         | PASS    |
    | Users cannot submit the form without a description                   | PASS    |

    | Comments Form                                                        | Testing |
    |----------------------------------------------------------------------|---------|
    | If a user is not logged in or signed up, they cannot access the form | PASS    |
    | Users cannot submit the form (add or edit) without a comment         | PASS    |

    | Checkout Form                                                                | Testing |
    |------------------------------------------------------------------------------|---------|
    | User cannot submit the form (add or edit) without an Email Address           | PASS    |
    | User cannot submit the form (add or edit) without a Phone Number             | PASS    |
    | User cannot submit the form (add or edit) without a Full Name                | PASS    |
    | User cannot submit the form (add or edit) without a Street Address 1         | PASS    |
    | User cannot submit the form (add or edit) without a Town or City             | PASS    |
    | User cannot submit the form (add or edit) without a Country                  | PASS    |
    | User cannot submit the form (add or edit) without a valid Card Number        | PASS    |
    | User cannot submit the form (add or edit) without a valid Card Expiry Date   | PASS    |
    | User cannot submit the form (add or edit) without a valid Card Security Code | PASS    |
    | User cannot submit the form (add or edit) without a valid Postcode           | PASS    |


  - __404 Error__- This has been tested to ensure that the custom 404 error page will show if the error occurs, with a link that redirects to the home page.

  - __405 Error__- This has been tested to ensure that the custom 405 error page will show if the error occurs, with a link that redirects to the home page.

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

