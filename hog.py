import random,math
random.seed(3)
s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">',
'<defs><radialGradient id="g" cx="50%" cy="30%"><stop offset="0" stop-color="#6b7a4a"/><stop offset="1" stop-color="#2d3a22"/></radialGradient>',
'<radialGradient id="b" cx="40%" cy="40%"><stop offset="0" stop-color="#7a5a3c"/><stop offset="1" stop-color="#3b2a1a"/></radialGradient></defs>',
'<rect width="400" height="260" fill="url(#g)"/>',
'<ellipse cx="190" cy="205" rx="130" ry="14" fill="#1a2214" opacity=".6"/>',
# spiny body base
'<ellipse cx="180" cy="140" rx="115" ry="68" fill="url(#b)"/>']
# spines: many strokes radiating over upper body
for i in range(1400):
    a=random.uniform(math.pi*0.98,math.pi*2.05)
    r=random.random()**0.5
    cx=180+math.cos(a)*r*105;cy=150+math.sin(a)*r*70
    L=random.uniform(14,24)
    ang=a+random.uniform(-.35,.35)
    x2=cx+math.cos(ang)*L;y2=cy+math.sin(ang)*L
    t=random.random()
    col="#%02x%02x%02x"%(int(60+t*140),int(45+t*110),int(28+t*70))
    s.append(f'<path d="M{cx:.1f} {cy:.1f} L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="1.6" stroke-linecap="round"/>')
# face
s+=['<path d="M262 112 Q330 128 352 158 Q330 182 268 186 Q250 150 262 112Z" fill="#d1ad88"/>',
'<path d="M262 112 Q300 112 330 140 Q300 130 262 140Z" fill="#a98763"/>',
'<ellipse cx="354" cy="158" rx="6" ry="5" fill="#1b1410"/>',
'<circle cx="318" cy="142" r="6" fill="#120c08"/><circle cx="320" cy="140" r="1.8" fill="#fff" opacity=".8"/>',
'<ellipse cx="282" cy="118" rx="9" ry="7" fill="#b5906b"/>',
'<ellipse cx="270" cy="196" rx="9" ry="6" fill="#b5906b"/><ellipse cx="200" cy="200" rx="9" ry="6" fill="#b5906b"/>']
s.append('</svg>')
open('hog.svg','w').write(''.join(s))
