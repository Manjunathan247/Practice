from selenium import webdriver
import logging
from selenium.webdriver import ActionChains

logging.basicConfig(filename='assignmentTwo.log', filemode='a', level=logging.INFO,
                    datefmt='%d-%b-%y %H:%M:%S', format='%(asctime)s - %(levelname)s: %(message)s')

driver = webdriver.Chrome("Drivers/chromedriver.exe")
site_url = "https://www.rahulshettyacademy.com/AutomationPractice/"
implicit_wait = 15
driver.get(site_url)
driver.maximize_window()
driver.implicitly_wait(implicit_wait)

if driver.title == 'Practice Page':
    print("I am in Practice page")
else:
    print("I am not in Practice Page")

radiobutton_value = "radio2"
suggestion_value = "Indon"
static_value = "option2"
check_box_valueone = "option1"
check_box_valuetwo = "option3"
user_name = "Manjunathan"
open_window_child_name = "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"
open_tab_child_name = "Rahul Shetty Academy"
course_substring = "Selenium"
switch_textfield = driver.find_element_by_css_selector("#name")
elementdisplayed_textfield = driver.find_element_by_css_selector("#displayed-text")
hide_button = driver.find_element_by_css_selector("#hide-textbox")
show_button = driver.find_element_by_css_selector("#show-textbox")
mouse_hover = driver.find_element_by_css_selector("#mousehover")
mouse_hover_values = driver.find_elements_by_xpath("//div[@class='mouse-hover-content']/a")
# iframes = driver.find_elements_by_tag_name("iframe")
# urls = driver.find_elements_by_tag_name("a")


def radio_button(radio):
    radiobuttons = driver.find_elements_by_xpath("//div[@id='radio-btn-example']/fieldset/label/input")
    for radiobutton in radiobuttons:
        if radiobutton.get_attribute("value") == radio:
            radiobutton.click()
            assert radiobutton.is_selected()
            logging.info("Clicked on " + radio + "radio button")


def suggestion_dropdown(auto_dropdown):
    autosuggestion = driver.find_element_by_css_selector("#autocomplete")
    autosuggestion.send_keys(auto_dropdown)
    place = driver.find_element_by_xpath("//li[@class='ui-menu-item']")
    place_value = place.text
    if auto_dropdown in place_value:
        place.click()
    logging.info("Selected " + auto_dropdown + " from suggestion drop down")
    script = "return document.getElementById('autocomplete').value"
    actual_value = driver.execute_script(script)
    print("Value in Auto suggestion box is:" + actual_value)
    expected_value = "Indonesia"
    assert actual_value == expected_value


def static_dropdown(dropdown):
    staticdropdownlist = driver.find_element_by_css_selector("#dropdown-class-example")
    staticdropdownlist.click()
    options = staticdropdownlist.find_elements_by_tag_name("option")
    for option in options:
        if option.get_attribute("value") == dropdown:
            option.click()
    logging.info("Selected " + dropdown + " from static drop down")
    script = "return document.getElementById('dropdown-class-example').value"
    selected_value = driver.execute_script(script)
    print("Value in static drop down is :" + selected_value)
    assert selected_value == dropdown


def check_box(checkbox_value):
    checkboxes = driver.find_elements_by_xpath(
        "//legend[contains(text(),'Checkbox')]/following-sibling::label /input")
    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == checkbox_value:
            checkbox.click()
            assert checkbox.is_selected()
    logging.info("Selected " + checkbox_value + " from checkbox example")


def enter_textbox(name, element):
    element.send_keys(name)
    logging.info("Enter " + name + " in text field")


def switch_textbox(user_name_switch, textbox):
    enter_textbox(user_name_switch, textbox)
    logging.info("Switch To Alert Example field")


def get_alert():
    return driver.switch_to.alert


def alert_message():
    return get_alert().text


def alert_handle_accept(name):
    alert_button = driver.find_element_by_css_selector("#alertbtn")
    alert_button.click()
    assert name in alert_message()
    logging.info("Alert message is having " + name)
    get_alert().accept()
    logging.info("Clicked on accept button")


def alert_handle_cancel(name):
    confirm_button = driver.find_element_by_css_selector("#confirmbtn")
    confirm_button.click()
    assert name in alert_message()
    logging.info("Alert message is having " + name)
    get_alert().dismiss()
    logging.info("Clicked on dismiss button")


def switch_windows(window_id):
    driver.switch_to.window(window_id)


def switchto_parent():
    parent_window = driver.window_handles[0]
    switch_windows(parent_window)
    logging.info("Now control back to parent browser")
    parentwindow_title = driver.title
    logging.info("Title of the parent page is: " + parentwindow_title)
    assert parentwindow_title == 'Practice Page'


def switchto_child(window_title):
    childwindow = driver.window_handles[1]
    switch_windows(childwindow)
    logging.info("Now control in child browser")
    childwindow_title = driver.title
    logging.info("Title of the child page is: " + childwindow_title)
    assert childwindow_title == window_title
    driver.close()
    logging.info("Child browser is closed")
    switchto_parent()


def openwindow_action(child_name):
    window_button = driver.find_element_by_css_selector("#openwindow")
    window_button.click()
    logging.info("Clicked on Open window button")
    switchto_child(child_name)


def open_tab(tab_child_name):
    tab_button = driver.find_element_by_css_selector("#opentab")
    tab_button.click()
    logging.info("Clicked on Open tab button")
    switchto_child(tab_child_name)


def table_handle(text_in_course):
    courses = driver.find_elements_by_xpath("//table[@id='product']/tbody/tr/following-sibling::tr /td[2]")
    i = 0
    for course in courses:
        course_name = course.text
        if text_in_course in course_name:
            i += 1
            print(course_name)
    print("Number of courses having Selenium as substring is: " + str(i))
    logging.info("Number of courses having Selenium as substring is: " + str(i))


def elementdisplayed(name_display, element_displayed, elementhide, elementshow):
    enter_textbox(name_display, element_displayed)
    logging.info("Clicked on hide button")
    elementhide.click()
    assert not element_displayed.is_displayed()
    logging.info("Text box is not displayed")
    elementshow.click()
    logging.info("Clicked on show button")
    assert element_displayed.is_displayed()
    logging.info("Text box is displayed")
    script = "return document.getElementById('displayed-text').value"
    valueintextbox = driver.execute_script(script)
    assert valueintextbox == name_display


def mousehover_action(element, values):
    element.location_once_scrolled_into_view
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    logging.info("Mouse on Mousehover button")
    print("Options displayed when mouserhover on button:")
    for value in values:
        option = value.text
        print(option)


def switch_frame(frame_index):
    driver.switch_to.frame(frame_index)


def switch_defaultframe():
    return driver.switch_to.default_content()


def frame_handle():
    frames = driver.find_elements_by_tag_name("iframe")
    no_of_iframes = len(frames)
    print("Number of iframes in page: " + str(no_of_iframes))
    for frame in range(no_of_iframes):
        switch_defaultframe()
        switch_frame(frame)
        logging.info("control switching into iframe")
        urls_element = driver.find_elements_by_tag_name("a")
        no_of_urls = len(urls_element)
        print("Number of urls in frame: " + str(no_of_urls))
        print("List of urls in frame: ")
        for url in urls_element:
            urltext = url.get_attribute("href")
            if urltext is not None:
                print(str(urltext))
        switch_defaultframe()
        logging.info("Control back to main page")


def close_browser():
    logging.info("Close the browser")
    driver.close()


radio_button(radiobutton_value)
suggestion_dropdown(suggestion_value)
static_dropdown(static_value)
check_box(check_box_valueone)
check_box(check_box_valuetwo)
switch_textbox(user_name, switch_textfield)
alert_handle_accept(user_name)
switch_textbox(user_name, switch_textfield)
alert_handle_cancel(user_name)
openwindow_action(open_window_child_name)
open_tab(open_tab_child_name)
table_handle(course_substring)
elementdisplayed(user_name, elementdisplayed_textfield, hide_button, show_button)
mousehover_action(mouse_hover, mouse_hover_values)
frame_handle()
close_browser()
