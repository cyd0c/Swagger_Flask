from flask import Flask
from flask import send_from_directory
from controllers import default_controller
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)
# Path to the Swagger YAML file
SWAGGER_URL = '/api/docs'  # URL to access Swagger UI
API_URL = '/static/swagger.yaml'  # URL to the Swagger spec file

# Setup Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "To-Do List API"}
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Define routes and connect to controllers
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return default_controller.get_todos()

@app.route('/api/todos', methods=['POST'])
def create_todo():
    return default_controller.create_todo()

@app.route('/api/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    return default_controller.get_todo_by_id(id)

@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo_by_id(id):
    return default_controller.update_todo_by_id(id)

@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todo_by_id(id):
    return default_controller.delete_todo_by_id(id)


@app.route('/swagger/<path:filename>')
def swagger_files(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'swagger'), filename)

if __name__ == '__main__':
    app.run(debug=True)
