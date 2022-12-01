import sys;

class locators():
#======================ALL-TEST-DATA=====================================
#Valid - username/password data
    usernames = [
           ("zinprorepresentative@mailinator.com"),
           ("abbasAdvCustomer@mailinator.com"),
           ("abbasAdmin@mailinator.com"),
           ("abbasZinPro@mailinator.com"),
           ("moiz@mailinator.com")
           ]
    passwords=["12345678","Abbas@123"]

#InValid - username/password data
    invalid_usernames = [
        ('invalid')
        ]
    invalid_passwords = [
        ("invalid")
        ]

#Forget-Pass_Email
    forget_email= ["abbasAdmin@mailinator.com"]
    
#=======================ALL-XPATH-ELEMENTS-LOCATION=====================
#Login Page-Element username/password Xpaths---
    username_xpath = "//input[@id='email']"
    password_xpath = "//input[@id='password']";
    btn_xpath= "//button[@type='submit']";
    invalid_credential_msg_xpath="//div[@role='alert']"

#Logout - linkBtn---
    logout_xpath = "//a[text() = 'Log Out']"


#forget-pass - XPATHS---
    forget_link = "//a[@class='pull-right focus reset-password-link']"
    forget_email_path = "//input[@id='username']";
    forget_submit="//button[@type='submit']";
    forget_success_msg_path = "//div[@role='alert']"


#quick-Evaluations Xpath
    eval_quick_bton_xpath = "//a[normalize-space()='Quick Start Evaluation']"
#Herd-Evaluation_Xpath    
    herd_btn_xpath = "//a[@href = '/evaluations/new']"


#-------------quick-Evaluation------------------------|

    values=[("imperial"),("metric")]
    measurement_path = "//input[@value='{}']";
    Next_path = "//button[@class='btn btn-primary btn-full--sm mt-4 float-right']"
    assesor_sort_path = "//button[@class='btn btn-primary btn-block--xs pull-right']"
    

    locomotion_checkbox = "/html/body/div/main/div[1]/div[1]/div/div[2]/div/div[1]/div[5]/div[12]/div/label[1]/span"
    heat_abatement_checbox = "/html/body/div/main/div[1]/div[1]/div/div[2]/div/div[1]/div[5]/div[6]/div/label[1]/span"
    #Dirt_Alot_checkbox = "//div[@class='card-body card-body--group mt-4']//div[3]//div[1]//label[1]//span[1]"
    #Dirt_Alot_checkbox = "//*[@id='top']/main/div[1]/div[1]/div/div[2]/div/div[5]/div[3]/div/label[1]/span"
    Dirt_Alot_checkbox = "/html/body/div/main/div[1]/div[1]/div/div[2]/div/div[1]/div[5]/div[3]/div/label[1]/span"
    Bio_security = " /html/body/div/main/div[1]/div[1]/div/div[2]/div/div[1]/div[5]/div[2]/div/label[1]/span"
    
#---------------Herd-Evaluation-------------------------|
    herd_next_path = "//button[@class='btn btn-primary btn-full--sm float-right ml-0 ml-md-4 mt-2 mt-md-0 order-md-2']"
    herd_assessor_sort_path = "//button[@class='btn btn-primary btn-block--xs pull-right']"
   
    #---Company-----
    company_name = "//select[@name = 'company']"
    company_country = "//select[@name = 'company_country']"
    company_state = "//div[3]//div[5]//div[1]//select[1]"
    company_address = "//input[@name = 'company_address_line_1']"
    company_city = "//input[@name = 'company_city']"
    company_postal_code = "//input[@name = 'company_postal_code']"

    #----Dairy------
    dairy_name = "//select[@name = 'dairy_name']"
    dairy_country = "//select[@name = 'dairy_country']"
    dairy_state = "//div[5]//div[5]//div[1]//select[1]"
    dairy_address = "//input[@name = 'address_1']"
    dairy_city = "//input[@name = 'city']"
    dairy_postal_code = "//input[@name = 'postal_code']"

    #---Contact-----
    contact_name_select = "//select[@data-vv-as='Contact Name']"
    contact_email = "//input[@name='email_address_1']"
    contact_business_phone = "//input[@name='business_phone']"
    

    #---Characteristics----
    consultation_date = "//input[@name='consultation_date']"
    select_Date = "//span[@class='cell day selected today']"
    herd_size = "//input[@name='herd_size']"
    metric_measurement= "//input[@value='metric']"
    currency = "//select[@name='currency']"
    milk_production = "//input[@name='computed_milk_production']"
    milk_price = "//input[@name='computed_milk_price']"


