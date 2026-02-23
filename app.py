import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Verification Fee Calculator",
    layout="centered"
)

st.title("Verification Fee Calculator")

# -------------------------------
# Pricing Configuration
# Each methodology has its own tier structure
# Format: (lower_bound, upper_bound, price_per_tonne)
# upper_bound = None means unlimited
# -------------------------------

pricing_config = {

    "Industrial Biochar": [
        (0, 25000, 10.00),
        (25000, 50000, 9.00),
        (50000, 75000, 8.00),
        (75000, 100000, 7.00),
        (100000, 150000, 6.00),
        (150000, 200000, 5.00),
        (200000, 250000, 4.00),
        (250000, 300000, 3.50),
        (300000, 350000, 3.40),
        (350000, 400000, 3.30),
        (400000, 450000, 3.20),
        (450000, 500000, 3.10),
        (500000, None, 3.00),
    ],

    "Artisanal Biochar": [
        (0, 25000, 12.00),
        (25000, 50000, 10.00),
        (50000, 75000, 9.00),
        (75000, 100000, 8.00),
        (100000, 150000, 7.00),
        (150000, 200000, 6.00),
        (200000, 250000, 5.00),
        (250000, 300000, 4.50),
        (300000, 350000, 4.00),
        (350000, 400000, 3.80),
        (400000, 450000, 3.60),
        (450000, 500000, 3.40),
        (500000, None, 3.20),
    ],

    "Electric Vehicles": [
        (0, 25000, 8.00),
        (25000, 50000, 7.50),
        (50000, 75000, 7.00),
        (75000, 100000, 6.50),
        (100000, 150000, 6.00),
        (150000, 200000, 5.50),
        (200000, 250000, 5.00),
        (250000, 300000, 4.50),
        (300000, 350000, 4.20),
        (350000, 400000, 4.00),
        (400000, 450000, 3.80),
        (450000, 500000, 3.60),
        (500000, None, 3.50),
    ],

    "Renewable Energy": [
        (0, 25000, 7.00),
        (25000, 50000, 6.50),
        (50000, 75000, 6.00),
        (75000, 100000, 5.50),
        (100000, 150000, 5.00),
        (150000, 200000, 4.50),
        (200000, 250000, 4.00),
        (250000, 300000, 3.70),
        (300000, 350000, 3.50),
        (350000, 400000, 3.30),
        (400000, 450000, 3.20),
        (450000, 500000, 3.10),
        (500000, None, 3.00),
    ],

    "Livestock": [
        (0, 25000, 11.00),
        (25000, 50000, 9.50),
        (50000, 75000, 8.50),
        (75000, 100000, 7.50),
        (100000, 150000, 6.50),
        (150000, 200000, 5.50),
        (200000, 250000, 4.80),
        (250000, 300000, 4.50),
        (300000, 350000, 4.20),
        (350000, 400000, 4.00),
        (400000, 450000, 3.80),
        (450000, 500000, 3.60),
        (500000, None, 3.40),
    ],

    "Methane": [
        (0, 25000, 9.00),
        (25000, 50000, 8.00),
        (50000, 75000, 7.00),
        (75000, 100000, 6.50),
        (100000, 150000, 6.00),
        (150000, 200000, 5.50),
        (200000, 250000, 5.00),
        (250000, 300000, 4.70),
        (300000, 350000, 4.50),
        (350000, 400000, 4.30),
        (400000, 450000, 4.10),
        (450000, 500000, 3.90),
        (500000, None, 3.70),
    ],

    "Compressed Biogas": [
        (0, 25000, 13.00),
        (25000, 50000, 11.00),
        (50000, 75000, 9.50),
        (75000, 100000, 8.50),
        (100000, 150000, 7.50),
        (150000, 200000, 6.50),
        (200000, 250000, 5.80),
        (250000, 300000, 5.20),
        (300000, 350000, 4.80),
        (350000, 400000, 4.50),
        (400000, 450000, 4.20),
        (450000, 500000, 4.00),
        (500000, None, 3.80),
    ],

    "Clean Cookstove": [
        (0, 25000, 6.00),
        (25000, 50000, 5.50),
        (50000, 75000, 5.00),
        (75000, 100000, 4.50),
        (100000, 150000, 4.00),
        (150000, 200000, 3.80),
        (200000, 250000, 3.60),
        (250000, 300000, 3.50),
        (300000, 350000, 3.40),
        (350000, 400000, 3.30),
        (400000, 450000, 3.20),
        (450000, 500000, 3.10),
        (500000, None, 3.00),
    ],
}

# -------------------------------
# Helper Functions
# -------------------------------

def format_currency(value):
    return "${:,.0f}".format(value)

def get_price_from_tiers(cumulative, tiers):
    for lower, upper, price in tiers:
        if upper is None:
            if cumulative >= lower:
                return lower, upper, price
        elif lower <= cumulative < upper:
            return lower, upper, price
    return tiers[0]

def format_tier_range(lower, upper):
    if upper is None:
        return f"{lower:,}+"
    return f"{lower:,} - {upper:,}"

# -------------------------------
# Inputs
# -------------------------------

methodology = st.selectbox(
    "Methodology",
    list(pricing_config.keys()),
    index=0
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

# -------------------------------
# Calculation
# -------------------------------

if expected_year > 0:

    cumulative = previous_year + expected_year
    tiers = pricing_config[methodology]

    lower, upper, price_per_tonne = get_price_from_tiers(cumulative, tiers)

    total_fee = expected_year * price_per_tonne

    st.divider()

    st.subheader("Total Verification Fee")
    st.markdown(
        f"<h1 style='font-size:42px;'>{format_currency(total_fee)}</h1>",
        unsafe_allow_html=True
    )

    with st.expander("Show breakdown"):

        st.markdown(f"**{methodology}**")

        st.write("### Verification fee table")

        for l, u, p in tiers:
            tier_label = format_tier_range(l, u)
            price_label = f"${p:.2f}"

            if l == lower and u == upper:
                st.markdown(f"**{tier_label} (applied)** — {price_label}")
            else:
                st.write(f"{tier_label} — {price_label}")

        st.divider()
        st.write(f"**Verification fee per tonne:** ${price_per_tonne:.2f}")
        st.write(f"**Total verification fee:** {format_currency(total_fee)}")
