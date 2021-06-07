fileMatrix = []

with open('201904 sales reciepts.csv', 'r') as fileRead:
    for lineContent in fileRead:
        fileMatrix.append(lineContent.strip('\n').split(','))

for i in fileMatrix:
    i[1]= int(i[1])
    i[0]= int(i[0])

for j in fileMatrix:
    if j[0] > 1000:
        fileMatrix.remove(j)

fileMatrix.sort()

from collections import Counter
a=[]
b=[]
most_love=[]

for x in range(1001):
    for y in fileMatrix:
        if y[0] == x:
            a.append(y[1])

    c=Counter(a)
    mode = c.most_common(3)

    if len(mode) == 0:
        k=0
        p=0
        q=0
        most_love.append([x,k,p,q])
        a=[]
    elif len(mode) == 1:
        k= mode[0][0]
        p=0
        q=0
        most_love.append([x,k,p,q])
        a=[]
    elif len(mode) == 2:
        k= mode[0][0]
        p= mode[1][0]
        q=0
        most_love.append([x,k,p,q])
        a=[]
    elif len(mode) ==3:
        k= mode[0][0]
        p= mode[1][0]
        q= mode[2][0]
        most_love.append([x,k,p,q])
        a=[]
    
customer =[]

with open('customer.csv', 'r') as fileRead:
    for lineContent in fileRead:
        customer.append(lineContent.strip('\n').split(','))

next_num = len(customer)

product =[]
with open('product.csv', 'r') as fileRead:
    for lineContent in fileRead:
        product.append(lineContent.strip('\n'))

while True:
    print("Cafe in Three")
    print("1. cafe member order (order alone)")
    print("2. cafe team order (order together)")
    print("3. add id")
    print("4. quit")

    select = int(input("choose one(1 or 2 or 3 or 4) : "))

    if select == 1:
        while True:
            id = int(input("press customer_id : "))
            password = str(input("press loyalty_card_number : "))

            if customer[id][3] == password:

                print("correct!")
                print("Hello!",customer[id][1])
                print("email: ",customer[id][2], "birth year: ",customer[id][4] )

                favorite_beverage1 = product[most_love[id][1]]
                favorite_beverage2 = product[most_love[id][2]]
                favorite_beverage3 = product[most_love[id][3]]

                print("please order. your most favorite beverage is", "[1.",favorite_beverage1,"2.",favorite_beverage2,"3.",favorite_beverage3+"]")
                order1 = str(input("do you want to favorite beverage? y/n:"))

                if order1 == "y":
                    fff = int(input("what kind of beverage?: "))
                    if fff == 1:
                        print("order is clear - " , favorite_beverage1)

                        with open('201904 sales reciepts.csv', 'a') as file:
                            id1 = str(id)
                            most_love1 = str(most_love[id][1])
                            file.write("\n%s,%s"%(id1,most_love1))
                        break
                    elif fff == 2:
                        print("order is clear - " , favorite_beverage2)

                        with open('201904 sales reciepts.csv', 'a') as file:
                            id1 = str(id)
                            most_love1 = str(most_love[id][2])
                            file.write("\n%s,%s"%(id1,most_love1))
                        break
                    elif fff == 3:
                        print("order is clear - " , favorite_beverage3)

                        with open('201904 sales reciepts.csv', 'a') as file:
                            id1 = str(id)
                            most_love1 = str(most_love[id][3])
                            file.write("\n%s,%s"%(id1,most_love1))    
                        break
                else:
                    order2 = int(input("beverage id? : "))
                    order_beverage = product[order2]
                    print("order is clear! - ", order_beverage)

                    with open('201904 sales reciepts.csv', 'a') as file:
                        id1 = str(id)
                        most_love1 = str(order2)
                        file.write("\n%s,%s"%(id1,most_love1))
                    break
            else:
                print("id_card_number is wrong!")
                break

    elif select ==2:
        num = int(input("number of people? :"))
        order =[]
        together =[]

        with open('product.csv', 'r') as fileRead:
            for lineContent in fileRead:
                together.append(lineContent.strip('\n'))

        i=0
        while i < num:
            i = i+1
            a = str(input("name of person? : "))
            b = int(input("beverage id? : "))
            b = together[b-1]
            order.append([a,b])

        while True:
            print(order)
            x = str(input("do yo want to change? y/n : "))

            if x == "y":
                k = str(input("name or beverage or add? n/b/a : "))

                if k == "b":
                    y = int(input("what number? : "))
                    z = int(input("beverage id? : "))
                    z = together[z-1]
                    order[y-1][1] = z
                elif k == "n":
                    y = int(input("what number? : "))
                    z = str(input("what is your name? : "))
                    order[y-1][0] = z
                elif k == "a":
                    y = str(input("what is your name? : "))
                    z= int(input("beverage id? : "))
                    z = together[z-1]
                    order.append([y,z])

            else:
                print("order is clear!!")
                print(order)
                break
            
    elif select == 3:
        name1 = str(input("what is your name? : "))
        email1 = str(input("what is your email? : "))
        idcardnum1 = str(input("what is your id card number? : "))
        birthyear1 = str(input("what is your birth year? : "))

        with open('customer.csv', 'a') as file:
            file.write("%s,%s,%s,%s,%s\n" %(next_num,name1,email1,idcardnum1,birthyear1))

        customer.append([next_num,name1,email1,idcardnum1,birthyear1])
        print("your customer id is", next_num)

    elif select ==4:
        print("quit the program. bye")
        break