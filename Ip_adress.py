def verifIP(adress):
    adress_buffer = str()
    counter_point = 0
    for i in adress:
        if counter_point == 3: 
            adress_buffer += i      
        elif i == ".":
            counter_point += 1;
            int_adress = int(adress_buffer)
            if  (0 <= int_adress <= 255) & (len(adress_buffer) <= 3):
                int_adress = 0
                adress_buffer = ""
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

