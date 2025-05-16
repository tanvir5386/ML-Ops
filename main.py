# Import Flask class from the flask module
from flask import Flask, render_template

# Create Flask application instance
# __name__ helps Flask determine the application's root path
app = Flask(__name__)

# Define route for the root URL ('/')
# This decorator tells Flask what URL should trigger our function
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')


# Main entry point for the application
# This ensures the server only runs when script is executed directly
if __name__ == "__main__":
    # Start Flask development server
    # debug=True enables automatic reloading and debug pages
    app.run(debug=True)

 