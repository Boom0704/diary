def fn_sales_price(value, percent):
    return (int(value * (100 - percent) / 100), int(value * percent / 100))

sales_result = fn_sales_price(1000, 10)
print(sales_result)
a =13
print(f"글자 : {a}")