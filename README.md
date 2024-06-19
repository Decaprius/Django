## SSE Web.vzB.22 SoSe24: "Gruppenprojekt" Django
- Michael Fössinger

## Wie man das Projekt aufsetzt (VS Code):
- pip install pipenv
- pipenv install django
- pipenv install willow
- pipenv install paypal-django
- Wenn Dependencies fehlen: in "pipfile.lock" stehen alle Abhängigkeiten.
- pipenv shell (Im Ordner "techmax", direkt unter dem "Django" Überordner)
- python manage.py runserver (Startet lokalen Server, auf der herumprobiert werden kann.)

## Was das Projekt alles kann:
- Grundsätzlich Vollständiger Webshop
- Routing
- User Authentifizierung & Autorisierung
- Zahlungsabwicklung mit PayPal (nur vorbereitet!)
- Bestellung, Warenkorb, Zahlung dynamisch umgesetzt
- Auch Gastwarenkörbe (ohne Benutzer) durch Cookies möglich
- Frontend mit HTML, CSS & Bootstrap umgesetzt
- Etwas JS war notwendig, um z.B. dynamische Warenkorbaktualisierung im Browser zu ermöglichen
