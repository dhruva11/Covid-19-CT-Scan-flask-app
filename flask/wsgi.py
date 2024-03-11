from app import covid_ct  # Import the Flask app instance

# Create the application instance for Gunicorn
application = covid_ct

# If running Gunicorn with multiple workers, you may need to use:
# application = create_app()

if __name__ == "__main__":
    application.run()
