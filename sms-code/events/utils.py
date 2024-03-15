def decrypt_event_mcidi(data):
        
    data = data.split()
    
    try:
        #Recveiver
        receiveer_no = R = data[2][0]
        #Line
        line_no = L = data[2][1]
        #Account
        account_no = CCCC = data[3]
        #Alarm Code
        alarm_code = TAAA = data[5]
        #Zone
        zone = GG = data[6]
        #User
        user = ZZZ = data[7]
        
        return receiveer_no, line_no, account_no, alarm_code, zone, user

    except:
        pass
    
    print(R, L, CCCC, TAAA, GG, ZZZ)
    

def decrypt_event_sg(data):
        
    data = data.split()
    
    try:
        #Protocole
        protocole = P = data[0][0]
        #Recveiver
        receiveer_no = R = data[0][1:3]
        #Line
        line_no = L = data[0][3:6]
        #Account
        account_no = CCCC = data[1][2:6]
        #Alarm Code
        alarm_code = TAAA = data[1][6:10]
        #Zone
        zone = GG = data[1][10:12]
        #User
        user = ZZZ = data[1][12:15]
        
        return protocole, receiveer_no, line_no, account_no, alarm_code, zone, user

    except:
        pass
    
    print(P, R, L, CCCC, TAAA, GG, ZZZ)
    

mask = "HH:mm__MM/DD__RL_CCCC_18_TAAA_GG_ZZZ"
mask = "ORRLLL_18CCCCTAAAGGZZZ"
data = "11:20  01/22  11 0516 18 E400 01 001"


decrypt_event_mcidi("11:20  01/22  11 0516 18 E400 01 001")
decrypt_event_sg("ORRLLL 18CCCCTAAAGGZZZ")
