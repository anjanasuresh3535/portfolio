# Anjana Suresh - Software Developer Portfolio

A recruiter-focused, responsive developer portfolio website for **Anjana Suresh**, an **MCA student** at **MACFAST, Thiruvalla** with a **B.Sc. Mathematics background** from **Catholicate College, Pathanamthitta**, seeking Software Development Internships and Campus Placements.

---

## 🌟 Key Highlights

- **Verified Profile & Credentials:**
  - **Email:** `anjanasuresh3535@gmail.com`
  - **Phone:** `+91 9946659118`
  - **Location:** Pathanamthitta, Kerala, India
  - **LinkedIn:** [linkedin.com/in/anjanasuresh7404](https://www.linkedin.com/in/anjanasuresh7404/)
  - **GitHub:** [github.com/anjanasuresh3535](https://github.com/anjanasuresh3535)
- **Flagship Project:** **AptitudePro** — Full-stack placement prep platform with 195 levels across 9 tiers, 5 sections, company tracks (TCS, Infosys, Wipro), MongoDB snapshot schema, and an in-browser SQL practice sandbox with `sql.js`.
- **Industry Experience:** Full Stack Development Intern at **Faith Infotech, Kerala** (Python, Django REST Framework, MySQL, Postman API testing).
- **Academic Distinction:**
  - **MCA (2025–2027), MACFAST, Thiruvalla** &bull; First Sem CGPA: **8.72/10** &bull; Second Sem CGPA: **8.39/10**
  - **B.Sc. in Mathematics (2022–2025), Catholicate College, Pathanamthitta**
- **Certification:** **Data Analytics with Python** — NPTEL SWAYAM
- **Zero Dependencies:** Pure HTML5, CSS3, and vanilla JavaScript. No npm install or complex setups required.

---

## 💻 How to Run This Portfolio

You have several easy options to preview and run your portfolio:

### Option 1: Just Double-Click `index.html` (Fastest)
1. Open the `anjana-portfolio` folder on your computer (`C:\Users\Brosis\Desktop\anjana-portfolio`).
2. Double-click on `index.html`.
3. It will open instantly in your default web browser (Chrome, Edge, Firefox, Safari).

---

### Option 2: Using Python's Built-in Server (Recommended)
This runs a local web server just like a live website:

1. Open PowerShell, Command Prompt, or Terminal inside this folder:
   ```powershell
   cd C:\Users\Brosis\Desktop\anjana-portfolio
   ```
2. Start the local server:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser and go to:
   ```
   http://localhost:8000
   ```
   *(To stop the server anytime, press `Ctrl + C` in the terminal).*

---

### Option 3: Using VS Code "Live Server"
1. Open the `anjana-portfolio` folder in **Visual Studio Code**.
2. If you don't have it yet, install the **Live Server** extension (by Ritwick Dey) from the Extensions tab (`Ctrl + Shift + X`).
3. Right-click on `index.html` in the file explorer and click **"Open with Live Server"**.
4. The site will open in your browser with automatic live reload on every save.

---

## 📁 Project Structure

```text
anjana-portfolio/
│
├── index.html                   # Main single-page portfolio (semantic HTML5)
├── style.css                    # Premium dark theme (deep violet & lavender accents)
├── script.js                    # Vanilla JS (navigation drawer, filter tabs, copy-email, mailto builder)
├── README.md                    # Setup, running & deployment instructions
│
├── assets/                      # Visual assets & project mockups
│   ├── favicon.svg              # Custom <AS/> monogram browser icon
│   ├── anjana-photo.jpg         # Profile photograph with neon violet aesthetic
│   └── project-aptitudepro.svg  # AptitudePro 9-tier platform & SQL console preview
│
└── resume/                      # Resume directory
    ├── Anjana_Suresh_Resume.pdf # Recruiter-ready PDF resume matching your credentials
    └── generate_resume.py       # Python script to regenerate the PDF
```

---

## 🚀 How to Publish for Free on GitHub Pages

You can host your portfolio for free on your GitHub account (`anjanasuresh3535`):

1. **Initialize Git & Commit:**
   ```bash
   git init
   git add .
   git commit -m "Launch Anjana Suresh developer portfolio"
   ```

2. **Create a GitHub Repository:**
   - Go to [github.com/new](https://github.com/new).
   - Create a repository named `anjanasuresh3535.github.io` (for a root personal domain) or `portfolio`.
   - Make it **Public**.

3. **Push your code to GitHub:**
   ```bash
   git branch -M main
   git remote add origin https://github.com/anjanasuresh3535/anjanasuresh3535.github.io.git
   git push -u origin main
   ```

4. **Turn on GitHub Pages:**
   - In your repository, click **Settings** (top tab) &rarr; **Pages** (left sidebar).
   - Under **Build and deployment > Source**, select **Deploy from a branch**.
   - Under **Branch**, select `main` and `/ (root)`, then click **Save**.
   - Within 1–2 minutes, your website will be live worldwide at:
     ```
     https://anjanasuresh3535.github.io/
     ```

---

## 📸 Adding Your Own Photo

To replace the avatar with your own real headshot photograph:
1. Copy your photo (e.g. `anjana-photo.jpg`) into the `assets/` folder.
2. In `index.html` (line ~168), change:
   ```html
   <img src="assets/profile-placeholder.svg" ...>
   ```
   to:
   ```html
   <img src="assets/anjana-photo.jpg" ...>
   ```

---

## 📄 License
Custom built for **Anjana Suresh**. Free to use, adapt, and customize for software development career opportunities.
