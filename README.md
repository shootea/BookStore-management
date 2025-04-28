A modern, full-featured Bookstore Management System built with Django and styled with a sleek, responsive UI. 
This project is designed for efficient management of books, authors, and genres, and demonstrates best practices
in Django development, database modeling, and frontend integration.

🚀 Features
Book Management
Add, Edit, Delete Books: Full CRUD operations for books with intuitive forms and validation.
Genre Management: Add, edit, and delete genres, with each book linked to one or more genres.
Author Management: Manage authors and associate them with books.

User Experience
Modern Glassmorphism UI: Stylish, gradient backgrounds and animated buttons for a contemporary look.
Responsive Design: Works seamlessly on desktops, tablets, and mobile devices.
Quick Navigation: Fixed navigation buttons for easy access to home and book list pages.

Security & Authentication
CSRF Protection: All forms are secured with Django’s CSRF tokens.

🛠️ How It Works & Concepts Used
Django Models:
Book, Author, and Genre models with proper relationships (ForeignKey, ManyToMany).
Model methods and properties for clean data access.

Forms & Validation:
Django ModelForms for creating and updating books, authors, and genres.
Server-side validation for data integrity.

Views:
Function-based views for CRUD operations.
Use of get_object_or_404 for robust error handling.
Context passing to templates for dynamic content rendering.

Templates:
Django template language for dynamic HTML generation.
Template inheritance for DRY (Don’t Repeat Yourself) code.
Usage of template tags for URL resolution and data display.

Static Files & Styling:
Custom CSS for glassmorphism effects and responsive layouts.
Integration of Google Fonts for modern typography.

URL Routing:

Clean URL patterns for all major actions.
Use of named URLs for maintainable navigation.

