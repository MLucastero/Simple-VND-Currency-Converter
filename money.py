#Convert to vietnam dong only
while True:
    print('''
#     # ##    # ######      
#     # # #   # #     # 
#     # #  #  # #     # 
 #   #  #   # # #     # 
  # #   #    ## #     # 
   #    #     # ######  
            ''')
    print("CTRL C to quit!")
    # Input 
    vnd = float(input("Enter VND: "))
    usd = float(vnd) / 23000
    euro = float(vnd) / 26000
    yen = float(vnd) / 196
    yuan = float(vnd) /  3500
    print('')
    # Calculate
    print("==========================================")
    print ( str(vnd) + " VND = " + str(usd) + " USD")
    print("------------------------------------------")
    print ( str(vnd) + " VND = " + str(euro) + " Euro")
    print("------------------------------------------")
    print ( str(vnd) + " VND = " + str(yen) + " Yen")
    print("------------------------------------------")
    print ( str(vnd) + " VND = " + str(yuan) + " Yuan")
    print("==========================================")
    print("^^^^^^@@@@@@^^^^^^******^^^^^^@@@@@@^^^^^^") 
    
   

    
