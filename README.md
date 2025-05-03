# 🔌 Simulador de Circuito RLC Serie

Este simulador interactivo permite estudiar la **respuesta natural y forzada** de un circuito **RLC serie** ante distintos parámetros. Está diseñado especialmente para estudiantes de ingeniería eléctrica, electrónica o áreas afines que cursan **Teoría de Circuitos**.

---

## ✨ Características

- Ajuste interactivo de:
  - Amortiguamiento (𝛼)
  - Frecuencia natural (𝜔₀)
  - Fuente de tensión DC (Vs)
  - Condiciones iniciales: voltaje en el capacitor (V₀) y corriente inicial (I₀)
- Gráficas dinámicas de:
  - Corriente \( i(t) \)
  - Voltaje en el capacitor \( v_C(t) \)
- Clasificación automática del régimen:
  - Sin pérdidas
  - Críticamente amortiguado
  - Infraamortiguado
  - Sobreamortiguado

---

## 🎯 Objetivo pedagógico

Permitir al estudiante **explorar visualmente** el comportamiento dinámico del circuito RLC y comprender cómo cada parámetro afecta la respuesta transitoria.

Ideal para:

- Comprender los efectos del amortiguamiento
- Analizar la transición entre distintos regímenes de oscilación
- Verificar respuestas esperadas a distintas condiciones iniciales y forzamientos

---

## 🧮 Fundamento teórico

El circuito simulado es un **RLC serie con fuente de tensión continua**. 

La ecuación diferencial que modela la dinámica del circuito en términos del voltaje en el capacitor $V_c(t)$ es:

$$\frac{d^2}{dt^2}V_c(t) + \frac{R}{L} \frac{d}{dt}V_c(t) + \frac{1}{LC}V_c(t) = \frac{1}{LC}V_s(t)$$ 

La ecuación diferencial que modela la dinámica del circuito en términos de la corriente del inductor $i_L(t)$ es:

$$\frac{d^2}{dt^2}i_L(t) + \frac{R}{L} \frac{d}{dt}i_L(t) + \frac{1}{LC}i_L(t) = 0$$ 

La resolución de las ecuaciones diferenciales se realiza con el método de Runge-Kutta de cuarto orden (RK4).

---

## 👾 Probar la aplicación en Streamlit

Haz click aqui: [RLC-simulator](https://rlcsimulator-6euappvhc22l2yhd8v9nfkn.streamlit.app)


