from main import simple_ex
res_of_min_1_2_3=simple_ex(1,2,3)
if res_of_min_1_2_3==-5:
    print("Test success")

else:
    print("Test failed")
def assertEqual(expected,actual):
    if expected==actual:
        print("Тест прошел успешно")
    else:
       raise AssertionError("Тест провален")

assertEqual(-1,simple_ex(1,1,1))

assertEqual(0,simple_ex(0,0,0))
assertEqual(-2,simple_ex(2,2,2))
assertEqual(-6,simple_ex(3,3,3))
assertEqual(-12,simple_ex(4,4,4))
assertEqual(-1,simple_ex(1,1,1))
assertEqual(0,simple_ex(0,1,1))
assertEqual(9,simple_ex(2,3,4))