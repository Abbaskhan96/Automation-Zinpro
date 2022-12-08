class Assessors_HeatAbatement_xpath():
 
#===================================<<<======| Heat- Abatement |======>>>======================================        
        accessible_water_pen = "//div[@class='col-lg-12']//div[@class='form-group mb-0 mb-sm-1']//input[@type='number']"
 
 #____________________________________________| W A T E R |____________________________________________________
 #-----------------------------------------Water_Availablity---------|
        WA_yes = "//div[4][@class='row']//child::div[2]//child::div[2]//child::label"  
        WA_no = "//div[4][@class='row']//child::div[2]//child::div[1]//child::label" 
 #---------------Area arount the Water is free of muds/stones-----------|
        Warea_yes = "//div[5][@class='row']//child::div[2]//child::div[2]//child::label"
        Warea_no = "//div[5][@class='row']//child::div[2]//child::div[2]//child::label"
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````
#_____________________________________________| F A N S |_______________________________________________________
#---------------------------------------Fans Located in Feed Area?--------|
        FL_FA_no = "//div[6][@class='row']//div[3]//child::div[2]//child::div[1]//label"  
        FL_FA_yes = "//div[6][@class='row']//div[3]//child::div[2]//child::div[2]//label"
        HVLS_FA_yes="//div[6][@class='row']//div[2]//child::div[2]//child::div[2]//label"
        HVLS_FA_no="//div[6][@class='row']//div[2]//child::div[2]//child::div[1]//label"
#----------------Fans'Temperature?-----------------------|
        Fan_FA_temp = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[1]/div[1]/input[1]"
#----------------Fan's Diameter? (SELECT)-------------------------|
        Fan_FA_diamter = "//select[@name='feed_bunk_area_fan_diameter']"
#----------------Fan's spacing?--------------------------|
        Fan_FA_space = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[3]/div[1]/input[1]"
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
#_____________________________________|R E S T I N G _ A R E A |________________________________________
#----------------------------------------Fan's Located in Resting---------------------------------------------- 
        FL_RA_no = "//*[@id='top']/main/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div[2]/div[1]/label"
        FL_RA_yes = "//*[@id='top']/main/div[1]/div/div/div[2]/div[8]/div[2]/div[1]/div[2]/div[2]/label"
        HVLS_RA_yes="//*[@id='top']/main/div[1]/div/div/div[2]/div[8]/div[2]/div[2]/div[2]/div[2]/label"
        HVLS_RA_no="//*[@id='top']/main/div[1]/div/div/div[2]/div[8]/div[2]/div[2]/div[2]/div[1]/label"
#----------------Fans'Temperature?-----------------------|
        Fan_RA_temp = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[9]/div[1]/div[1]/input[1]"
#----------------Fan's Diameter (SELECT)?-------------------------|
        Fan_RA_diamter = "//select[@name='resting_area_paddock_fan_diameter']"
#----------------Fan's spacing?--------------------------|
        Fan_RA_space = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[9]/div[3]/div[1]/input[1]"

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
#_____________________________________________| S O A K E R S |________________________________________

#----------------------------------------Soakers Located in Feeding Area---------------------------------------------- 
        Soak_FA_no = "//*[@id='top']/main/div[1]/div/div/div[2]/div[10]/div[2]/div[1]/div[2]/div[1]/label"
        Soak_FA_yes = "//*[@id='top']/main/div[1]/div/div/div[2]/div[10]/div[2]/div[1]/div[2]/div[2]/label"
#----------------------------------------Soakers Located in Resting Area-----------------------------
        Soak_RA_no = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[10]/div[2]/div[2]/div[2]/div[1]/label"
        Soak_RA_yes = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[10]/div[2]/div[2]/div[2]/div[2]/label"
#----------------------------------------water droplet effecting cows------------------------------
        drop_no= "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[10]/div[2]/div[3]/div[2]/div[1]/label"
        drop_yes="//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[10]/div[2]/div[3]/div[2]/div[2]/label"
#----------------Soak Temperature?----------------------|
        Soak_temp = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[11]/div[1]/div[1]/input[1]"
#----------------Soak Duration?-------------------------|
        Soak_time = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[11]/div[2]/div[1]/input[1]"
#----------------Soak Frequency?------------------------|
        Soak_freq = "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[11]/div[3]/div[1]/input[1]"
#----------------------------------------Frequency of soaking vary with Temperature------------------------------
        SoakFreq_VT_no= "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[11]/div[4]/div/div[2]/div[1]/label"
        SoakFreq_VT_yes= "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[11]/div[4]/div/div[2]/div[2]/label"
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````
##____________________________________________| S H A D E |________________________________________

#----------------------------------------Soakers Located in Feeding Area---------------------------------------------- 
        Shade_FA_no = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[12]/div[2]/div[1]/div[2]/div[1]/label"
        Shade_FA_yes = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[12]/div[2]/div[1]/div[2]/div[2]/label"
#----------------------------------------Soakers Located in Resting Area---------------------------------------------- 
        Shade_RA_no = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[12]/div[2]/div[2]/div[2]/div[1]/label"
        Shade_RA_yes = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[12]/div[2]/div[2]/div[2]/div[2]/label"
#----------------------------------------AirCooling units used in Resting Area------------------------------------
        Shade_unit_no="//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[12]/div[2]/div[3]/div[2]/div[1]/label"
        Shada_unit_yes="//*[@id='top']/main/div[1]/div[1]/div/div[2]/div[12]/div[2]/div[3]/div[2]/div[2]/label"
#=======================================================================================================================================================

        
        select_fields = [
            Fan_FA_diamter,
            Fan_RA_diamter
            ]

        path_yes = {
             WA_yes : WA_yes,
             Warea_yes : Warea_yes,
             FL_FA_yes : FL_FA_yes,
             HVLS_FA_no : HVLS_FA_no,
             FL_RA_yes : FL_RA_yes,
             HVLS_RA_no : HVLS_RA_no,
             Soak_FA_yes : Soak_FA_yes,
             Soak_RA_yes : Soak_RA_yes,
             drop_yes : drop_yes,
             SoakFreq_VT_yes : SoakFreq_VT_yes,
             Shade_FA_yes : Shade_FA_yes,
             Shade_RA_yes : Shade_RA_yes,
             Shada_unit_yes : Shada_unit_yes
            }


        path_no = {
             WA_no : WA_no,
             Warea_no : Warea_no,
             FL_FA_no : FL_FA_no,
             FL_RA_no : FL_RA_no,
             Soak_FA_no : Soak_FA_no,
             Soak_RA_no : Soak_RA_no,
             Shade_FA_no :Shade_FA_no,
             Shade_RA_no : Shade_RA_no
            }

        path_N_A = {
             WA_no : WA_no,
             Warea_no : Warea_no,
             FL_FA_no : FL_FA_no,
             FL_RA_no : FL_RA_no,
             Soak_FA_no : Soak_FA_no,
             Soak_RA_no : Soak_RA_no,
             Shade_FA_no : Shade_FA_no,
             Shade_RA_no : Shade_RA_no,   
            }

        path_yes_no = {
            WA_no : WA_no,  
            Warea_no : Warea_no,
            FL_FA_yes : FL_FA_yes,
            HVLS_FA_yes: HVLS_FA_yes,
            FL_RA_yes : FL_RA_yes,
            HVLS_RA_yes : HVLS_RA_yes,
            Soak_FA_yes : Soak_FA_yes,
            Soak_RA_yes: Soak_RA_yes,
            drop_no: drop_no,
            SoakFreq_VT_no : SoakFreq_VT_no,
            Shade_FA_no : Shade_FA_no,
            Shade_RA_yes : Shade_RA_yes,
            Shade_unit_no : Shade_unit_no
            }