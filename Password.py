import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔑")
st.title("🔐Password Strength Meter")
st.markdown("""
            ## Welcome to the Password Strength Meter!👋
            we will help you create a strong password🔒 that is hard to guess and secure your accounts.
            """)

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0
if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one uppercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(e.g., !@#$%^&*).")

    if score == 4:
        st.success("✅Your password is strong!")
    elif score == 3:                                                    
        st.warning("⚠️Your password is moderate. Consider adding more complexity.")
    elif score == 2:
        st.warning("⚠️Your password is weak. Consider adding more complexity.")

    if feedback:
        st.markdown("## Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)
else:
    st.warning("⚠️Please enter a password to check its strength.")


