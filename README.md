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

El circuito simulado es un **RLC serie con fuente de tensión continua**. La ecuación diferencial que lo modela es:
$$\frac{d^2}{dt^2}V_c(t) + \frac{R}{L} \frac{d}{dt}V_c(t) + \frac{1}{LC}V_c(t) = \frac{1}{LC}V_s(t)$$

---
