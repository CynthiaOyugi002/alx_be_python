weather = input("what is the weather like today?(sunny/rainy/cold):").lower()
if weather == "sunny":
    print("wear a t-shirt and sunglasses")
elif weather == "rainy":
    print("do not forget your umbrella and a raincoat")
elif weather == "cold":
    print("make sure to wear a warm coat and  a scarf")
else :
    print("soory, i do not have recommendations for this weather")