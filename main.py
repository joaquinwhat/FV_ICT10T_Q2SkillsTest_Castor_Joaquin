from pyscript import document, display

planets = {"MERCURY": ("MERCURY", 1, 0)}


def search_planet(e):
    
    Planet1 = document.getElementById("planet1").value

    result = planets.get(Planet1, ("Planet Not Found", "-", "-"))

    document.getElementById("code").innerText = Planet1
    document.getElementById("name").innerText = result[0]
    document.getElementById("order").innerText = result[1]
    document.getElementById("moons").innerText = result[2]