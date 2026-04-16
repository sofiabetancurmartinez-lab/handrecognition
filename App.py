import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Mi tablero creativo", page_icon="🎨", layout="centered")

st.title("🎨 Mi tablero creativo")
st.markdown("Personaliza tu lienzo y dibuja libremente.")

with st.sidebar:
    st.header("⚙️ Configuración")

    st.markdown("### 📐 Tamaño del lienzo")
    canvas_width = st.slider("Ancho", 300, 900, 600, 50)
    canvas_height = st.slider("Alto", 200, 700, 400, 50)

    st.divider()

    st.markdown("### ✏️ Herramienta")
    drawing_mode = st.selectbox(
        "Selecciona una herramienta",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider("Grosor del trazo", 1, 25, 8)
    stroke_color = st.color_picker("Color del trazo", "#FFFFFF")
    fill_color = st.color_picker("Color de relleno", "#FFB347")
    bg_color = st.color_picker("Color de fondo", "#1E1E1E")

    st.divider()

    clear_canvas = st.button("🗑️ Limpiar lienzo")

st.markdown("#### 🖌️ Área de dibujo")

canvas_result = st_canvas(
    fill_color=fill_color + "80",  # transparencia
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}_{clear_canvas}",
)

if canvas_result.json_data is not None:
    st.success("✨ Tu dibujo se está registrando correctamente.")
