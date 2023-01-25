import os
from selene import have, be

from selene.support.shared import browser


def test_student_registration_form(open_page_form):
    browser.element('[id="firstName"]').type('Nikita')
    browser.element('[id="lastName"]').type('Kuznetsov')
    browser.element('[id="userEmail"]').type('mamintargetolog@gmail.com')
    gender_is_male = browser.element('[for = "gender-radio-1"]')
    gender_is_male.click()
    browser.element('[id="userNumber"]').type('81111111111')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    month_of_date_of_birth = browser.element('[value="10"]')
    month_of_date_of_birth.click()
    browser.element('.react-datepicker__year-select').click()
    year_of_date_of_birth = browser.element('[value="1991"]')
    year_of_date_of_birth.click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('[id="subjectsInput"]').type('Civ').press_enter().type('Comp').press_enter()
    hobby_is_sports = browser.element('[for = "hobbies-checkbox-1"]')
    hobby_is_sports.click()
    hobby_is_reading = browser.element('[for = "hobbies-checkbox-2"]')
    hobby_is_reading.click()
    hobby_is_music = browser.element('[for = "hobbies-checkbox-3"]')
    hobby_is_music.click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('resourses/Screenshot_2.jpg'))
    browser.element('[id="currentAddress"]').type('Россия, Москва, Свободный проспект 177')
    browser.element('[id="react-select-3-input"]').type('HAR').press_enter()
    browser.element('[id="react-select-4-input"]').type('PAN').press_enter()
    browser.element('[id="submit"]').press_enter()

    browser.elements('.modal-body tr').should(have.texts(
        'Label Values',
        'Student Name Nikita Kuznetsov',
        'Student Email mamintargetolog@gmail.com',
        'Gender Male',
        'Mobile 8111111111',
        'Date of Birth 19 November,1991',
        'Subjects Civics, Computer Science',
        'Hobbies Sports, Reading, Music',
        'Picture Screenshot_2.jpg',
        'Address Россия, Москва, Свободный проспект 177',
        'State and City Haryana Panipat'
    ))

