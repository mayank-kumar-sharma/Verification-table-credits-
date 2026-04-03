import streamlit as st

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(
    page_title="Verification Fee Calculator",
    layout="centered"
)

# ------------------------------------------------
# Custom Styling (Premium Minimal UI)
# ------------------------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 600;
    margin-bottom: 20px;
}
.big-fee {
    font-size: 52px;
    font-weight: 700;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Verification Fee Calculator</div>', unsafe_allow_html=True)

# ------------------------------------------------
# Pricing Configuration (Flat Pricing)
# ------------------------------------------------
pricing_config = {
    "EV Fleets": 90,
    "Solar Energy": 45,
    "Biochar (Industrial)": 900,
    "Biochar (Artisanal)": 450,
    "Compressed Biogas (CBG)": 135,
    "Clean Cookstove": 90,
    "Livestock Methane": 180
}

# ------------------------------------------------
# Helper Function
# ------------------------------------------------
def format_currency(value):
    return "₹{:,.0f}".format(value)

# ------------------------------------------------
# CALCULATOR SECTION
# ------------------------------------------------
methodology_calc = st.selectbox(
    "Methodology",
    list(pricing_config.keys())
)

previous_year = st.number_input(
    "Tonnes issued to the Supplier in the previous calendar year",
    min_value=0,
    value=0,
    step=1000
)

expected_year = st.number_input(
    "Tonnes expected to be issued to the Supplier this calendar year",
    min_value=0,
    value=0,
    step=1000
)

# ------------------------------------------------
# Calculation Logic (Flat Pricing)
# ------------------------------------------------
if expected_year > 0:
    price_per_tonne = pricing_config[methodology_calc]
    total_fee = expected_year * price_per_tonne

    st.markdown(
        f'<div class="big-fee">{format_currency(total_fee)}</div>',
        unsafe_allow_html=True
    )

    st.write(f"Verification fee per tonne: ₹{price_per_tonne}")

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("---")
st.markdown("💡 Made with ❤️ by **Mayank Kumar Sharma**")
