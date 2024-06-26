#Advices the user on type of clothing based on entered weather condition

weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
else:
    print("Sorry, I don't have recommendations for this weather.")
