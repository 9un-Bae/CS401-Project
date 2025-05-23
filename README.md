# 🌺 Hunger Helpers Web App

**Hunger Helpers** is a community-driven web application built to uplift and support those facing food insecurity across Hawai‘i. 
This platform connects users with essential resources, volunteer opportunities, and ways to give back — all while highlighting the spirit of aloha and unity.

## 🌟 Project Goal

Our mission is to strengthen our local communities by making it easy to:
- **Find** nearby food assistance resources  
- **Register** to volunteer at local organizations  
- **Donate** directly to trusted nonprofits  
- **Learn** about who we are and why we care  

Whether you're in need or ready to help, Hunger Helpers bridges the gap between giving and receiving.

---

## 🏛️ Website Structure
- **Home**: A warm welcome message, showcasing the heart of the community  
- **About**: Our group mottos and bios of the team behind Hunger Helpers  
- **Resources**: Local organizations offering food assistance  
- **Volunteer**: Nonprofits you can serve with and a list of upcoming events  
- **Donate**: Direct donation links to impactful organizations  

---

## 🏃🏻‍♂️ How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hunger-helpers.git
   cd hunger-helpers
2. **Install Flask (if not already installed):**
   ```bash
   pip install Flask
3. **Build Docker Container for API**
   ```bash
   docker build -t <your-username>/<image-name>:<version> -f <dockerfile> .
4. **Run Docker Container**
   ```bash
   docker run --name "<flask-app-name>" -d -p 5000:5000 <your-username>/<image-name>:1.0
5. **Run Flask server:**
   ```bash
   flask --app app.py --debug run
6. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/index.html
   ```

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap, Font Awesome
- **Backend:** Python, Flask
- **Templating:** Jinja2
- **Version Control:** Git, GitHub

---

## 📄 Project Documentation

- 🎞️ [Presentation Slides (PPTX)](docs/Presentation.pptx)
- 📘 [Final Report (PDF)](docs/PDF%20Report.pdf)
- 🧩 [UML Class Diagram](docs/UML%20Class%20Diagram.png)

---

## 👥 Group Members

- Johnny Bae
- Lydia Hefel
- Upumoni Logologo



