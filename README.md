# Rescue Me Read Me

## Table of Contents
1. [User Stories & Acceptance Criteria](#1-user-stories--acceptance-criteria)
   - [Search and Filter](#11-search-and-filter)
   - [View Detailed Profiles of Animals](#12-view-detailed-profiles-of-animals)
   - [Understand the Rescue's Requirements](#13-understand-the-rescues-requirements)
   - [Get in Touch with the Rescue Shelter](#14-get-in-touch-with-the-rescue-shelter)
   - [Browse and Buy Products in the Shop](#15-browse-and-buy-products-in-the-shop)
   - [FAQ](#16-faq)
   - [About Us](#17-about_us)
   - [Blog](#18-blog)
   - [Our Mission](#19-our_mission)
   - [User Registration and Authentication](#110-user-registration-and-authentication)
   - [User Dashboard](#111-user-dashboard)
   - [Notifications and Alerts](#112-notifications-and-alerts)
   - [Social Media Integration](#113-social-media-integration)

---

## 1. User Stories & Acceptance Criteria

### 1.1 Search and Filter

#### MoSCoW Framework
- **Must Have:** Users can search for animals using keywords and apply filters (e.g., species, breed, age, size) to refine results. Search results update dynamically without reloading the page.
- **Should Have:** Filters can be combined for more precise searches, and users can easily clear filters to start a new search.
- **Could Have:** Search results are paginated for better performance on large datasets.
- **Won’t Have:** Advanced AI-based recommendations for animals (future feature).

#### User Journey
Sarah, a first-time pet adopter, visits the website to find a dog that fits her lifestyle. She types "Golden Retriever" into the search bar, and the results dynamically update to show available Golden Retrievers. She applies filters for "puppy" and "medium size" to narrow her search. The results instantly update without reloading the page. Sarah clears the filters to start a new search for cats and is impressed by how easy it is to find animals that match her preferences.

#### Acceptance Criteria
- **Search Bar:** Users can enter keywords in a search bar to find animals.
- **Filter Options:** Users can filter animals by species, breed, age, and size.
- **Dynamic Search Results:** Search results update instantly without reloading the page.
- **Responsive Design:** The search and filter functionality is optimized for various screen sizes.

#### Implementation
- **Backend (Django):**
  - Use Django views to handle search and filter logic.
  - Implement `django-filter` for filtering animals by species, breed, age, and size.
  - Use Django’s `Paginator` for paginated search results.
- **Frontend:**
  - Use AJAX to dynamically update search results without reloading the page.
  - Ensure filters and search terms are passed to the backend via query parameters.
  - Use Django templates to render search results.

---

### 1.2 View Detailed Profiles of Animals

#### MoSCoW Framework
- **Must Have:** Users can view detailed profiles of animals, including a picture, name, age, breed, background story, health status, and special needs.
- **Should Have:** Users can navigate between profiles using "Next" and "Previous" buttons.
- **Could Have:** Profiles include embedded videos or additional media to showcase the animal’s personality.
- **Won’t Have:** Real-time video calls with shelters to meet the animal (future feature).

#### User Journey
John is looking for a cat to adopt. He clicks on a search result for a cat named "Mittens" and is taken to a detailed profile page. The page includes a picture of Mittens, her age, breed, and a heartwarming story about her rescue. John also sees information about her health status and special needs. He navigates to other profiles using the "Next" and "Previous" buttons but keeps coming back to Mittens' profile. He decides to proceed with the adoption process.

#### Acceptance Criteria
- **Animal Profile Details:** Users can view detailed profiles of animals, including a picture, name, age, breed, background story, health status, and special needs.
- **Profile Navigation:** Users can easily navigate between different animal profiles.

#### Implementation
- **Backend (Django):**
  - Create a `DetailView` for animal profiles.
  - Use Django’s ORM to fetch animal details from the database.
- **Frontend:**
  - Use Django templates to render animal profile details dynamically.
  - Add navigation links to move between profiles.

---

### 1.3 Understand the Rescue's Requirements

#### MoSCoW Framework
- **Must Have:** Users must complete a checklist confirming they understand the rescue's requirements before proceeding.
- **Should Have:** The contact form becomes visible only after the checklist is completed.
- **Could Have:** The checklist includes links to educational resources for first-time adopters.
- **Won’t Have:** Automated approval of adoption applications (future feature).

#### User Journey
Emily finds a dog she wants to adopt but notices a checklist she must complete before proceeding. The checklist includes items like "I understand the dog requires daily exercise" and "I have a fenced yard." Emily carefully reads and checks each item. Once she completes the checklist, a contact form appears. She fills out her details and submits the form, feeling confident that she understands the rescue's requirements.

#### Acceptance Criteria
- **Requirements Checklist:** Users must complete a checklist confirming they understand the rescue's requirements and the animal's needs.
- **Contact Form:** Display a contact form only after the checklist is completed.

#### Implementation
- **Backend (Django):**
  - Use Django forms to create the checklist and validate completion.
  - Display the contact form only after successful validation of the checklist.
- **Frontend:**
  - Use Django templates to render the checklist and contact form.
  - Add basic JavaScript for client-side validation (optional).

---

### 1.4 Get in Touch with the Rescue Shelter

#### MoSCoW Framework
- **Must Have:** Users can submit a referral email with their details and a summary of the checklist.
- **Should Have:** Users receive a confirmation email with the shelter's contact details.
- **Could Have:** The confirmation email includes a personalized message from the shelter.
- **Won’t Have:** Real-time chat with shelter staff (future feature).

#### User Journey
After completing the checklist, Emily submits a contact form to express her interest in adopting Mittens. She receives a confirmation email with the shelter's contact details and a summary of her application. The email reassures her that the shelter will contact her soon. She feels confident that her application has been received and looks forward to hearing back.

#### Acceptance Criteria
- **Referral Email:** Users can submit a referral email with their details and a summary of the checklist.
- **Confirmation Email:** Users receive a confirmation email with the shelter's contact details.

#### Implementation
- **Backend (Django):**
  - Use Django’s `send_mail` to send referral and confirmation emails.
  - Use Django forms to handle contact form submissions.
- **Frontend:**
  - Use Django templates to display the contact form and confirmation message.

---

### 1.5 Browse and Buy Products in the Shop

#### MoSCoW Framework
- **Must Have:** Users can browse product categories, add items to a shopping cart, and securely complete purchases.
- **Should Have:** Users can view product details, including images, descriptions, and prices.
- **Could Have:** Users can save items to a wishlist for future purchases.
- **Won’t Have:** Subscription-based product delivery (future feature).

#### User Journey
Mark visits the shop to buy supplies for his new dog. He browses categories like "Food," "Toys," and "Accessories." He adds a leash and a bag of dog food to his cart. At checkout, he securely enters his payment details and completes the purchase. Mark receives an order confirmation email and is excited to receive his items.

#### Acceptance Criteria
- **Product Categories:** Users can browse different categories of pet products.
- **Shopping Cart:** Users can add items to a cart and proceed to checkout.
- **Payment Integration:** Secure payment transactions are supported.

#### Implementation
- **Backend (Django):**
  - Use Django models to manage product categories and items.
  - Use Django sessions to store cart data.
  - Integrate Stripe or PayPal for secure payment processing.
- **Frontend:**
  - Use Django templates to render product listings and cart details.
  - Use JavaScript for minor interactivity (e.g., updating cart quantities).

---

### 1.6 FAQ

#### MoSCoW Framework
- **Must Have:** Users can access the FAQ page and navigate through questions organized into categories.
- **Should Have:** Users can expand and collapse FAQ entries to view answers.
- **Could Have:** FAQs include links to related blog posts or resources.
- **Won’t Have:** AI-powered chatbot for answering questions (future feature).

#### User Journey
Lisa has questions about the adoption process. She navigates to the FAQ page and finds answers organized into categories like "Adoption," "Donations," and "Volunteering." She clicks on a question to expand it and read the answer. The clear and concise information helps her understand the process, and she feels more confident about adopting.

#### Acceptance Criteria
- **Information Access:** Users can easily access the FAQ page from the main navigation menu.
- **Content Structure:** FAQs are organized into logical categories for easy navigation.

#### Implementation
- **Backend (Django):**
  - Use a `ListView` to fetch FAQ entries from the database.
- **Frontend:**
  - Use Django templates to render FAQ content.
  - Add collapsible sections using JavaScript for better UX.

---

### 1.7 About Us

#### MoSCoW Framework
- **Must Have:** Users can access the About Us page to learn about the organization’s mission, history, and team members.
- **Should Have:** The page includes pictures and bios of the founders and key team members.
- **Could Have:** An interactive timeline showcasing the organization’s milestones.
- **Won’t Have:** Live video interviews with the founders (future feature).

#### User Journey
Curious about the organization, Sarah visits the "About Us" page. She reads about the founders' passion for rescuing animals and the organization's mission to reduce the number of animals in shelters. She also learns about the team members and their roles. The page inspires her to support the organization by donating.

#### Acceptance Criteria
- **Information Access:** Users can easily access the About Us page from the main navigation menu.
- **Content Structure:** The page provides a detailed history of why the company was built.

#### Implementation
- **Backend (Django):**
  - Use Django templates to render the About Us page.
- **Frontend:**
  - Add navigation elements to move between sections about the company's mission and founders.

---

### 1.8 Blog

#### MoSCoW Framework
- **Must Have:** Users can access blog posts, which include a title, publication date, author name, and content.
- **Should Have:** Users can leave comments on blog posts and share them on social media.
- **Could Have:** Blog posts include embedded videos or infographics.
- **Won’t Have:** AI-generated blog content (future feature).

#### User Journey
David visits the blog to learn more about pet care. He finds a post titled "5 Tips for First-Time Dog Owners" and reads it. The post includes helpful advice, and David leaves a comment thanking the author. He also shares the post on his social media to help his friends who are considering adopting pets.

#### Acceptance Criteria
- **Information Access:** Users can easily access the Blog page from the main navigation menu.
- **Content Structure:** Each blog post includes a title, publication date, author name, and content.

#### Implementation
- **Backend (Django):**
  - Use a `ListView` to fetch and display blog posts.
  - Implement search and categorization using `django-filter`.
  - Use Django’s `comments` framework for blog comments.
- **Frontend:**
  - Use Django templates to render blog posts and comments.

---

### 1.9 Our Mission

#### MoSCoW Framework
- **Must Have:** Users can access the Our Mission page to learn about the organization’s goals and impact.
- **Should Have:** The page includes visual elements like images and infographics.
- **Could Have:** The page features testimonials from adopters and volunteers.
- **Won’t Have:** Real-time impact tracking (future feature).

#### User Journey
Jessica visits the "Our Mission" page to learn about the organization's goals. She reads about their efforts to reduce the number of animals in shelters and their plans for the future. The page includes infographics showing the impact they've made, which inspires Jessica to volunteer.

#### Acceptance Criteria
- **Information Access:** Users can easily access the Our Mission page from the main navigation menu.
- **Content Structure:** The page provides a clear explanation of the company’s mission, goals, and future direction.

#### Implementation
- **Backend (Django):**
  - Use Django templates to render the Our Mission page.
- **Frontend:**
  - Add interactive elements like progress trackers or future milestones.

---

### 1.10 User Registration and Authentication

#### MoSCoW Framework
- **Must Have:** Users can register, log in, and recover their passwords.
- **Should Have:** Users receive a confirmation email upon registration.
- **Could Have:** Users can log in using social media accounts.
- **Won’t Have:** Biometric authentication (future feature).

#### User Journey
Tom creates an account to save his favorite animals. He fills out the registration form and receives a confirmation email. Later, he logs in to view his saved searches. When he forgets his password, he uses the password recovery feature to reset it and regain access to his account.

#### Acceptance Criteria
- **User Registration:** Users can create an account and receive a confirmation email.
- **User Login:** Users can log in with their registered email and password.
- **Password Recovery:** Users can request a password reset link.

#### Implementation
- **Backend (Django):**
  - Use Django’s `User` model for registration and authentication.
  - Use `PasswordResetView` and `PasswordChangeView` for password recovery.
- **Frontend:**
  - Use Django templates to render registration, login, and password recovery forms.

---

### 1.11 User Dashboard

#### MoSCoW Framework
- **Must Have:** Users can view and update their profile information and activity history.
- **Should Have:** Users can save search criteria and preferences.
- **Could Have:** Users receive personalized recommendations based on their activity.
- **Won’t Have:** Advanced analytics for user behavior (future feature).

#### User Journey
Anna logs into her account and visits her dashboard. She updates her profile information, reviews her activity history, and saves a search for "small dogs." The dashboard makes it easy for her to manage her preferences and track her interactions with the website.

#### Acceptance Criteria
- **Profile Management:** Users can view and update their profile information.
- **Activity History:** Users can view their previous interactions with the website.
- **Saved Searches and Preferences:** Users can save search criteria and preferences.

#### Implementation
- **Backend (Django):**
  - Use `UpdateView` for profile management.
  - Use Django’s ORM to fetch user activity history and preferences.
- **Frontend:**
  - Use Django templates to render dashboard content.

---

### 1.12 Notifications and Alerts

#### MoSCoW Framework
- **Must Have:** Users can sign up for notifications about animals matching their saved search criteria.
- **Should Have:** Users receive email alerts for order updates and important announcements.
- **Could Have:** Notifications are sent via SMS or push notifications.
- **Won’t Have:** Real-time notifications for all website updates (future feature).

#### User Journey
Michael signs up for notifications about small dogs. A week later, he receives an email alert about a new dog that matches his criteria. Excited, he visits the website to learn more about the dog and starts the adoption process.

#### Acceptance Criteria
- **Animal Availability Alerts:** Users can sign up for notifications when animals matching their saved search criteria become available.

#### Implementation
- **Backend (Django):**
  - Use Django signals to send notifications based on user preferences.
- **Frontend:**
  - Use Django templates to render notification settings.

---

### 1.13 Social Media Integration

#### MoSCoW Framework
- **Must Have:** Users can share animal profiles and blog posts on social media platforms.
- **Should Have:** Users can follow the organization’s social media accounts via links on the website.
- **Could Have:** Social media feeds are embedded on the website.
- **Won’t Have:** Direct messaging with the organization via social media (future feature).

#### User Journey
Sophia finds an adorable dog profile and shares it on her Facebook page using the "Share" button. Her friends see the post and one of them decides to adopt the dog. Sophia feels happy knowing she helped the dog find a home.

#### Acceptance Criteria
- **Share Animal Profiles:** Users can share animal profiles on social media platforms.
- **Share Blog Posts:** Users can share blog posts on social media platforms.

#### Implementation
- **Backend (Django):**
  - Use Django templates to render shareable content.
- **Frontend:**
  - Add social media sharing buttons using JavaScript or third-party libraries.
