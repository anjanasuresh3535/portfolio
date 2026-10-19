import os

assets_dir = r"c:\Users\Brosis\Desktop\anjana-portfolio\assets"

# AptitudePro SVG Preview
aptitudepro_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="apBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#120c29"/>
      <stop offset="100%" stop-color="#0a0618"/>
    </linearGradient>
    <linearGradient id="tierGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="barApt" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>
  
  <rect width="800" height="480" fill="url(#apBg)"/>
  
  <!-- Window Header -->
  <rect x="0" y="0" width="800" height="42" fill="#181135"/>
  <circle cx="24" cy="21" r="5.5" fill="#ef4444" opacity="0.85"/>
  <circle cx="42" cy="21" r="5.5" fill="#f59e0b" opacity="0.85"/>
  <circle cx="60" cy="21" r="5.5" fill="#10b981" opacity="0.85"/>
  <rect x="180" y="9" width="440" height="24" rx="12" fill="#0d081e"/>
  <text x="400" y="25" font-family="'JetBrains Mono', monospace" font-size="11" fill="#cbd5e1" text-anchor="middle">aptitudepro.anjana.dev/practice/tier-9</text>
  
  <!-- Left Sidebar: Tiers & Sections -->
  <rect x="0" y="42" width="200" height="438" fill="#100b25"/>
  <text x="24" y="76" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="800" fill="#f8fafc">AptitudePro</text>
  <rect x="120" y="62" width="60" height="20" rx="10" fill="#a855f7" fill-opacity="0.2"/>
  <text x="150" y="76" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#c084fc" text-anchor="middle">v2.4</text>
  
  <!-- Tier Badge -->
  <rect x="18" y="98" width="164" height="48" rx="8" fill="#1b123d" stroke="#3b2575" stroke-width="1"/>
  <text x="30" y="118" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#94a3b8">CURRENT PROGRESS</text>
  <text x="30" y="136" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" fill="#38bdf8">Tier 9 • 195 Levels</text>
  
  <!-- Section Tabs -->
  <text x="24" y="174" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" letter-spacing="1">SECTIONS</text>
  
  <rect x="14" y="186" width="172" height="30" rx="6" fill="#24164e"/>
  <text x="26" y="206" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#e9d5ff">📐 Quantitative Maths</text>
  
  <text x="26" y="238" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">🧩 Logical Reasoning</text>
  <text x="26" y="268" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">📖 Verbal English</text>
  <text x="26" y="298" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">💻 Programming (Java/Py)</text>
  <text x="26" y="328" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">🎲 Mixed Speed Test</text>
  
  <!-- Company Specific Tracks -->
  <text x="24" y="366" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" letter-spacing="1">COMPANY TRACKS</text>
  <g transform="translate(18, 380)">
    <rect x="0" y="0" width="48" height="24" rx="4" fill="#1b143c"/>
    <text x="24" y="16" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="600" fill="#f8fafc" text-anchor="middle">TCS</text>
    <rect x="56" y="0" width="54" height="24" rx="4" fill="#1b143c"/>
    <text x="83" y="16" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="600" fill="#f8fafc" text-anchor="middle">INFOSYS</text>
    <rect x="118" y="0" width="50" height="24" rx="4" fill="#1b143c"/>
    <text x="143" y="16" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="600" fill="#f8fafc" text-anchor="middle">WIPRO</text>
  </g>
  
  <!-- Main Dashboard Area -->
  <g transform="translate(220, 60)">
    <!-- Top Stat Row -->
    <rect x="0" y="0" width="170" height="72" rx="10" fill="#171038" stroke="#2e1d5e" stroke-width="1"/>
    <text x="16" y="26" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">Total XP Earned</text>
    <text x="16" y="54" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="800" fill="#f8fafc">4,850 XP</text>
    
    <rect x="185" y="0" width="180" height="72" rx="10" fill="#171038" stroke="#2e1d5e" stroke-width="1"/>
    <text x="201" y="26" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">Accuracy Rate</text>
    <text x="201" y="54" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="800" fill="#10b981">92.4%</text>
    
    <rect x="380" y="0" width="175" height="72" rx="10" fill="#171038" stroke="#2e1d5e" stroke-width="1"/>
    <text x="396" y="26" font-family="'Inter', sans-serif" font-size="11" fill="#94a3b8">Avg Time / Question</text>
    <text x="396" y="54" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="800" fill="#c084fc">42s</text>
    
    <!-- Active Quiz Card -->
    <rect x="0" y="88" width="555" height="180" rx="10" fill="#150f33" stroke="#2d1c5a" stroke-width="1"/>
    <text x="20" y="116" font-family="'JetBrains Mono', monospace" font-size="11" fill="#38bdf8">QUESTION 14 / 20 • MATHEMATICAL REASONING</text>
    <text x="20" y="142" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="600" fill="#f8fafc">A train travels at 72 km/h and crosses a 260m platform in 23 seconds. Find the length of the train?</text>
    
    <!-- Answer Options -->
    <rect x="20" y="162" width="245" height="34" rx="6" fill="#1c1440" stroke="#3d2778" stroke-width="1"/>
    <text x="34" y="184" font-family="'Inter', sans-serif" font-size="12" fill="#cbd5e1">A. 180 meters</text>
    
    <rect x="280" y="162" width="245" height="34" rx="6" fill="#1c1440" stroke="#10b981" stroke-width="1.5"/>
    <text x="294" y="184" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#34d399">B. 200 meters (Correct ✓)</text>
    
    <rect x="20" y="206" width="245" height="34" rx="6" fill="#1c1440" stroke="#3d2778" stroke-width="1"/>
    <text x="34" y="228" font-family="'Inter', sans-serif" font-size="12" fill="#cbd5e1">C. 220 meters</text>
    
    <rect x="280" y="206" width="245" height="34" rx="6" fill="#1c1440" stroke="#3d2778" stroke-width="1"/>
    <text x="294" y="228" font-family="'Inter', sans-serif" font-size="12" fill="#cbd5e1">D. 240 meters</text>
    
    <!-- In-browser SQL Console Panel (Powered by sql.js) -->
    <rect x="0" y="280" width="555" height="125" rx="10" fill="#0d081f" stroke="#2a1a54" stroke-width="1"/>
    <rect x="0" y="280" width="555" height="28" rx="10" fill="#171035"/>
    <text x="20" y="299" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#c084fc">⚡ IN-BROWSER SQL PRACTICE CONSOLE (sql.js)</text>
    <text x="470" y="299" font-family="'JetBrains Mono', monospace" font-size="10" fill="#10b981">● SQLite Ready</text>
    
    <text x="20" y="330" font-family="'JetBrains Mono', monospace" font-size="11" fill="#cbd5e1"><tspan fill="#a855f7">SELECT</tspan> candidate_id, score, rank() <tspan fill="#a855f7">OVER</tspan> (<tspan fill="#a855f7">ORDER BY</tspan> score <tspan fill="#a855f7">DESC</tspan>) <tspan fill="#a855f7">FROM</tspan> results;</text>
    <text x="20" y="352" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">-- Output: 14 rows returned in 2.4ms (Indexed)</text>
    <rect x="20" y="364" width="70" height="22" rx="4" fill="#a855f7" fill-opacity="0.3"/>
    <text x="32" y="379" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#d8b4fe">▶ Run SQL</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-aptitudepro.svg"), "w", encoding="utf-8") as f:
    f.write(aptitudepro_svg)

# Faith Infotech Internship REST API Mockup
django_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="djBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f0c24"/>
      <stop offset="100%" stop-color="#080616"/>
    </linearGradient>
  </defs>
  
  <rect width="800" height="480" fill="url(#djBg)"/>
  
  <!-- Window Header -->
  <rect x="0" y="0" width="800" height="42" fill="#181135"/>
  <circle cx="24" cy="21" r="5.5" fill="#ef4444" opacity="0.85"/>
  <circle cx="42" cy="21" r="5.5" fill="#f59e0b" opacity="0.85"/>
  <circle cx="60" cy="21" r="5.5" fill="#10b981" opacity="0.85"/>
  <rect x="180" y="9" width="440" height="24" rx="12" fill="#0d081e"/>
  <text x="400" y="25" font-family="'JetBrains Mono', monospace" font-size="11" fill="#cbd5e1" text-anchor="middle">api.faithinfotech.internal/v1/endpoints</text>
  
  <!-- Left Postman Style Collections -->
  <rect x="0" y="42" width="220" height="438" fill="#110d29"/>
  <text x="24" y="76" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#f8fafc">Django REST Services</text>
  
  <g transform="translate(16, 95)">
    <rect x="0" y="0" width="188" height="34" rx="6" fill="#1b143c"/>
    <rect x="8" y="8" width="40" height="18" rx="4" fill="#10b981" fill-opacity="0.2"/>
    <text x="18" y="21" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#34d399">GET</text>
    <text x="56" y="21" font-family="'Inter', sans-serif" font-size="11" fill="#f8fafc">/api/v1/modules/</text>
    
    <rect x="0" y="42" width="188" height="34" rx="6" fill="#1b143c"/>
    <rect x="8" y="50" width="45" height="18" rx="4" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="14" y="63" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#38bdf8">POST</text>
    <text x="60" y="63" font-family="'Inter', sans-serif" font-size="11" fill="#f8fafc">/api/v1/records/</text>
    
    <rect x="0" y="84" width="188" height="34" rx="6" fill="#1b143c"/>
    <rect x="8" y="92" width="40" height="18" rx="4" fill="#f59e0b" fill-opacity="0.2"/>
    <text x="18" y="105" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#fbbf24">PUT</text>
    <text x="56" y="105" font-family="'Inter', sans-serif" font-size="11" fill="#f8fafc">/api/v1/data/42/</text>
  </g>
  
  <text x="24" y="260" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" letter-spacing="1">INTERNSHIP SCOPE</text>
  <text x="24" y="285" font-family="'Inter', sans-serif" font-size="11" fill="#cbd5e1">• Faith Infotech, Kerala</text>
  <text x="24" y="310" font-family="'Inter', sans-serif" font-size="11" fill="#cbd5e1">• Python &amp; Django REST</text>
  <text x="24" y="335" font-family="'Inter', sans-serif" font-size="11" fill="#cbd5e1">• MySQL Schema Design</text>
  <text x="24" y="360" font-family="'Inter', sans-serif" font-size="11" fill="#cbd5e1">• Postman Verification</text>
  
  <!-- Right API Response Body -->
  <g transform="translate(240, 65)">
    <!-- Endpoint bar -->
    <rect x="0" y="0" width="535" height="42" rx="8" fill="#150f33" stroke="#2d1c58" stroke-width="1"/>
    <rect x="12" y="10" width="48" height="22" rx="4" fill="#10b981" fill-opacity="0.25"/>
    <text x="23" y="25" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#10b981">GET</text>
    <text x="70" y="26" font-family="'JetBrains Mono', monospace" font-size="12" fill="#f8fafc">https://api.faithinfotech.internal/v1/modules/verify</text>
    <rect x="460" y="10" width="60" height="22" rx="4" fill="#a855f7" fill-opacity="0.3"/>
    <text x="475" y="25" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#c084fc">200 OK</text>
    
    <!-- JSON Response Container -->
    <rect x="0" y="55" width="535" height="340" rx="8" fill="#0c081d" stroke="#221544" stroke-width="1"/>
    <text x="20" y="85" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748b">// Response Payload (Django REST Framework Serializer)</text>
    <text x="20" y="110" font-family="'JetBrains Mono', monospace" font-size="11" fill="#f8fafc">{</text>
    <text x="40" y="132" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">"status": <tspan fill="#34d399">"success"</tspan>,</text>
    <text x="40" y="154" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">"internship_role": <tspan fill="#38bdf8">"Full Stack Development Intern"</tspan>,</text>
    <text x="40" y="176" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">"organization": <tspan fill="#f8fafc">"Faith Infotech, Kerala"</tspan>,</text>
    <text x="40" y="198" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">"technologies": [</text>
    <text x="60" y="220" font-family="'JetBrains Mono', monospace" font-size="11" fill="#cbd5e1">"Python", "Django REST Framework", "MySQL", "REST APIs", "Postman"</text>
    <text x="40" y="242" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">],</text>
    <text x="40" y="264" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">"verified_endpoints": <tspan fill="#f59e0b">true</tspan>,</text>
    <text x="40" y="286" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">"request_time_ms": <tspan fill="#38bdf8">14.2</tspan></text>
    <text x="20" y="310" font-family="'JetBrains Mono', monospace" font-size="11" fill="#f8fafc">}</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-django-api.svg"), "w", encoding="utf-8") as f:
    f.write(django_svg)

print("Project SVGs updated!")
