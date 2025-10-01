import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Titulek aplikace
st.title("Body na kružnici")

# --- Vstupy od uživatele ---
st.sidebar.header("Parametry kružnice")
x0 = st.sidebar.number_input("Souřadnice středu X", value=0.0)
y0 = st.sidebar.number_input("Souřadnice středu Y", value=0.0)
r = st.sidebar.number_input("Poloměr (m)", value=5.0, min_value=0.1)
n = st.sidebar.number_input("Počet bodů", value=6, min_value=1, step=1)
color = st.sidebar.color_picker("Barva bodů", "#ff0000")

# Výpočet bodů
theta = np.linspace(0, 2*np.pi, n, endpoint=False)
x = x0 + r * np.cos(theta)
y = y0 + r * np.sin(theta)

# --- Vykreslení ---
fig, ax = plt.subplots()
ax.plot(x0, y0, "bo", label="Střed")
ax.scatter(x, y, c=color, label="Body")
circle = plt.Circle((x0, y0), r, color="gray", fill=False)
ax.add_patch(circle)

# Osy s jednotkami
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_aspect("equal")
ax.legend()

st.pyplot(fig)

# --- Info sekce ---
with st.expander("O aplikaci"):
    st.write("""
    **Autor:** Milan Chmelař  
    **Kontakt:** mildamilda0@post.cz  
    **Škola**: Vysoké Učení Technické Brno - Fakulta Stavební
    
    **Použité technologie:** Python, Streamlit, Matplotlib, ReportLab  
    """)

# --- Export do PDF ---
if st.button("Uložit do PDF"):
    pdf_file = "vystup.pdf"
    c = canvas.Canvas(pdf_file, pagesize=A4)
    text = c.beginText(50, 800)
    text.setFont("Helvetica", 12)
    text.textLine("Parametry úlohy:")
    text.textLine(f"Střed: ({x0}, {y0})")
    text.textLine(f"Poloměr: {r} m")
    text.textLine(f"Počet bodů: {n}")
    text.textLine(f"Barva: {color}")
    text.textLine("")
    text.textLine("Autor: Milan Chmelař, Kontakt: mildamilda0@post.cz")
    c.drawText(text)
    c.save()
    st.success("PDF bylo vytvořeno.")
    with open(pdf_file, "rb") as f:
        st.download_button("Stáhnout PDF", f, file_name="vystup.pdf")



