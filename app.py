import connexion


# Create the Connexion app
app = connexion.FlaskApp(__name__, specification_dir='./')

# Add the OpenAPI specification (your YAML file)
app.add_api('swagger.yaml')

# Access the underlying Flask app to set the debug mode
app.app.config['DEBUG'] = True

# Run the app
app.run()
