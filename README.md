# TechCorp Solutions - Company Website

A professional Django website showcasing development services with modern UI/UX design.

## Features

- **Homepage**: Company introduction with hero section, stats, and service preview
- **Services Page**: Detailed service offerings (Software, App, Website Development)
- **About Page**: Team member cards with individual portfolio links
- **Contact Page**: Professional contact form with service type selection
- **Individual Portfolio Pages**: Detailed team member profiles with projects
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Admin Panel**: Easy content management for team members and projects

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Load sample data:
   ```bash
   python manage.py create_sample_data
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Admin Access

- URL: `/admin/`
- Username: `admin`
- Password: Set during superuser creation

## Project Structure

- **Models**: TeamMember, Project, ContactSubmission
- **Views**: Home, Services, About, Contact, Portfolio
- **Templates**: Responsive HTML templates with Tailwind CSS
- **Forms**: Professional contact form with validation

## Customization

1. Update company information in templates
2. Add team members through admin panel
3. Add projects for each team member
4. Customize colors and styling in base.html
5. Update contact information and social links

## Technologies Used

- Django 5.0
- Tailwind CSS
- Font Awesome Icons
- SQLite Database
- Pillow for image handling