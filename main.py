from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# New POST route
@app.route('/contact', methods=['POST'])
def handle_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Process the data here (e.g., send email, save to DB)
    print(f"New message from {name} ({email}): {message}")
    
    return redirect('/')

# Main entry point for the application
# This ensures the server only runs when script is executed directly
if __name__ == "__main__":
    # Start Flask development server
    # debug=True enables automatic reloading and debug pages
    app.run(debug=True)

 