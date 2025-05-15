#!/usr/bin/env python
"""
Setup script to initialize the database and create an admin user.
Run this script once after setting up your project to create all tables
and add an initial admin user.
"""

import argparse
import os
import sys
from pathlib import Path

# Add the project root directory to the Python path
project_root = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_root))

import bcrypt
from db.database import SessionLocal, engine
from models.user import User
from models.photo import Photo

# Create all tables if they don't exist
from db.create_tables import create_tables, drop_tables

def create_admin_user(username, password, full_name, email):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create a database session
    db = SessionLocal()
    
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            print(f"User '{username}' already exists!")
            return False
        
        # Create a new admin user
        admin_user = User(
            username=username,
            password=hashed_password,
            full_name=full_name,
            email=email,
            storage_quota_mb=5120  # 5GB quota for admin
        )
        
        # Add to the database
        db.add(admin_user)
        db.commit()
        print(f"Admin user '{username}' created successfully!")
        return True
        
    except Exception as e:
        db.rollback()
        print(f"Error creating admin user: {e}")
        return False
    
    finally:
        db.close()

def setup_uploads_directory():
    """Create the uploads directory if it doesn't exist"""
    uploads_dir = Path("/uploads")
    if not uploads_dir.exists():
        try:
            uploads_dir.mkdir(parents=True, exist_ok=True)
            print("Created uploads directory")
        except PermissionError:
            print("WARNING: Could not create /uploads directory. Make sure you have the right permissions.")
            print("You may need to create this directory manually and ensure your application has write access.")
    else:
        print("Uploads directory already exists")

def main():
    parser = argparse.ArgumentParser(description='Setup the database and create an admin user')
    parser.add_argument('--drop', action='store_true', help='Drop all tables before creating them')
    parser.add_argument('--username', default='admin', help='Admin username')
    parser.add_argument('--password', default=None, help='Admin password')
    parser.add_argument('--full-name', default='Administrator', help='Admin full name')
    parser.add_argument('--email', default='admin@example.com', help='Admin email')
    
    args = parser.parse_args()
    
    if args.drop:
        print("Dropping all existing tables...")
        drop_tables()
        print("All tables dropped.")
    
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully!")
    
    setup_uploads_directory()
    
    if not args.password:
        args.password = input("Enter password for admin user: ")
    
    create_admin_user(args.username, args.password, args.full_name, args.email)

if __name__ == "__main__":
    main()