#! /usr/bin/env python
'''
    Program: Push data to AWS Dynamo DB
    Author: Vignesh Natarajan (www.vikilabs.in)
    
'''


from selenium import webdriver
import time
import inspect
import parse_foursquare_csv as fs

close_browser_on_error = False
encountered_error = False

def lineno():
    return inspect.currentframe().f_back.f_lineno

def init_browser():
    global driver
    driver = webdriver.Firefox()

def aws_login():
    global encountered_error
    global driver
    time.sleep(2)

    try:
        driver.get('https://ap-southeast-1.console.aws.amazon.com/console/home')
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    time.sleep(4)

    try:
        loginBox = driver.find_element_by_xpath("//input[@id='resolving_input']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", loginBox)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    loginBox.send_keys('614110936296')
    time.sleep(2)

    try:
        nxt = driver.find_element_by_id('next_button')
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", nxt)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    nxt.click()
    time.sleep(2)

    try:
        un = driver.find_element_by_xpath("//input[@id='username']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", un)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    un.send_keys('user_name')
    time.sleep(2)

    try:
        pwBox = driver.find_element_by_xpath("//input[@id='password']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", pwBox)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    pwBox.send_keys('password')
    time.sleep(2)

    try:
        pnxt = driver.find_element_by_xpath("//a[@id='signin_button']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", pnxt)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    pnxt.click()
    time.sleep(4)

def enter_menu_services():
    global encountered_error
    global driver

    time.sleep(6)

    try:
        services_menu = driver.find_element_by_xpath("//div[@class='nav-elt-label' and contains(text(), 'Services')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", services_menu)
        time.sleep(4)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    services_menu.click()
    time.sleep(4)

def enter_option_dynamo_db():
    global encountered_error
    global driver
    time.sleep(2)

    try:
        option_dynamo_db = driver.find_element_by_xpath("//span[contains(text(), 'DynamoDB')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", option_dynamo_db)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    option_dynamo_db.click()
    time.sleep(4)

    try:
        table = driver.find_element_by_xpath("//a[@id='ddbv2-shortcut-tables-link']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", table)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    table.click()
    time.sleep(4)

#Enterng table Main Restaurant Photos
def enter_table():
    global encountered_error
    global driver
    time.sleep(2)

    try:
        res_details = driver.find_element_by_xpath("//a[contains(text(), 'MainRestaurantMenuDetails')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", res_details)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        #Get the nearest ancestor from bottom who has the tag <tbody>
        ancestor1 = res_details.find_element_by_xpath("ancestor::tbody[1]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ancestor1)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        child1 = ancestor1.find_element_by_xpath("child::tr[7]/td[1]/div/label")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", child1)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click checkbox "MainRestaurantMenuDetails"
    child1.click()
    time.sleep(4)

def select_item_tab():
    global encountered_error
    global driver
    time.sleep(2)

    try:
        items_tab = driver.find_element_by_xpath("//div[@id='ddbv2-tabs-items']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", items_tab)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Select Items Tab
    items_tab.click()
    time.sleep(2)

def select_query_drop_down():
    global encountered_error
    global driver
    time.sleep(2)

    try:
        scan_query_dropdown = driver.find_element_by_xpath("//select[@id='ddbv2-scan-query-operation-type-drop-down']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", scan_query_dropdown)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        query = scan_query_dropdown.find_element_by_xpath("child::option[2]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", query)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Select Query Drop Down
    query.click()
    time.sleep(2)

def scroll_scan_table_down():
    global encountered_error
    global driver

    time.sleep(2)

    try:
        #@ class ='GK-UOA4CANB' and
        table = driver.find_element_by_xpath("//div[@id='ddbv2-scan-query-view']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", table)
        time.sleep(2)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        #@ class ='GK-UOA4CANB' and
        table1 = table.find_element_by_xpath("ancestor::div[2]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", table1)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    time.sleep(4)


    try:
        #Scroll Table1 Down By 15 Offset (Pixels)
        driver.execute_script("arguments[0].scrollBy(0, 15);", table1)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

scrolled = False

def search_restaurant_by_id(restaurant_id):
    global scrolled
    #Write your parsing stuffs
    global encountered_error
    global driver
    time.sleep(1)

    try:
        value_textbox = driver.find_element_by_xpath("//input[@id='ddbv2-scan-query-primary-sort-key-attribute-value-text-field']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", value_textbox)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Clear Value Text Box
    value_textbox.clear()
    time.sleep(1)

    #Enter Restaurant ID
    value_textbox.send_keys(restaurant_id)
    time.sleep(1)

    if scrolled == False:
        #Need to scroll down to find  the search Button
        scroll_scan_table_down()
        time.sleep(4)
        scrolled = True

    try:
        search_button = driver.find_element_by_xpath("//button[@id='ddbv2-scan-query-start-button']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", search_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click Search Button
    search_button.click()
    time.sleep(1)

def select_restaurant_id_from_search_results(res_id):
    global encountered_error
    global driver

    locator = "//div/a[contains(text(), '" + res_id + "')]"

    time.sleep(4)

    # /label
    try:
        # @ class ='GK-UOA4CANB' and
        div = driver.find_element_by_xpath(locator)
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", div)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # /label
    try:
        # @ class ='GK-UOA4CANB' and
        checkbox = div.find_element_by_xpath("ancestor::tbody[1]/tr[1]/td[1]/div/label")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", checkbox)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Select restaurant id from search results
    checkbox.click()
    time.sleep(2)

def edit_restaurant_info():
    global encountered_error
    global driver

    time.sleep(1)

    #/label
    try:
        #@ class ='GK-UOA4CANB' and
        actions_button = driver.find_element_by_xpath("//button[@id='ddbv2-items-action-menu-button']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", actions_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click the Action Button
    actions_button.click()
    time.sleep(1)

    try:
        #@ class ='GK-UOA4CANB' and
        edit_option = driver.find_element_by_xpath("//td[@id='ddbv2-items-edit-item-button']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", edit_option)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Edit Restaurant ID
    edit_option.click()
    time.sleep(1)


def insert_string(key, value):
    global encountered_error
    global driver
    time.sleep(1)

    try:
        plus_button = driver.find_element_by_xpath("(//button[@title='Click to open the actions menu (Ctrl+M)'])[1]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", plus_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click the + button
    plus_button.click()
    time.sleep(1)

    try:
        ibutton = driver.find_element_by_xpath("//button[@class='insert' and @title='Select the type of the field to be inserted before this field']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ibutton)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click the insert button
    ibutton.click()
    time.sleep(1)


    try:
        string_option = driver.find_element_by_xpath("//button[@class='type-string' and contains(@title, 'This is a String with quotes around it')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", string_option)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click String to insert
    string_option.click()
    time.sleep(1)

    try:
        field_box = driver.find_element_by_xpath("//div[@class='field empty' and @contenteditable='true']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", field_box)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    field_box.click()
    time.sleep(1)

    #Enter a Key to insert
    field_box.send_keys(key)
    time.sleep(1)


    try:
        value_box = driver.find_element_by_xpath("//div[@class='value empty' and @contenteditable='true']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", value_box)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    value_box.click()
    time.sleep(1)

    #Enter a value to insert
    value_box.send_keys(value)
    time.sleep(1)



def insert_record(key, value):
    global encountered_error
    global driver

    time.sleep(1)

    locator = "//div[@class='field'and contains(text(), '"+key+"')]"

    try:
        record = driver.find_element_by_xpath(locator)
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", record)
        time.sleep(1)
    except:
        print "ADDING NEW [ "+key+" ]"
        insert_string(key, value)
        time.sleep(1)

def delete_record(key):
    global encountered_error
    global driver

    time.sleep(1)

    locator = "//div[@class='field'and contains(text(), '"+key+"')]"

    try:
        record = driver.find_element_by_xpath(locator)
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", record)
        time.sleep(1)
    except:
        #print "RECORD NOT FOUND, CREATE NEW [ "+key+" ]"
        return

    try:
        ancestor1 = record.find_element_by_xpath("(ancestor::table[1])")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ancestor1)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        ancestor2 = ancestor1.find_element_by_xpath("(ancestor::tr[1])")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ancestor2)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        button_record = ancestor2.find_element_by_xpath("child::td[2]/button")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", button_record)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Click the + Button
    button_record.click()
    time.sleep(1)

    try:
        delete_button = ("//button[@class='remove' and @title='Remove this field (Ctrl+Del)']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", record)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Delete Record
    delete_button.click()
    time.sleep(1)

def insert_map(map_name):
    global encountered_error
    global driver
    time.sleep(1)

    #Search the insert button again to identify the Map Button
    try:
        ibutton1 = driver.find_element_by_xpath("//button[@class='insert' and @title='Select the type of the field to be inserted before this field']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ibutton1)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        ancestor1 = ibutton1.find_element_by_xpath("ancestor::li[@class=' selected']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ancestor1)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        map_button = ancestor1.find_element_by_xpath(".//button[@class='type-object' and contains(@title, 'This is a map which contains unordered key-value pairs.')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", map_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return


    #Click Map Button
    map_button.click()
    time.sleep(1)

    try:
        field_box = driver.find_element_by_xpath("//div[@class='field empty' and @contenteditable='true']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", field_box)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    field_box.click()
    time.sleep(1)
    # Enter a Key to insert
    field_box.send_keys(map_name)

def append_list_under_map(map_name, list_name):
    global encountered_error
    global driver
    time.sleep(1)

    locator = "//div[contains(text(), '"+map_name+"') and @class='field' and @contenteditable='true']"

    try:
        timeframes = driver.find_element_by_xpath(locator);
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", timeframes)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        next_row = timeframes.find_element_by_xpath("ancestor::table[1]/ancestor::tr[1]/following-sibling::tr")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", next_row)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        #[@title='Click to open the actions menu (Ctrl+M)']
        plus_button = next_row.find_element_by_xpath(".//button[@class='contextmenu' and contains(@title, 'Click to open the actions menu (Ctrl+M)')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", plus_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click Plus Button
    plus_button.click()
    time.sleep(1)

    try:
        append_button = driver.find_element_by_xpath("//button[@class='append' and contains(@title, 'Select the type of the field to be appended after this field')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", append_button)
        time.sleep(1)
    except:
        try:
            append_button = driver.find_element_by_xpath("//button[contains(@class,'insert') and @title='Select the type of the field to be inserted before this field']")
            print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", append_button)
        except:
            print "ERROR : ", lineno()
            encountered_error = True
            close_browser()
            return


    # Click Append Button
    append_button.click()
    time.sleep(1)

    try:
        li_selected = driver.find_element_by_xpath("//li[@class=' selected']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", li_selected)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        list_button = li_selected.find_element_by_xpath(".//button[contains(@class, 'type-array') and contains(@title, 'This is a list which can have elements of various DynamoDB types(Binary, String, Number) .')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", list_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Click List Button
    list_button.click()
    time.sleep(1)

    try:
        field = driver.find_element_by_xpath("//div[@class='field empty' and @contenteditable='true']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", field)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Click Field TextBox
    field.click()
    time.sleep(1)

    #day_string = "FILLING_DAY_OF_THE_WEEK"

    # Enter Values in Field Text Box [List]
    field.send_keys(list_name)
    time.sleep(1)

def replace_list_value(from_value, to_value):

    locator = "//div[contains(@class, 'field') and contains(text(), '"+from_value+"')]"

    try:
        field = driver.find_element_by_xpath(locator)
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", field)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Click Field TextBox
    field.click()
    time.sleep(1)

    # Click Field TextBox
    field.clear()
    time.sleep(1)
    #day_string = "FILLING_DAY_OF_THE_WEEK"

    # Enter Values in Field Text Box [List]
    field.send_keys(to_value)
    time.sleep(1)


#Insert List Element from Descending Order to get Ascending Structure
def append_string_under_list(list_name, string_value):
    global encountered_error
    global driver
    time.sleep(1)

    locator = "//div[contains(text(), '"+ list_name + "')]"

    try:
        day_list = driver.find_element_by_xpath(locator)
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", day_list)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        next_row = day_list.find_element_by_xpath("ancestor::table[1]/ancestor::tr[1]/following-sibling::tr")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", next_row)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    try:
        #[@title='Click to open the actions menu (Ctrl+M)']
        plus_button = next_row.find_element_by_xpath(".//button[@class='contextmenu' and contains(@title, 'Click to open the actions menu (Ctrl+M)')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", plus_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click Plus Button
    plus_button.click()
    time.sleep(1)

    try:
        append_button = driver.find_element_by_xpath("//button[@class='append' and contains(@title, 'Select the type of the field to be appended after this field')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", append_button)
        time.sleep(1)
    except:
        time.sleep(1)
        try:
            append_button = driver.find_element_by_xpath("//button[@class='insert' and @title='Select the type of the field to be inserted before this field']")
            print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", append_button)
        except:
            print "ERROR : ", lineno()
            encountered_error = True
            close_browser()
            return

    # Click Append/Insert Button
    append_button.click()
    time.sleep(1)

    try:
        li_selected = driver.find_element_by_xpath("//li[@class=' selected']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", li_selected)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return


    try:
        string_button = li_selected.find_element_by_xpath(".//button[contains(@class, 'type-string') and contains(@title, 'This is a String with quotes around it')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", string_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Click String Button
    string_button.click()
    time.sleep(1)

    try:
        field = driver.find_element_by_xpath("//div[@class='value empty' and @contenteditable='true']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", field)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    # Click Field TextBox
    field.click()
    time.sleep(1)

    #time_string = "FOR_THIS_WEEK_DAY1_TIME1"

    stripped_string =  string_value.decode('utf-8').strip()
    print "Stripped String : ", stripped_string
    # Enter Values in Field Text Box [List]
    field.send_keys(stripped_string)
    time.sleep(1)

def aws_reorder_list(list):
    reordered_list = []
    l = len(list)
    last = True
    last_but_one = False
    for i in range(l-1, -1, -1):
        if last:
            reordered_list.append(list[i-1])
            reordered_list.append(list[i])
            last = False
            last_but_one = True
            continue

        if last_but_one:
            last_but_one = False
            continue

        reordered_list.append(list[i])

    print reordered_list
    return reordered_list

def fill_restaurant_open_timings(map_name, day_of_week, timing_list):

    append_list_under_map(map_name, "RES_OPEN_DAY")

    if timing_list != 0:
        r_time_list = aws_reorder_list(timing_list)
        for item in r_time_list:
            if item:
                print "RES TIMING ", item
                append_string_under_list("RES_OPEN_DAY", item)  #Last But 1 to first item

    replace_list_value("RES_OPEN_DAY", day_of_week) #Last But one [Info filled from sun to sat]


def insert_open_hours(restaurant_open_times):
    global encountered_error
    global driver
    time.sleep(1)

    try:
        plus_button = driver.find_element_by_xpath("(//button[@title='Click to open the actions menu (Ctrl+M)'])[1]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", plus_button)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click the + button
    plus_button.click()
    time.sleep(1)

    try:
        ibutton = driver.find_element_by_xpath("//button[@class='insert' and @title='Select the type of the field to be inserted before this field']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", ibutton)
        time.sleep(1)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    #Click the insert button
    ibutton.click()
    time.sleep(1)

    map_name = 'timeframes'
    list_name = 'RES_OPEN_DAY1'
    string_value = 'RES_OPEN_DAY_TIME1'

    #Insert MAP timeframes
    insert_map(map_name)

    #Days : Parse in order "last but one day to first day" [Res Info Will be filled Sun to Sat in AWS]
    day_of_week = ['fri', 'sat', 'thu','wed','tue','mon', 'sun']

    for o_day in day_of_week:
        timing_list = restaurant_open_times[o_day]
        fill_restaurant_open_timings(map_name, o_day, timing_list)


def save_table(res_id):
    global encountered_error
    global driver
    time.sleep(1)

    # Save Form
    try:
        save_button = driver.find_element_by_xpath("//button[@id='cmn-confirm-btn']")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", save_button)
    except:
        print "ERROR : ", lineno()
        encountered_error = True
        close_browser()
        return

    save_button.click()
    time.sleep(1)

    ctrl_bit = False

    # Error Check
    try:
        error_check = driver.find_element_by_xpath("//div[contains(text(), 'ConditionalCheckFailedException')]")
        print "Current Syntax : ", driver.execute_script("return arguments[0].outerHTML", error_check)
        time.sleep(1)

        print "[ERROR] Save Failed, ", res_id

        # Click Cancel [Only if ConditionalCheckFailedException found the control comes here]
        cancel_button = driver.find_element_by_xpath("//a[@class='gwt-Anchor GK-UOA4CNWD mcancel' and contains(text(), 'Cancel')]")
        cancel_button.click()
        time.sleep(1)
        ctrl_bit = True

    except:
        if ctrl_bit:
            # CANCEL FAILED, UNABLE
            print "CANCEL Failure, ", res_id
            print "Error Unable to find cancel button"
            return
        else:
            # Previous SAVE WAS Successful
            print "Save Successful, ", res_id
            return


def close_browser():
    global driver
    global encountered_error
    global close_browser_on_error

    if encountered_error == True:
        if close_browser_on_error == True:
            driver.quit()
    else:
        driver.quit()

    exit()

def parse_list_and_append_maplist(from_list, to_map, key):
    if from_list:
        for item in from_list:
            to_map[key].append(item)
            #print "item ", item

if __name__ == '__main__':
    driver=""

    fs.get_records_from_foursquare_csv()

    #10 Unccessful 4bd116ef41b9ef3be984fbe5
    #118 Unsuccessful 4cfddc50d8468cfadca5026c
    #142 50d6c970e4b04490b9a5c287
    #241 56559d63498ef88692e0d7ea
    #242
    end = len(fs.mon)
    start = 243

    #'''
    init_browser()
    aws_login()
    enter_menu_services()
    enter_option_dynamo_db()
    enter_table()
    select_item_tab()
    select_query_drop_down()

    #'''

    for i in range(start, end):
        day_open_info = {}
        day_open_info['mon'] = []
        day_open_info['tue'] = []
        day_open_info['wed'] = []
        day_open_info['thu'] = []
        day_open_info['fri'] = []
        day_open_info['sat'] = []
        day_open_info['sun'] = []

        print i, fs.rest_id[i], fs.url[i], fs.contact[i], fs.locality[i], fs.price[i]
        print "Open ", "SUN : ", fs.sun[i], ", MON : ", fs.mon[i], ", TUE :", fs.tue[i],
        print ", WED : ", fs.wed[i], ", THU : ", fs.thu[i], ", FRI : ", fs.fri[i], ", SAT : ", fs.sat[i]

        parse_list_and_append_maplist(fs.get_open_timing_list(fs.mon[i]), day_open_info, 'mon')
        parse_list_and_append_maplist(fs.get_open_timing_list(fs.tue[i]), day_open_info, 'tue')
        parse_list_and_append_maplist(fs.get_open_timing_list(fs.wed[i]), day_open_info, 'wed')
        parse_list_and_append_maplist(fs.get_open_timing_list(fs.thu[i]), day_open_info, 'thu')
        parse_list_and_append_maplist(fs.get_open_timing_list(fs.fri[i]), day_open_info, 'fri')
        parse_list_and_append_maplist(fs.get_open_timing_list(fs.sat[i]), day_open_info, 'sat')
        parse_list_and_append_maplist(fs.get_open_timing_list(fs.sun[i]), day_open_info, 'sun')

        #print "DAY OPEN ", day_open_info

        restaurant_id = fs.rest_id[i]
        restaurant_url = fs.url[i]
        restaurant_contact = fs.contact[i]
        restaurant_locality = fs.locality[i]
        restaurant_price = fs.price[i]

        #'''
        search_restaurant_by_id(restaurant_id)
        select_restaurant_id_from_search_results(restaurant_id)
        edit_restaurant_info()

        if restaurant_contact:
            insert_record("contact", restaurant_contact)

        if restaurant_locality:
            insert_record("locality", restaurant_locality)

        if restaurant_price:
            insert_record("price", restaurant_price)

        if restaurant_url:
            insert_record("url", restaurant_url)

        insert_open_hours(day_open_info)
        save_table(restaurant_id)
        #'''

    #close_browser()
    time.sleep(1)

