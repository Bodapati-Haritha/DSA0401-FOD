import pandas as pd
data = {
    'property_id': [11, 22, 33, 44, 55],
    'location': ['City p', 'City q', 'City r', 'City s', 'City q'],
    'number_of_bedrooms': [1,2,3,4,5],
    'area_sqft': [2500, 2800, 2200, 1200, 2500],
    'listing_price': [250000, 30000, 350000, 20000, 40000]
}
data1= pd.DataFrame(data)
avg=data1.groupby('location')['listing_price'].mean()
bed1= data1[data1['number_of_bedrooms'] > 4]
bed2=len(bed1)
area=data1[data1['area_sqft']==data1['area_sqft'].max()]
print(avg)
print("Number of properties with more than four bedrooms:")
print(bed2)
print("Property with the largest area:")
print(area)
