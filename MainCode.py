import streamlit as st

st.sidebar.header("Navigation")

HomeButton = st.sidebar.button("Home")
BCButton = st.sidebar.button("Stake Calculator")
OCButton = st.sidebar.button("Odd Converter")

if HomeButton:
    st.session_state.page = "home"
    
if BCButton:
    st.session_state.page = "stake_calculator"
    
if OCButton:
    st.session_state.page = "odd_converter"

def home():
    st.title("Betting Tools")
    st.write("Welcome to the Betting Tools App! Use the navigation bar to the left to enter into the available tools.")

def stake_calculator():
    st.title("Stake Calculator")
    
    # User inputs
    bankroll = st.number_input("Enter your bankroll ($):", min_value=0, step=100)
    props_count = st.number_input("Enter number of props:", min_value=0, step=1)
    portion = st.number_input("Enter portion percentage (%):", min_value=0, max_value=100, step=5)
    
    if st.button("Calculate"):
        try:
            stake = (bankroll * (portion/100) / (props_count + 1/2))
            multi_stake = stake / 2
            total_wagered = (stake * props_count) + multi_stake
            
            # Display results
            st.success(f"Stake per bet: ${stake:.2f}")
            st.success(f"Multi Stake: ${multi_stake:.2f}")
            st.success(f"Total Wagered: ${total_wagered:.2f}")
        except Exception as e:
            st.error("Error in calculation. Please check your inputs.")

def odd_converter():
    st.title("Odd Converter")
    
    # User inputs
    decimal_odds = st.number_input("Insert Decimal Odds:", min_value=0.00, step=0.01, format="%.2f")
    
    if st.button("Calculate"): 
        try:
            if decimal_odds >= 2:
                MoneyLineOdds = (decimal_odds - 1) * 100
            else:
                MoneyLineOdds = -100 / (decimal_odds-1)
                
            st.success(f"Moneyline Odds: {MoneyLineOdds:.0f}")
            
        except Exception as e:
            st.error("Error in calculation. Please check your inputs.")
            

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Page Navigation
if st.session_state.page == "home":
    home()
elif st.session_state.page == "stake_calculator":
    stake_calculator()
elif st.session_state.page == "odd_converter":
    odd_converter()
