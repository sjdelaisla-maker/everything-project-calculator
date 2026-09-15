import streamlit as st
import math

st.title("The Everything Project Calculator")

# --- DECAY TIME CALCULATOR ---
if "show_decay" not in st.session_state:
    st.session_state.show_decay = False

if st.button("Decay Time Equation"):
    st.session_state.show_decay = not st.session_state.show_decay

if st.session_state.show_decay:
    st.latex(r"D = \lfloor\frac{100}{m}\rfloor m \ln(m+1)")
    st.write("D = Decay time")
    st.write("m = Number of Middlouras")

    # --- INPUTS ---
    m = st.number_input(
        "Number of Middlouras (m)",
        value=1.0,
        min_value=0.0,
        key="decay_m"
    )

    # --- CALCULATE BUTTON ---
    if st.button("Calculate Decay Time", key="decay_calc"):
        if m == 0:
            st.error("m cannot be zero.")
        else:
            D = math.floor(100 / m) * m * math.log(m + 1)
            st.success(f"Decay Time (D) = {D:.4f} years")

# --- TIME EQUATION ---
if "show_time" not in st.session_state:
    st.session_state.show_time = False

if st.button("Time Equation"):
    st.session_state.show_time = not st.session_state.show_time

if st.session_state.show_time:
    st.latex(r"t =\ln\left(m-M+1\right)")
    st.write("t = Time")
    st.write("M = Number of Desired Middlouras")

    # --- INPUTS ---
    m = st.number_input(
        "Number of Middlouras (m)",
        value=1.0,
        min_value=0.0,
        key="time_m"
    )
    M = st.number_input(
        "Number of Desired Middlouras (M)",
        value=1.0,
        min_value=0.0,
        key="time_M"
    )

    # --- CALCULATE BUTTON ---
    if st.button("Calculate Time at M Middlouras", key="time_calc"):
        t = math.log(m - M + 1)
        st.success(f"Time (t) = {t:.4f} years")