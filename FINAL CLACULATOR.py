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
        if m < M:
            st.error("m must be greater than or equal to M.")
        else:
            t = math.log(m - M + 1)
            st.success(f"Time (t) = {t:.4f} years")


# --- Fusion EQUATION ---
if "show_fusion" not in st.session_state:
    st.session_state.show_fusion = False

if st.button("Fusion Equation"):
    st.session_state.show_fusion = not st.session_state.show_fusion

if st.session_state.show_fusion:
    st.latex(r"+F(a, m, n) = F(a, mn) + a(n-1) + \Delta m")
    st.write("+F = Auronic System Fusion")
    st.write("m = Number of Middlouras")
    st.write("a = Number of Aurons")
    st.write("n = Number of Initial Systems")

    # --- INPUTS ---
    m = st.number_input(
        "Number of Middlouras (m)",
        value=1.0,
        min_value=0.0,
        key="fusion_m"
    )
    a = st.number_input(
        "Number of Aurons (a)",
        value=1.0,
        min_value=0.0,
        key="fusion_a"
    )
    n = st.number_input(
        "Number of Initial Systems (n)",
        value=1.0,
        min_value=0.0,
        key="fusion_n"
    )

    # --- CALCULATE BUTTON ---
    if st.button("Calculate Fusion", key="fusion_calc"):
        F1 = m * n
        F2 = a * (n - 1)
        F="F"
        st.success(
    f"Auronic System Fusion (+F) = F({a}, {F1}) + {F2:.4f} aurons + Δm"
)
