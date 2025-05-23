from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


volunteer_data = {
    "organizations": [
        {
            "name": "Aloha Harvest",
            "website": "https://alohaharvest.org/",
            "image": "imgs/alohaharvest.png",
            "description": "Help rescue quality food and redistribute it to those in need across Oʻahu."
        },
        {
            "name": "Hawaii Meals on Wheels",
            "website": "https://hmow.org/",
            "image": "imgs/hmow.png",
            "description": "Deliver meals and build meaningful connections with kūpuna in your community."
        },
        {
            "name": "Hawaii Foodbank",
            "website": "https://hawaiifoodbank.org/",
            "image": "imgs/hawaiifoodbank.png",
            "description": "Sort, pack, or distribute food to fight hunger across the islands."
        },
        {
            "name": "The Pantry",
            "website": "https://thepantry.org/",
            "image": "imgs/thepantry.png",
            "description": "Support Hawaii’s first e-commerce food distribution center helping low-income families."
        },
        {
            "name": "Angel Network Charities",
            "website": "https://example.org/angel-network",
            "image": "imgs/angelnetwork.png",
            "description": "Provides food, clothing, and support to those in need."
        },
        {
            "name": "River of Life Mission",
            "website": "https://riveroflifemission.org",
            "image": "imgs/riveroflife.png",
            "description": "Helps those experiencing homelessness with meals and services."
        },
        {
            "name": "Giving Hope",
            "website": "https://example.org/giving-hope",
            "image": "imgs/givinghope.png",
            "description": "Inspires lives through faith-based community outreach programs."
        },
        {
            "name": "Aloha United Way",
            "website": "https://www.auw.org",
            "image": "imgs/auw.png",
            "description": "Supports Hawaii's local families through community partnerships."
        }
    ],
    "upcoming_events": {
        "Aloha Harvest": [
            {"date": "Apr 27", "title": "Kakaʻako Food Rescue Drive"},
            {"date": "May 5", "title": "Volunteer Orientation (Zoom)"},
            {"date": "May 18", "title": "Downtown Distribution Day"}
        ],
        "Hawaii Meals on Wheels": [
            {"date": "Apr 25", "title": "Waikīkī Meal Delivery Route"},
            {"date": "May 2", "title": "Kūpuna Caregiver Workshop"},
            {"date": "May 10", "title": "Mānoa Volunteer Meet-Up"}
        ],
        "Hawaii Foodbank": [
            {"date": "Apr 29", "title": "Community Food Sort Day"},
            {"date": "May 6", "title": "Food Drive at Ala Moana"},
            {"date": "May 20", "title": "Warehouse Support Shift"}
        ],
        "The Pantry": [
            {"date": "Apr 30", "title": "Volunteer Fulfillment Shift"},
            {"date": "May 8", "title": "Packing and Prep Session"},
            {"date": "May 15", "title": "Drive-Thru Distribution Event"}
        ],
        "Angel Network Charities": [
            {"date": "May 2", "title": "Drive-Thru Pantry Day"},
            {"date": "May 9", "title": "Volunteer Coordination Day"},
            {"date": "May 16", "title": "Community Clothing Drive"}
        ],
        "River of Life Mission": [
            {"date": "Apr 26", "title": "Mobile HUB Meal Outreach"},
            {"date": "May 3", "title": "Community Worship & Meal"},
            {"date": "May 17", "title": "40-Year Anniversary Celebration"}
        ],
        "Giving Hope": [
            {"date": "Apr 28", "title": "Hope Food Distribution"},
            {"date": "May 5", "title": "Charity Golf Tournament"},
            {"date": "May 12", "title": "Youth Mentorship Weekend"}
        ],
        "Aloha United Way": [
            {"date": "Apr 19", "title": "Chocolate, Champagne & Couture For-A-Cause"},
            {"date": "Aug 6", "title": "Workplace Giving Campaign Kickoff"},
            {"date": "Ongoing", "title": "Volunteer Opportunities Across O‘ahu"}
        ]
    }
}

resource_data = [
    {"name": "Aloha Harvest", "image": "img/AlohaHarvest.jpg", "url": "https://www.alohaharvest.org/", "description": "Aloha Harvest is a Hawaiʻi-based nonprofit that rescues quality excess food and delivers it free of charge to organizations feeding those in need."},
    {"name": "The Pantry", "image": "img/Pantry.png", "url": "https://www.thepantry.org/", "description": "The Pantry is a food distribution service by Feeding Hawaiʻi Together, offering a grocery-style experience where individuals and families can select free, nutritious food with dignity and care."},
    {"name": "Hawai'i Food Bank", "image": "img/FoodBank.jpg", "url": "https://hawaiifoodbank.org/", "description": "Hawai‘i Foodbank provides food assistance to families, keiki, and kūpuna across the islands, working with a network of partners to ensure no one in our community goes hungry."},
    {"name": "Angel Network Charities", "image": "imgs/angelnetwork.png", "url": "https://www.angelnetworkcharities.org/", "description": "Angel Network Charities provides food, basic necessities, and supportive services to individuals and families in need across O‘ahu, striving to uplift the community."},
    {"name": "River of Life Mission", "image": "imgs/riveroflife.png", "url": "https://www.riveroflifemission.org/", "description": "River of Life Mission provides meals, essentials, and hope to Honolulu’s houseless community, helping people move toward a brighter future."},
    {"name": "Giving Hope Hawai'i", "image": "images/GiveHopeLogo.png", "url": "https://www.givinghopehawaii.org/", "description": "Giving Hope Hawai‘i supports those in crisis by offering resources and services that restore dignity and inspire lasting change."},
    {"name": "Aloha United Way", "image": "imgs/auw.png", "url": "https://www.auw.org/", "description": "Aloha United Way connects people and resources to improve lives, supporting programs that build a stronger, healthier Hawai‘i."},
    {"name": "Hawai'i Meals on Wheels", "image": "imgs/hmow.png", "url": "https://hmow.org/", "description": "Hawai‘i Meals on Wheels delivers meals and care to homebound seniors, helping them stay nourished, independent, and connected."}
]

donate_data = [
{"name": "Aloha Harvest", "image": "img/AlohaHarvest.jpg", "url": "https://alohaharvest.org/donate-money/"},
    {"name": "The Pantry", "image": "img/Pantry.png", "url": "https://thepantry.app.neoncrm.com/forms/donation"},
    {"name": "Hawai'i Food Bank", "image": "img/FoodBank.jpg", "url": "https://hawaiifoodbank.org/?form=FUNLSDJGUQN"},
    {"name": "Angel Network Charities", "image": "imgs/angelnetwork.png", "url": "https://www.angelnetworkcharities.org/blank-page"},
    {"name": "River of Life Mission", "image": "imgs/riveroflife.png", "url": "https://www.riveroflifemission.org/?form=donate"},
    {"name": "Giving Hope Hawai'i", "image": "images/GiveHopeLogo.png", "url": "https://givinghopenola.org/donate/"},
    {"name": "Aloha United Way", "image": "imgs/auw.png", "url": "https://www.auw.org/donate/"},
    {"name": "Hawai'i Meals on Wheels", "image": "imgs/hmow.png", "url": "https://hmow.org/donate/"}
]

@app.route('/resource_data', methods=['GET'])
def get_resources():
    return resource_data

@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/donate.html', methods=['POST', 'GET'])
def donate():
    return render_template('donate.html', data = donate_data)

@app.route('/volunteer.html')
def volunteer():
    return render_template(
        "volunteer.html",
        organizations=volunteer_data["organizations"],
        upcoming_events=volunteer_data["upcoming_events"]
    )


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get("name")
    org_name = data.get("organization")

    for org in volunteer_data["organizations"]:
        if org["name"] == org_name:
            if "members" not in org:
                org["members"] = []
            org["members"].append(name)
            return jsonify({"message": f"{name} added to {org_name}"}), 201

    return jsonify({"error": "Organization not found"}), 404

@app.route('/remove_member', methods=['DELETE'])
def remove_member():
    data = request.get_json()
    name = data.get("name")
    org_name = data.get("organization")

    for org in volunteer_data["organizations"]:
        if org["name"] == org_name:
            if "members" in org and name in org["members"]:
                org["members"].remove(name)
                return jsonify({"message": f"{name} removed from {org_name}"}), 200
            return jsonify({"error": "Member not found"}), 404

    return jsonify({"error": "Organization not found"}), 404

@app.route('/resource.html', methods=['GET'])
def resource():
    return render_template('resource.html', data = resource_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')