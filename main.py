from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

def get_response(user):
    user = user.lower().strip()
    words = user.split()

    if any(x in words for x in ["hi", "hello", "hey"]):
        return "Hello! Welcome to SmartStay."
    
    if "city" in user or "cities" in user or "location" in user:
        return "We currently support hotels in Delhi, Mumbai and Pune."

    if "delhi" in user:
        return "Hotels available in Delhi near Airport and Connaught Place."

    if "mumbai" in user:
        return "Hotels available in Mumbai near CST and Airport."

    if "pune" in user:
        return "Hotels available in Pune near Hinjewadi."

    if "room" in user:
        return "We offer Single, Double, Suite and Family rooms."

    if "single" in user:
        return "Single room starts at ₹2000 per night."

    if "double" in user:
        return "Double room starts at ₹5000 per night."

    if "suite" in user:
        return "Suite costs around ₹10000 per night."

    if "family" in user:
        return "Family room costs around ₹6000 per night."

    if "book" in user or "reserve" in user:
        return "You can fill the booking form above to reserve your stay."

    if "price" in user or "cost" in user:
        return "Rooms range from ₹2000 to ₹10000."

    if "facility" in user or "amenities" in user:
        return "Facilities include WiFi, Gym, Pool and Parking."

    if "payment" in user:
        return "We accept UPI, Debit/Credit Cards and Net Banking."

    if "cancel" in user:
        return "Free cancellation up to 24 hours before check-in."

    if "time" in user or "check" in user:
        return "Check-in at 2 PM and check-out at 11 AM."

    if "bye" in user:
        return "Goodbye! Have a great day."

    return "Please ask about rooms, cities, or booking."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    return jsonify({"response": get_response(msg)})

if __name__ == "__main__":
    app.run(debug=True)