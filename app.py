from flask import Flask, render_template

app= Flask(__name__)

# Route for your landing page
@app.route("/")
def index():
    """Renders the home page."""
    return render_template("index.html")

# THIS ROUTE IS ESSENTIAL
@app.route("/dashboard")
def dashboard():
    """Renders the dashboard UI."""
    return render_template("dashboard.html")

# Add this route to your existing app.py
@app.route("/contact")
def contact():
    """Renders the contact page."""
    return render_template("contact.html")

@app.route("/about-us")
def about():
    """Renders the about us page."""
    return render_template("about.html")

@app.route("/pricing")
def pricing():
    """Renders the pricing page."""
    return render_template("pricing.html")

@app.route("/features")
def features():
    """Renders the features page."""
    return render_template("features.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
