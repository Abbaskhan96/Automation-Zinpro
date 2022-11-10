class Assessors_xpath():
 
#===================================<<<======| Heat- Abatement |======>>>======================================        
        accessible_water_pen = "//div[@class='col-lg-12']//div[@class='form-group mb-0 mb-sm-1']//input[@type='number']"
 
 #____________________________________________| W A T E R |____________________________________________________
 #-----------------------------------------Water_Availablity---------|
        WA_yes = "//label[@for='kfpbus' and text()='Yes']"  
        WA_no = "//label[@for='nk8oxv']" 
 #---------------Area arount the Water is free of muds/stones-----------|
        Warea_yes = "//label[@for='qdd8v']"
        Warea_no = "//label[@for='4o5hi']"
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````
#_____________________________________________| F A N S |_______________________________________________________
#---------------------------------------Fans Located in Feed Area?--------|
        FL_FA_no = "//label[@for='3a3hu']"  
        FL_FA_yes = "//label[@for='b4lp5s']"
        HVLS_FA_yes="//label[@for='bkgazm']"
        HVLS_FA_no="//label[@for='2xi4wq']"
#----------------Fans'Temperature?-----------------------|
        Fan_FA_temp = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[1]/div[1]/input[1]"
#----------------Fan's Diameter? (SELECT)-------------------------|
        Fan_FA_diamter = "//select[@name='feed_bunk_area_fan_diameter']"
#----------------Fan's spacing?--------------------------|
        Fan_FA_space = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[3]/div[1]/input[1]"
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
#_____________________________________|R E S T I N G _ A R E A |________________________________________
#----------------------------------------Fan's Located in Resting---------------------------------------------- 
        FL_RA_no = "//label[@for='308p8f']"
        FL_Ra_yes = "//label[@for='6rhft']"
        HVLS_RA_yes="//label[@for='8jijyt']"
        HVLS_RA_no="//label[@for='nhq1uf']"
#----------------Fans'Temperature?-----------------------|
        Fan_RA_temp = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[9]/div[1]/div[1]/input[1]"
#----------------Fan's Diameter (SELECT)?-------------------------|
        Fan_RA_diamter = "//select[@name='resting_area_paddock_fan_diameter']"
#----------------Fan's spacing?--------------------------|
        Fan_RA_space = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[9]/div[3]/div[1]/input[1]"

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
#_____________________________________________| S O A K E R S |________________________________________

#----------------------------------------Soakers Located in Feeding Area---------------------------------------------- 
        Soak_FA_no = "//label[@for='7hgwdi']"
        Soak_FA_yes = "//label[@for='w265nk']"
#----------------------------------------Soakers Located in Resting Area-----------------------------
        Soak_RA_no = "//label[@for='2yc3vt']"
        Soak_RA_yes = "//label[@for='xdmp7']"
#----------------------------------------water droplet effecting cows------------------------------
        drop_no= "//label[@for='vwldj']"
        drop_yes="//label[@for='ky0a1']"
#----------------Soak Temperature?----------------------|
        Soak_temp = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[11]/div[1]/div[1]/input[1]"
#----------------Soak Duration?-------------------------|
        Soak_time = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[11]/div[2]/div[1]/input[1]"
#----------------Soak Frequency?------------------------|
        Soak_freq = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[11]/div[3]/div[1]/input[1]"
#----------------------------------------Frequency of soaking vary with Temperature------------------------------
        SoakFreq_VT_no= "//label[@for='vwldj']"
        SoakFreq_VT_yes= "//label[@for='fiban']"
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
##____________________________________________| S H A D E |________________________________________

#----------------------------------------Soakers Located in Feeding Area---------------------------------------------- 
        Shade_FA_no = "//label[@for='mnzeg']"
        Shade_FA_yes = "//label[@for='0sk45h']"
#----------------------------------------Soakers Located in Resting Area---------------------------------------------- 
        Shade_RA_no = "//label[@for='er2xyi']"
        Shade_RA_yes = "//label[@for='b8buzo']"
#----------------------------------------AirCooling units used in Resting Area------------------------------------
        Shade_unit_no="//label[@for='glnb8']"
        Shada_unit_yes="//label[@for='g3pzdr']"