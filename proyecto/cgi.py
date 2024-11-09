# cgi.py - Simulador de ejemplo (esto no reemplaza todas las funciones del módulo original)
def escape(s, quote=True):
    """Función simple de ejemplo para escapar HTML"""
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    if quote:
        s = s.replace('"', "&quot;")
        s = s.replace("'", "&#x27;")
    return s
from cgi import escape  # Usará tu archivo personalizado