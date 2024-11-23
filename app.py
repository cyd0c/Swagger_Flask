from flask import Flask
from flask_cors import CORS
import connexion

# Create the Connexion app
app = connexion.FlaskApp(__name__, specification_dir='./')

# Enable CORS for specific origins
CORS(app.app, resources={r"/api/*": {"origins": ["http://localhost:8000", "http://127.0.0.1:8000"]}})

# Add the OpenAPI specification (your YAML file)
app.add_api('swagger.yaml')

# Access the underlying Flask app to set the debug mode
app.app.config['DEBUG'] = True

# Run the app
app.run(port=8000)
