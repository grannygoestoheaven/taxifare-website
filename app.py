import streamlit as st
import datetime
import requests

'''# How much will it cost ?'''

st.markdown("""let's see...""")

date = st.date_input('Day of trip :', datetime.datetime.now())
hour = st.time_input('Pickup hour :', datetime.datetime.now())
pickup_long = st.text_input('Pickup long :')
pickup_lat = st.text_input('Pickup lat :')
dropoff_long = st.text_input('Dropoff long :')
dropoff_lat = st.text_input('Dropoff lat :')
pass_count = st.text_input('Passenger count :')

if st.button('CHECK PRICES'):

    url = 'https://taxifare.lewagon.ai/predict'

    dict = {'pickup_datetime': str(date) + " " +str(hour),
            'pickup_longitude' : pickup_long,
            'pickup_latitude': pickup_lat,
            'dropoff_longitude': dropoff_long,
            'dropoff_latitude' : dropoff_lat,
            'passenger_count': pass_count}

    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url, params=dict)
    prediction = response.json()

    st.write(f"Estimated fare : {round(prediction['fare'], 2)} $")