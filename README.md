# 🌍 Planet Simulation

A **Pygame-based simulation** of planetary orbits in a simplified 2D solar system. This project models the motion of celestial bodies under gravitational forces using Newtonian mechanics, and visualises their orbits in real time.

---

## 🚀 Features

- Real-time simulation of gravitational forces
- Visual orbit trails for each planet
- Distance display from the Sun for each planet
- Scaled orbits using astronomical units
- Realistic planetary motion with velocity updates

---

## 🛠️ Technologies Used

- **Python 3**
- **Pygame** – for graphics and event handling

---

## 🪐 Celestial Bodies

- ☀️ **Sun** – Massive central body, fixed in space
- 🌍 **Earth**
- 🔴 **Mars**
- 🟤 **Mercury**
- 🟡 **Venus**
  
More planets and suns can be added via the Planet and Sun classes.

Each planet has:
- Mass (kg)
- Initial velocity (m/s)
- Distance from the Sun (AU)
- Color and size for visualisation

---

## 📏 Physics Details

- **G**: Gravitational constant = `6.67428e-11 N·(m/kg)^2`
- **AU**: Astronomical Unit = `149,597,870.7 km`
- **Time Step**: One simulation day per frame (`86400 seconds`)
- **Distance scale**: `200 pixels = 1 AU`

---

## 💻 How to Run

1. Install dependencies:

```bash
pip install pygame
```

2. Run the simulation:
```bash
python main.py
```

Orbits are drawn as trails of the planet's past positions.

Distance from Sun is displayed dynamically.

Window size: 800 x 800 pixels

