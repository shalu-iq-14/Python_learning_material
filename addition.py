import streamlit as st
st.set_page_config(page_title="number addition",page_icon="➕",layout="centered")
st.title("addition of two number")
st.caption("enter you two number and it will return addtion of them")
form=st.form("add_form")
num1=form.number_input("first number")
num2=form.number_input("second number")
submitted=form.form_submit_button("calculate sum")



if submitted:
    result=num1+num2
    st.divider()
    st.success(F"sum {result}")
    st.metric(label="result",value=result)


for i in range(1,11):
    st.write(f"2 x {i} = {2*i}")