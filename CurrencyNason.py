Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Nason
# Fall 2022
# Currency


# input
usd_eud = float(input('Enter U.S. Dollar to Euros Exchange Rate: '))
choice = input('Enter Currency you would like to convert to either USD or Euros: ')
# If Statement
if choice == 'USD':
  amount = float(input('Enter Amount you would like to convert: '))
  converted_amount = usd_eud * amount
  print('$'"{:.2f}".format(amount),'is', "{:.2f}".format(converted_amount), 'Euros')
  
# Else if Statement
elif choice == 'Euros':
  amount = float(input('Enter Amount you would like to convert: '))
  converted_amount = amount / usd_eud
  print("{:.2f}".format(amount), 'Euros is','$'"{:.2f}".format(converted_amount))
# Else Statement
else:
  print('Error, please enter either USD or Euros')