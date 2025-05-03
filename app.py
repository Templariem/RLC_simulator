import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Título y descripción de la aplicación ---
st.set_page_config(page_title="Simulador RLC Serie", layout="centered")

st.title("🔌 Simulador de Circuito RLC Serie")

st.markdown("""
Esta aplicación permite simular la **respuesta transitoria** de un circuito RLC serie ante distintas condiciones iniciales y parámetros del sistema. Es una herramienta interactiva pensada para apoyar el aprendizaje en cursos de teoría de circuitos.

La ecuación diferencial que gobierna el comportamiento del voltaje en el capacitor es:

$$\\frac{d^2}{dt^2}V_c(t) + \\frac{R}{L} \\frac{d}{dt}V_c(t) + \\frac{1}{LC}V_c(t) = \\frac{1}{LC}V_s(t)$$

---

**Desarrollado por:** *Giovanni Cocca-Guardia*, estudiante de doctorado (Ph.D.)  
**Institución:** Escuela de Ingeniería Eléctrica  
**Universidad:** Pontificia Universidad Católica de Valparaíso  
**Curso:** *Teoría de Circuitos 1*

---

🔗 **Repositorio en GitHub:**  
[https://github.com/Templariem/RLC_simulator](https://github.com/Templariem/RLC_simulator)
""")

# --- Simulación numérica (RK4) del RLC serie con fuente Vs ---
def simulate_response(t, alpha, omega0, Vs, V0, I0):
    L = 1.0
    R = 2 * alpha * L
    C = 1 / (omega0**2 * L)
    dt = t[1] - t[0]

    i = I0
    vC = V0
    i_t = np.zeros_like(t)
    vC_t = np.zeros_like(t)

    for idx, _ in enumerate(t):
        i_t[idx] = i
        vC_t[idx] = vC

        def deriv(state):
            i_s, vC_s = state
            di = (Vs - R * i_s - vC_s) / L
            dvC = i_s / C
            return np.array([di, dvC])

        state = np.array([i, vC])
        k1 = deriv(state)
        k2 = deriv(state + 0.5 * dt * k1)
        k3 = deriv(state + 0.5 * dt * k2)
        k4 = deriv(state +     dt * k3)
        state += (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

        i, vC = state

    return i_t, vC_t

def damping_case(alpha, omega0):
    if alpha == 0:
        return "Sin pérdidas"
    if abs(alpha - omega0) < 1e-2:
        return "Críticamente amortiguado"
    if alpha < omega0:
        return "Infraamortiguado"
    return "Sobreamortiguado"

# --- Sliders de parámetros ---
st.sidebar.header("⚙️ Parámetros del sistema")

alpha = st.sidebar.slider("Amortiguamiento α (s⁻¹)", 0.0, 2000.0, 200.0, 10.0)
omega0 = st.sidebar.slider("Frecuencia natural ω₀ (rad/s)", 10.0, 2000.0, 2000.0, 10.0)
Vs = st.sidebar.slider("Fuente DC Vs (V)", 0.0, 100.0, 0.0, 0.5)
V0 = st.sidebar.slider("Voltaje inicial V₀ (V)", 0.0, 20.0, 10.0, 0.5)
I0 = st.sidebar.slider("Corriente inicial I₀ (A)", 0.0, 5.0, 0.0, 0.1)

# --- Cálculo y visualización ---
t = np.linspace(0, 0.1, 2000)
i_t, vC_t = simulate_response(t, alpha, omega0, Vs, V0, I0)

regimen = damping_case(alpha, omega0)
st.subheader(f"🧠 Régimen: **{regimen}**")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, vC_t, color='blue', linewidth=3)
ax1.set_ylabel("Voltaje vC(t) [V]")
ax1.grid(True)

ax2.plot(t, i_t, color='red', linewidth=3)
ax2.set_ylabel("Corriente i(t) [A]")
ax2.set_xlabel("Tiempo [s]")
ax2.grid(True)

st.pyplot(fig)

