"""
Setup script for Resource Management System
Run this script after installing dependencies to initialize the database and create demo users
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resource_management.settings')
django.setup()

from django.contrib.auth.models import User, Group
from resources.models import Resource


def create_groups():
    """Create user groups"""
    print("Creating user groups...")
    faculty_group, created = Group.objects.get_or_create(name='Faculty')
    if created:
        print("✓ Faculty group created")
    else:
        print("✓ Faculty group already exists")
    
    student_group, created = Group.objects.get_or_create(name='Student')
    if created:
        print("✓ Student group created")
    else:
        print("✓ Student group already exists")


def create_users():
    """Create demo users with different roles"""
    print("\nCreating demo users...")
    
    # Create Administrator (superuser)
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print("✓ Administrator created (username: admin, password: admin123)")
    else:
        print("✓ Administrator already exists")
    
    # Create Faculty user
    if not User.objects.filter(username='faculty').exists():
        faculty = User.objects.create_user(
            username='faculty',
            email='faculty@example.com',
            password='faculty123'
        )
        faculty_group = Group.objects.get(name='Faculty')
        faculty.groups.add(faculty_group)
        print("✓ Faculty user created (username: faculty, password: faculty123)")
    else:
        print("✓ Faculty user already exists")
    
    # Create Student user
    if not User.objects.filter(username='student').exists():
        student = User.objects.create_user(
            username='student',
            email='student@example.com',
            password='student123'
        )
        student_group = Group.objects.get(name='Student')
        student.groups.add(student_group)
        print("✓ Student user created (username: student, password: student123)")
    else:
        print("✓ Student user already exists")


def create_sample_resources():
    """Create sample resources"""
    print("\nCreating sample resources...")
    
    admin = User.objects.get(username='admin')
    faculty = User.objects.get(username='faculty')
    
    sample_resources = [
        {
            'title': 'Introduction to Python',
            'resource_type': 'lecture',
            'description': 'Basic concepts and fundamentals of Python programming language.',
            'created_by': admin
        },
        {
            'title': 'Django Web Framework',
            'resource_type': 'lecture',
            'description': 'Complete guide to building web applications with Django.',
            'created_by': faculty
        },
        {
            'title': 'Assignment 1: Python Basics',
            'resource_type': 'assignment',
            'description': 'Practice exercises on Python variables, loops, and functions.',
            'created_by': faculty
        },
        {
            'title': 'Database Design Principles',
            'resource_type': 'reference',
            'description': 'Comprehensive guide to database normalization and design patterns.',
            'created_by': admin
        },
        {
            'title': 'REST API Development',
            'resource_type': 'lecture',
            'description': 'Learn how to build RESTful APIs using Django REST Framework.',
            'created_by': faculty
        },
    ]
    
    # Create dummy files for sample resources
    os.makedirs('media/resources', exist_ok=True)
    
    for i, resource_data in enumerate(sample_resources):
        if not Resource.objects.filter(title=resource_data['title']).exists():
            # Create a dummy text file
            file_path = f'media/resources/sample_{i+1}.txt'
            with open(file_path, 'w') as f:
                f.write(f"Sample content for {resource_data['title']}")
            
            resource = Resource.objects.create(
                title=resource_data['title'],
                resource_type=resource_data['resource_type'],
                description=resource_data['description'],
                created_by=resource_data['created_by'],
                uploaded_file=f'resources/sample_{i+1}.txt'
            )
            print(f"✓ Created: {resource.title}")
    
    print(f"\nTotal resources: {Resource.objects.count()}")


def main():
    print("=" * 60)
    print("Resource Management System - Initial Setup")
    print("=" * 60)
    
    create_groups()
    create_users()
    create_sample_resources()
    
    print("\n" + "=" * 60)
    print("Setup completed successfully!")
    print("=" * 60)
    print("\nDemo credentials:")
    print("  Administrator: admin / admin123")
    print("  Faculty:       faculty / faculty123")
    print("  Student:       student / student123")
    print("\nYou can now run the server with: python manage.py runserver")
    print("=" * 60)


if __name__ == '__main__':
    main()
