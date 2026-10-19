import os

assets_dir = r"c:\Users\Brosis\Desktop\anjana-portfolio\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. Favicon SVG
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <rect width="64" height="64" rx="16" fill="#0c0919"/>
  <rect x="2" y="2" width="60" height="60" rx="14" fill="none" stroke="url(#grad)" stroke-width="2" stroke-opacity="0.6"/>
  <!-- AS Monogram -->
  <text x="32" y="42" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="26" font-weight="800" fill="url(#grad)" text-anchor="middle" filter="url(#glow)">AS</text>
  <!-- Tiny math/code dot -->
  <circle cx="49" cy="22" r="3" fill="#38bdf8"/>
</svg>'''

with open(os.path.join(assets_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# 2. Profile Photo Placeholder (High-end developer avatar with math & code aura)
profile_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="bgGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#3b1d6e" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#140f2d" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0a0715" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  
  <!-- Outer circle background -->
  <circle cx="250" cy="250" r="230" fill="url(#bgGlow)"/>
  <circle cx="250" cy="250" r="230" fill="none" stroke="url(#borderGrad)" stroke-width="4" stroke-dasharray="12 8" opacity="0.6"/>
  <circle cx="250" cy="250" r="215" fill="none" stroke="#a855f7" stroke-width="1.5" opacity="0.3"/>
  
  <!-- Subtle Math & Code ambient symbols in background -->
  <g opacity="0.18" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="20">
    <text x="70" y="140">∫ f(x)dx</text>
    <text x="360" y="150">&lt;code/&gt;</text>
    <text x="80" y="360">O(log n)</text>
    <text x="350" y="350">λ → f(λ)</text>
    <text x="220" y="80">∑ n²</text>
  </g>
  
  <!-- Professional Silhouette / Stylized Avatar representation -->
  <g id="avatarFigure">
    <!-- Glow behind head -->
    <circle cx="250" cy="205" r="90" fill="#a855f7" opacity="0.25" filter="url(#softGlow)"/>
    
    <!-- Torso / Blazer silhouette -->
    <path d="M 120 440 C 130 350, 180 300, 250 300 C 320 300, 370 350, 380 440 Z" fill="#1e183a" stroke="#818cf8" stroke-width="2"/>
    <path d="M 210 320 L 250 380 L 290 320" fill="none" stroke="#c084fc" stroke-width="2.5"/>
    <polygon points="250,340 230,300 270,300" fill="#a855f7" opacity="0.7"/>
    
    <!-- Neck -->
    <rect x="232" y="260" width="36" height="45" rx="6" fill="#e2d8f0"/>
    
    <!-- Face oval -->
    <ellipse cx="250" cy="205" rx="65" ry="75" fill="#f1e9fb"/>
    
    <!-- Sleek professional hairstyle -->
    <path d="M 175 200 C 170 130, 210 110, 250 110 C 290 110, 330 130, 325 200 C 315 160, 285 140, 250 140 C 215 140, 185 160, 175 200 Z" fill="#2d1c4d"/>
    <path d="M 175 200 C 170 230, 180 270, 195 285 C 190 260, 185 230, 185 200 Z" fill="#2d1c4d"/>
    <path d="M 325 200 C 330 230, 320 270, 305 285 C 310 260, 315 230, 315 200 Z" fill="#2d1c4d"/>
    
    <!-- Professional Glasses -->
    <rect x="200" y="195" width="40" height="26" rx="6" fill="none" stroke="#6366f1" stroke-width="3"/>
    <rect x="260" y="195" width="40" height="26" rx="6" fill="none" stroke="#6366f1" stroke-width="3"/>
    <line x1="240" y1="208" x2="260" y2="208" stroke="#6366f1" stroke-width="3"/>
    <line x1="185" y1="205" x2="200" y2="205" stroke="#6366f1" stroke-width="2.5"/>
    <line x1="300" y1="205" x2="315" y2="205" stroke="#6366f1" stroke-width="2.5"/>
    
    <!-- Gentle friendly smile -->
    <path d="M 235 245 Q 250 256 265 245" fill="none" stroke="#6b21a8" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  
  <!-- Subtle Badge overlay at bottom -->
  <g transform="translate(145, 420)">
    <rect width="210" height="42" rx="21" fill="#0f0b21" stroke="url(#borderGrad)" stroke-width="2"/>
    <circle cx="25" cy="21" r="5" fill="#10b981"/>
    <text x="42" y="26" font-family="'Plus Jakarta Sans', system-ui, sans-serif" font-size="13" font-weight="600" fill="#f8fafc">Anjana Suresh</text>
    <text x="145" y="26" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="500" fill="#a78bfa">MCA '26</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "profile-placeholder.svg"), "w", encoding="utf-8") as f:
    f.write(profile_svg)

# 3. Project 1 Screenshot Mockup: Algorithmic Graph & Math Visualizer
proj1_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="p1bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110d24"/>
      <stop offset="100%" stop-color="#0a0716"/>
    </linearGradient>
    <linearGradient id="p1line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="50%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>
  
  <rect width="800" height="480" fill="url(#p1bg)"/>
  
  <!-- Window Header -->
  <rect x="0" y="0" width="800" height="44" fill="#171233"/>
  <circle cx="26" cy="22" r="6" fill="#ef4444" opacity="0.8"/>
  <circle cx="46" cy="22" r="6" fill="#f59e0b" opacity="0.8"/>
  <circle cx="66" cy="22" r="6" fill="#10b981" opacity="0.8"/>
  <rect x="180" y="10" width="440" height="24" rx="12" fill="#0c091a"/>
  <text x="400" y="26" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8" text-anchor="middle">math-algo-visualizer.anjana.dev</text>
  
  <!-- Grid overlay -->
  <g opacity="0.08" stroke="#c084fc" stroke-width="1">
    <line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="160" x2="800" y2="160"/>
    <line x1="0" y1="220" x2="800" y2="220"/>
    <line x1="0" y1="280" x2="800" y2="280"/>
    <line x1="0" y1="340" x2="800" y2="340"/>
    <line x1="0" y1="400" x2="800" y2="400"/>
    
    <line x1="120" y1="44" x2="120" y2="480"/>
    <line x1="240" y1="44" x2="240" y2="480"/>
    <line x1="360" y1="44" x2="360" y2="480"/>
    <line x1="480" y1="44" x2="480" y2="480"/>
    <line x1="600" y1="44" x2="600" y2="480"/>
    <line x1="720" y1="44" x2="720" y2="480"/>
  </g>
  
  <!-- Left panel: Algorithm Control -->
  <rect x="24" y="68" width="220" height="388" rx="10" fill="#161130" stroke="#2d2358" stroke-width="1.5"/>
  <text x="44" y="104" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#f8fafc">Graph Traversal</text>
  <rect x="44" y="122" width="180" height="28" rx="6" fill="#241a4a"/>
  <text x="56" y="141" font-family="'JetBrains Mono', monospace" font-size="11" fill="#c084fc">▶ Dijkstra / BFS / DFS</text>
  
  <!-- Stat boxes -->
  <rect x="44" y="170" width="85" height="52" rx="6" fill="#1b143c"/>
  <text x="54" y="190" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8">Vertices</text>
  <text x="54" y="212" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="700" fill="#f8fafc">18 Nodes</text>
  
  <rect x="139" y="170" width="85" height="52" rx="6" fill="#1b143c"/>
  <text x="149" y="190" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8">Complexity</text>
  <text x="149" y="212" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#38bdf8">O(V + E)</text>
  
  <!-- Mini code block -->
  <rect x="44" y="240" width="180" height="196" rx="6" fill="#0d0a1c"/>
  <text x="54" y="265" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b">// Shortest Path Algorithm</text>
  <text x="54" y="285" font-family="'JetBrains Mono', monospace" font-size="10" fill="#a78bfa">function dijkstra(graph, s) {</text>
  <text x="64" y="305" font-family="'JetBrains Mono', monospace" font-size="10" fill="#cbd5e1">  dist[s] = 0;</text>
  <text x="64" y="325" font-family="'JetBrains Mono', monospace" font-size="10" fill="#cbd5e1">  pq.enqueue(s, 0);</text>
  <text x="64" y="345" font-family="'JetBrains Mono', monospace" font-size="10" fill="#38bdf8">  while(!pq.isEmpty()) {</text>
  <text x="74" y="365" font-family="'JetBrains Mono', monospace" font-size="10" fill="#cbd5e1">    let u = pq.dequeue();</text>
  <text x="54" y="385" font-family="'JetBrains Mono', monospace" font-size="10" fill="#a78bfa">  }</text>
  <text x="54" y="405" font-family="'JetBrains Mono', monospace" font-size="10" fill="#10b981">  return shortestPaths;</text>
  
  <!-- Right Graph Canvas -->
  <rect x="264" y="68" width="512" height="388" rx="10" fill="#130e28" stroke="#2d2358" stroke-width="1.5"/>
  
  <!-- Network Edges -->
  <g stroke="#3f3370" stroke-width="2.5" opacity="0.8">
    <line x1="330" y1="160" x2="450" y2="120"/>
    <line x1="450" y1="120" x2="600" y2="140"/>
    <line x1="600" y1="140" x2="700" y2="240"/>
    <line x1="330" y1="160" x2="380" y2="280"/>
    <line x1="380" y1="280" x2="520" y2="260"/>
    <line x1="520" y1="260" x2="600" y2="140"/>
    <line x1="520" y1="260" x2="640" y2="380"/>
    <line x1="380" y1="280" x2="480" y2="400"/>
    <line x1="480" y1="400" x2="640" y2="380"/>
    <line x1="640" y1="380" x2="700" y2="240"/>
  </g>
  
  <!-- Highlighted Shortest Path -->
  <g stroke="url(#p1line)" stroke-width="4.5">
    <line x1="330" y1="160" x2="450" y2="120"/>
    <line x1="450" y1="120" x2="520" y2="260"/>
    <line x1="520" y1="260" x2="700" y2="240"/>
  </g>
  
  <!-- Graph Nodes -->
  <g>
    <!-- Node A (Source) -->
    <circle cx="330" cy="160" r="22" fill="#8b5cf6" stroke="#c084fc" stroke-width="3"/>
    <text x="330" y="165" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">A</text>
    <rect x="305" y="118" width="50" height="20" rx="4" fill="#0d0a1c" stroke="#8b5cf6" stroke-width="1"/>
    <text x="330" y="132" font-family="'Inter', sans-serif" font-size="10" fill="#d8b4fe" text-anchor="middle">Cost: 0</text>
    
    <!-- Node B -->
    <circle cx="450" cy="120" r="20" fill="#6366f1" stroke="#818cf8" stroke-width="2.5"/>
    <text x="450" y="125" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">B</text>
    <rect x="425" y="78" width="50" height="20" rx="4" fill="#0d0a1c" stroke="#6366f1" stroke-width="1"/>
    <text x="450" y="92" font-family="'Inter', sans-serif" font-size="10" fill="#a5b4fc" text-anchor="middle">Cost: 4</text>
    
    <!-- Node C -->
    <circle cx="600" cy="140" r="18" fill="#1e183a" stroke="#818cf8" stroke-width="2"/>
    <text x="600" y="145" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#cbd5e1" text-anchor="middle">C</text>
    
    <!-- Node D -->
    <circle cx="380" cy="280" r="18" fill="#1e183a" stroke="#818cf8" stroke-width="2"/>
    <text x="380" y="285" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#cbd5e1" text-anchor="middle">D</text>
    
    <!-- Node E -->
    <circle cx="520" cy="260" r="21" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
    <text x="520" y="265" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">E</text>
    <rect x="495" y="295" width="50" height="20" rx="4" fill="#0d0a1c" stroke="#38bdf8" stroke-width="1"/>
    <text x="520" y="309" font-family="'Inter', sans-serif" font-size="10" fill="#7dd3fc" text-anchor="middle">Cost: 7</text>
    
    <!-- Node F (Target) -->
    <circle cx="700" cy="240" r="23" fill="#10b981" stroke="#34d399" stroke-width="3"/>
    <text x="700" y="245" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">Z</text>
    <rect x="670" y="196" width="60" height="22" rx="4" fill="#0d0a1c" stroke="#10b981" stroke-width="1"/>
    <text x="700" y="211" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#6ee7b7" text-anchor="middle">Target: 9</text>
    
    <!-- Node G -->
    <circle cx="480" cy="400" r="18" fill="#1e183a" stroke="#818cf8" stroke-width="2"/>
    <text x="480" y="405" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#cbd5e1" text-anchor="middle">G</text>
    
    <!-- Node H -->
    <circle cx="640" cy="380" r="18" fill="#1e183a" stroke="#818cf8" stroke-width="2"/>
    <text x="640" y="385" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#cbd5e1" text-anchor="middle">H</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-1.svg"), "w", encoding="utf-8") as f:
    f.write(proj1_svg)

# 4. Project 2 Screenshot Mockup: Full-Stack Task & Project Management (DevFlow)
proj2_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="p2bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f0b24"/>
      <stop offset="100%" stop-color="#090615"/>
    </linearGradient>
  </defs>
  
  <rect width="800" height="480" fill="url(#p2bg)"/>
  
  <!-- Window Header -->
  <rect x="0" y="0" width="800" height="44" fill="#171233"/>
  <circle cx="26" cy="22" r="6" fill="#ef4444" opacity="0.8"/>
  <circle cx="46" cy="22" r="6" fill="#f59e0b" opacity="0.8"/>
  <circle cx="66" cy="22" r="6" fill="#10b981" opacity="0.8"/>
  <rect x="180" y="10" width="440" height="24" rx="12" fill="#0c091a"/>
  <text x="400" y="26" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8" text-anchor="middle">devflow-app.anjana.dev/kanban</text>
  
  <!-- Sidebar -->
  <rect x="0" y="44" width="180" height="436" fill="#120d29"/>
  <text x="24" y="80" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="800" fill="#f8fafc">DevFlow</text>
  
  <rect x="16" y="105" width="148" height="34" rx="8" fill="#241a4a"/>
  <text x="32" y="127" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#d8b4fe">📊 Sprint Board</text>
  
  <text x="32" y="165" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">📁 Repositories</text>
  <text x="32" y="200" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">⚡ API Integrations</text>
  <text x="32" y="235" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">👥 Team Roles</text>
  <text x="32" y="270" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">⚙ Settings</text>
  
  <!-- Main Content Board -->
  <!-- Column 1: Backlog -->
  <rect x="204" y="68" width="175" height="388" rx="8" fill="#15102f" stroke="#261d4a" stroke-width="1"/>
  <rect x="216" y="82" width="10" height="10" rx="3" fill="#a78bfa"/>
  <text x="234" y="92" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" fill="#e2e8f0">Backlog (3)</text>
  
  <!-- Card 1 -->
  <rect x="216" y="112" width="151" height="90" rx="6" fill="#1e173e" stroke="#332463" stroke-width="1"/>
  <text x="226" y="132" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">OAuth2 / JWT Auth</text>
  <text x="226" y="152" font-family="'Inter', sans-serif" font-size="9.5" fill="#94a3b8">Role-based permission middleware</text>
  <rect x="226" y="168" width="45" height="18" rx="4" fill="#a855f7" fill-opacity="0.2"/>
  <text x="234" y="180" font-family="'JetBrains Mono', monospace" font-size="9" fill="#c084fc">Auth</text>
  
  <!-- Card 2 -->
  <rect x="216" y="214" width="151" height="85" rx="6" fill="#1e173e" stroke="#332463" stroke-width="1"/>
  <text x="226" y="234" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">Database Schema</text>
  <text x="226" y="254" font-family="'Inter', sans-serif" font-size="9.5" fill="#94a3b8">PostgreSQL indexing</text>
  <rect x="226" y="268" width="60" height="18" rx="4" fill="#38bdf8" fill-opacity="0.2"/>
  <text x="233" y="280" font-family="'JetBrains Mono', monospace" font-size="9" fill="#38bdf8">Postgres</text>
  
  <!-- Column 2: In Progress -->
  <rect x="395" y="68" width="185" height="388" rx="8" fill="#15102f" stroke="#261d4a" stroke-width="1"/>
  <rect x="407" y="82" width="10" height="10" rx="3" fill="#38bdf8"/>
  <text x="425" y="92" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" fill="#e2e8f0">In Progress (2)</text>
  
  <!-- Card 3 -->
  <rect x="407" y="112" width="161" height="110" rx="6" fill="#1e173e" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="419" y="132" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">RESTful API Endpoints</text>
  <text x="419" y="152" font-family="'Inter', sans-serif" font-size="9.5" fill="#94a3b8">CRUD controllers &amp; request validation handlers</text>
  <rect x="419" y="184" width="55" height="18" rx="4" fill="#6366f1" fill-opacity="0.25"/>
  <text x="427" y="196" font-family="'JetBrains Mono', monospace" font-size="9" fill="#818cf8">Express</text>
  <rect x="480" y="184" width="40" height="18" rx="4" fill="#10b981" fill-opacity="0.25"/>
  <text x="488" y="196" font-family="'JetBrains Mono', monospace" font-size="9" fill="#34d399">Jest</text>
  
  <!-- Column 3: Completed / Tested -->
  <rect x="596" y="68" width="180" height="388" rx="8" fill="#15102f" stroke="#261d4a" stroke-width="1"/>
  <rect x="608" y="82" width="10" height="10" rx="3" fill="#10b981"/>
  <text x="626" y="92" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" fill="#e2e8f0">Completed (4)</text>
  
  <!-- Card 4 -->
  <rect x="608" y="112" width="156" height="85" rx="6" fill="#1a1438" stroke="#10b981" stroke-width="1"/>
  <text x="618" y="132" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">Responsive UI Layout</text>
  <text x="618" y="152" font-family="'Inter', sans-serif" font-size="9.5" fill="#94a3b8">Tailwind / CSS Grid</text>
  <rect x="618" y="166" width="60" height="18" rx="4" fill="#10b981" fill-opacity="0.2"/>
  <text x="628" y="178" font-family="'JetBrains Mono', monospace" font-size="9" fill="#10b981">✓ Passed</text>
</svg>'''

with open(os.path.join(assets_dir, "project-2.svg"), "w", encoding="utf-8") as f:
    f.write(proj2_svg)

# 5. Project 3 Screenshot Mockup: CampusPlacement & Recruiter Matching Platform
proj3_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <defs>
    <linearGradient id="p3bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0a22"/>
      <stop offset="100%" stop-color="#080614"/>
    </linearGradient>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#6366f1"/>
    </linearGradient>
  </defs>
  
  <rect width="800" height="480" fill="url(#p3bg)"/>
  
  <!-- Window Header -->
  <rect x="0" y="0" width="800" height="44" fill="#171233"/>
  <circle cx="26" cy="22" r="6" fill="#ef4444" opacity="0.8"/>
  <circle cx="46" cy="22" r="6" fill="#f59e0b" opacity="0.8"/>
  <circle cx="66" cy="22" r="6" fill="#10b981" opacity="0.8"/>
  <rect x="180" y="10" width="440" height="24" rx="12" fill="#0c091a"/>
  <text x="400" y="26" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8" text-anchor="middle">talent-match.anjana.dev/analytics</text>
  
  <!-- Top Stat Cards -->
  <g transform="translate(30, 64)">
    <rect x="0" y="0" width="230" height="84" rx="10" fill="#150f33" stroke="#2c205c" stroke-width="1.5"/>
    <text x="20" y="30" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">Screened Candidates</text>
    <text x="20" y="62" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800" fill="#f8fafc">1,248</text>
    <text x="140" y="60" font-family="'Inter', sans-serif" font-size="11" fill="#10b981">+18.4%</text>
    
    <rect x="255" y="0" width="230" height="84" rx="10" fill="#150f33" stroke="#2c205c" stroke-width="1.5"/>
    <text x="275" y="30" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">Skill Match Score</text>
    <text x="275" y="62" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800" fill="#c084fc">94.2%</text>
    <text x="390" y="60" font-family="'JetBrains Mono', monospace" font-size="11" fill="#38bdf8">Top Tier</text>
    
    <rect x="510" y="0" width="230" height="84" rx="10" fill="#150f33" stroke="#2c205c" stroke-width="1.5"/>
    <text x="530" y="30" font-family="'Inter', sans-serif" font-size="12" fill="#94a3b8">Active Drives</text>
    <text x="530" y="62" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800" fill="#38bdf8">14</text>
    <text x="610" y="60" font-family="'Inter', sans-serif" font-size="11" fill="#d8b4fe">Active</text>
  </g>
  
  <!-- Analytics Chart & Candidate list -->
  <rect x="30" y="168" width="460" height="286" rx="10" fill="#130e2c" stroke="#2a1f59" stroke-width="1.5"/>
  <text x="54" y="200" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#f8fafc">Placement Assessment Trends</text>
  
  <!-- Bar chart bars -->
  <g transform="translate(54, 220)">
    <!-- Gridlines -->
    <line x1="0" y1="180" x2="410" y2="180" stroke="#2b2158" stroke-width="1"/>
    <line x1="0" y1="120" x2="410" y2="120" stroke="#231b47" stroke-width="1" stroke-dasharray="4"/>
    <line x1="0" y1="60" x2="410" y2="60" stroke="#231b47" stroke-width="1" stroke-dasharray="4"/>
    
    <rect x="25" y="70" width="36" height="110" rx="4" fill="url(#barGrad)"/>
    <text x="43" y="200" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">DSA</text>
    
    <rect x="95" y="40" width="36" height="140" rx="4" fill="url(#barGrad)"/>
    <text x="113" y="200" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">OOP</text>
    
    <rect x="165" y="55" width="36" height="125" rx="4" fill="url(#barGrad)"/>
    <text x="183" y="200" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">DBMS</text>
    
    <rect x="235" y="30" width="36" height="150" rx="4" fill="url(#barGrad)"/>
    <text x="253" y="200" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Math/Logic</text>
    
    <rect x="305" y="65" width="36" height="115" rx="4" fill="url(#barGrad)"/>
    <text x="323" y="200" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Web/Sys</text>
  </g>
  
  <!-- Right list -->
  <rect x="510" y="168" width="260" height="286" rx="10" fill="#130e2c" stroke="#2a1f59" stroke-width="1.5"/>
  <text x="530" y="200" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#f8fafc">Top Candidate Criteria</text>
  
  <g transform="translate(530, 220)">
    <rect x="0" y="0" width="220" height="50" rx="6" fill="#1b143c"/>
    <text x="12" y="22" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">Algorithms &amp; Problem Solving</text>
    <text x="12" y="38" font-family="'JetBrains Mono', monospace" font-size="10" fill="#10b981">Match rate: 98%</text>
    
    <rect x="0" y="60" width="220" height="50" rx="6" fill="#1b143c"/>
    <text x="12" y="82" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">Full-Stack Architecture</text>
    <text x="12" y="98" font-family="'JetBrains Mono', monospace" font-size="10" fill="#a78bfa">Match rate: 92%</text>
    
    <rect x="0" y="120" width="220" height="50" rx="6" fill="#1b143c"/>
    <text x="12" y="142" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#f8fafc">Database &amp; SQL Querying</text>
    <text x="12" y="158" font-family="'JetBrains Mono', monospace" font-size="10" fill="#38bdf8">Match rate: 95%</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "project-3.svg"), "w", encoding="utf-8") as f:
    f.write(proj3_svg)

print("Visual assets generated successfully!")
