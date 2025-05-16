# Import Flask class from the flask module
from flask import Flask

# Create Flask application instance
# __name__ helps Flask determine the application's root path
app = Flask(__name__)

# Define route for the root URL ('/')
# This decorator tells Flask what URL should trigger our function
@app.route('/')
def Tanvir():
    # Return HTML content for the home route
    return '''
    <h1>Hello HTML TANVIR!</h1>
    <p>This is a custom HTML response from Flask</p>
    '''

# Main entry point for the application

# This ensures the server only runs when script is executed directly
if __name__ == '__main__':
    app.run(debug=True)

 