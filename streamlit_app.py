import streamlit as st
iport rando
st.title("おみくじアプリ")
if st.button("おみくじを引く"):
    results=["大吉","中吉","小吉","吉","","大凶",凶]
    result=random.choice(results)
    st.write(f"結果:{result}")