def verifIP(adress):   

    adress_buffer = str() #I create a buffer adress to store each pattern
    counter_point = 0 #to count the number of points

    for i in adress:     

        if i == ".":
            counter_point += 1; #to count pattern
            int_adress = int(adress_buffer) 

            if  (0 <= int_adress <= 255) & (len(adress_buffer) <= 3):
                int_adress = 0 # I empty this 
                adress_buffer = "" # and this

            else:
                print adress," is correct"
                break

        else:
            adress_buffer += i

    if counter_point == 3: 
        int_adress = int(adress_buffer)

        if  (0 <= int_adress <= 255) & (len(adress_buffer) <= 3):
            print adress,"is correct"

        else:
            print adress,"is wrong"

IP_adress = input("Enter valid IP adress (use quotes): ")

verifIP(IP_adress);

