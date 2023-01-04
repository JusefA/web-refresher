#the code was made to be able to redeem an item in valorant...
while True:
    if any(["Puffy" in h1.text.replace('\uFEFF', "") for h1 in driver.find_elements_by_class_name("https://redeem.playvalorant.com/")]):
        break
    else:
        driver.refresh
driver.find_element_by_xpath("//*[contains(., 'Puffy')]").click()