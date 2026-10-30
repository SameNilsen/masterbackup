def func_x(num):
    if num == 1:
        return a()
    elif num == 2:
        return b()
    elif num == 3:
        return c()
    elif num == 4:
        return d()
    elif num == 5:
        return e()



def func_x(is_chubby):
    if is_chubby is True:
        return a()
    elif is_chubby is False:
        return b()


def func_x(array):
    for i in range(len(array)):
        print(array[i])



def func_x(num):
    if num > 10:
        return True
    else:
        return False



a = 1
b = 2
c = 3



x = [10, 20, 30]

a = x[0]
b = x[1]
c = x[2]



def func_x(breeds, pet):
    for breed in breeds:
        if breed == pet:
            print("I have a dog.")
    else:
        print("I don't have a dog")


func_x(["chihuahua", "jack russell"], "chihuahua")

# => I have a dog.
# => I don't have a dog



from typing import *



f = open("file.text", "r")
try:
    content = f.read()
finally:
    f.close()


def func_x(param):
    if param:
        return 200, {"message": f"{param}"}
    else:
        return 400, "A useful error message"



if something == None:
    print("Something is None!")


condition = True
if conditon == True:
    print("'Tis true!")



doggos = ["tamago", "charlie"]
if type(doggos) is list:
    print("'doggos' is a list")



def get_lego():
    return "21103", "Back to the Future Time Machine", "401", "2013"

my_lego = get_lego()
print(my_lego[0], my_lego[1], my_lego[2], my_lego[3])



numbers = [10, 20, 30]
double_numbers = list(map(lambda num: num * 2, numbers))



from elastic_appsearch import *



if "key" in dictionary:
    item = dictionary["key"]
else:
    item = ""




try:
    item = dictionary["key"]
except KeyError:
    item = ""





if super_long_comparsion1 and super_long_comparison2:
    pass

