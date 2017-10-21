total = 0

def process_order(x_list):
    index_number = 0
    for i in x_list:
        print(str(index_number) + " - "+ str(i))
        index_number = index_number + 1
    remove_item = int(input("which item would you like to remove?: "))
    print("thank you for removing this item")
    del x_list[remove_item]
    total_calc = 0
    for n in x_list:
        total_calc = (n[1] * n[2]) + total_calc
    global total 
    total = total_calc
    #return total
    del x_list[0:-1]
    del x_list[0]
    
     


x = [("oranges", 4, 3.22),("gummy bears",1,1.99),("sour bites", 3, 2.33), ("antacid", 1, 5.33)]
while(len(x)>0):
    process_order(x)
    
print("total price: ", total)