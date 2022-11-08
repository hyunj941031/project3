from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import os

import pandas as pd
import csv

# columns = ['CITY', 'LOCATION', 'HOTEL', 'GRADE', 'RATE', 'REVIEWS', 'WEEKDAY_PRICE', 'WEEKDAY_DATE', 'FRIDAY_PRICE', 'FRIDAY_DATE', 'SATURDAY_PRICE', 'SATURDAY_DATE', 'SUNDAY_PRICE', 'SUNDAY_DATE']
# with open('hotels.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(columns)

DB_FILENAME = 'Hotel_DB_API.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('./chromedriver', options=options)

try:
    driver.get('https://dailyhotel.com')
    driver.implicitly_wait(time_to_wait=10)
    # elem = driver.find_element_by_class_name('icons-inner').click()
    # time.sleep(1)
    # elem = driver.find_element_by_class_name('search-input-box').click()
    # time.sleep(1)
    # elem = driver.find_element_by_xpath('//div[@class="ui input full-width bg-gray icon"]/input')
    # elem.send_keys("강릉")
    # time.sleep(1)
    # elem.send_keys(Keys.RETURN)
    # time.sleep(1)
    # elem = driver.find_element_by_tag_name('button').click()
    elem = driver.find_element_by_css_selector('#root > div:nth-child(2) > div.Styled__ShortCutWrapper-sc-16jx7y3-0.bSEMmy > div > div:nth-child(1)').click()
    time.sleep(0.5)
    
    elem = driver.find_element_by_css_selector('#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-right-pane > div:nth-child(1)')
    cities = elem.find_elements_by_xpath('.//div')
#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div.Styled__LocalPaneLeftSideItem-sc-sk0kbc-5.fUXuSh > div

#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div.Styled__LocalPaneLeftSideItem-sc-sk0kbc-5.fUXuSh
#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div:nth-child(2)
#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div.Styled__LocalPaneLeftSideItem-sc-sk0kbc-5.fUXuSh > div
#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div:nth-child(3) > div
    city_name = '서울'
    for city_i in range(1, len(cities)+2):
        time.sleep(3)
        city = driver.find_element_by_css_selector('#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div:nth-child(' + str(city_i) + ') > div')
        #root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div:nth-child(7) > div
        #root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-left-pane > div:nth-child(7) > div
        city.click()
        city_name = city.text
        print(city_name)
        elem = driver.find_element_by_css_selector('#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-right-pane')
        locations = elem.find_elements_by_xpath('.//div/div')
        print(len(locations))
        for location_i in range(1, len(locations)):
            try:
                location = driver.find_element_by_css_selector('#root > div.region-wrap.slide-up-enter-done > div.Styled__TabWrapper-sc-sk0kbc-0.jxOAHr > div.Styled__Pane-sc-sk0kbc-1.iPMOom > div > ul.list-wrapper.province-right-pane > div:nth-child(' + str(location_i) + ')')
            except:
                driver.find_element_by_css_selector('#root > div.region-wrap.slide-up-enter-done > div.navbar > img').click()
                break
            loc_name = location.text
            print(loc_name)
            location.click()
            time.sleep(1)
            try:
                elem = driver.find_element_by_xpath('//div[contains(text(), "호텔") and @class="menu-item"]').click()
                time.sleep(1)
            except:
                driver.find_element_by_css_selector('#root > div.stay-wrapper > div > div:nth-child(2) > div.sub-navbar-wrapper > div.sub-navbar > div > div:nth-child(1) > div').click()
                time.sleep(1)
                continue

            try:
                elem = driver.find_element_by_xpath('//div[contains(text(), "전체") and @class="section-title"]')
            except:
                driver.find_element_by_css_selector('#root > div.stay-wrapper > div > div:nth-child(2) > div.sub-navbar-wrapper > div.sub-navbar > div > div:nth-child(1) > div').click()
                continue
            #root > div.stay-wrapper > div > ul > div:nth-child(4) > div > li:nth-child(2)
            div_sec = driver.find_elements_by_class_name('container')
            sec_num = len(div_sec)

            sec_li = driver.find_element_by_css_selector('#root > div.stay-wrapper > div > ul > div:nth-child(' + str(sec_num) + ') > div')

            room_li = sec_li.find_elements_by_xpath('./li')
            data_list = []
            for i in range(2, len(room_li)+2):
                time.sleep(1)
                try:
                    li = driver.find_element_by_css_selector("#root > div.stay-wrapper > div > ul > div:nth-child(" + str(sec_num) + ") > div > li:nth-child(" + str(i) + ") > div.hotel-sale-item-inner")
                except:
                    break
                grade_path = li.find_element_by_class_name('grade')
                grade = grade_path.text

                image = li.find_element_by_tag_name('img').get_attribute('src')
                try:
                    reviews = grade_path.find_element_by_xpath('../div[@class="review-count"]/span/span').text
                    reviews = int(re.sub(r"[^0-9]", "", reviews))
                except:
                    reviews = 0

                try:
                    rate = li.find_element_by_class_name('rating').text
                    rate = int(rate[:-1])
                except:
                    rate = 0

                # if rate >= 85 or reviews >= 1000 or '특' in grade:
                check = li.find_element_by_xpath('.//div[@class="inner-price"]').text
                tel_name_path = li.find_element_by_xpath('.//div[@class="name"]')
                tel_name = tel_name_path.text
                driver.execute_script('arguments[0].click()', li)
                # li.click()
                time.sleep(3)
                try:
                    if len(check) < 5:
                        driver.find_element_by_xpath('//button[contains(text(), "취소") and @type="button"]').click()
                except:
                    pass
                time.sleep(2)
                driver.find_element_by_class_name('inner').click()
                time.sleep(1)
                table_list = driver.find_elements_by_tag_name('table')

                prices_weekday = []
                prices_friday = []
                prices_saturday = []
                prices_sunday = []

                skip = 0
                for k, table in enumerate(table_list):
                    if k > 2:
                        break
                    tr_list = table.find_elements_by_tag_name('tr')
                    
                    for tr in tr_list:
                        td_list = tr.find_elements_by_tag_name('td')
                        for j, td in enumerate(td_list):
                            try:
                                price_path = td.find_element_by_tag_name('span')
                                price = price_path.text
                                # print(price)
                                day = td.find_element_by_class_name("custom-date").text
                                day = day.split('\n')[0]
                                # print(day)
                            except:
                                price = 0
                           
                            month = driver.find_element_by_css_selector('#root > div:nth-child(2) > div > div.stay-wrap > div.datepicker-wrap.calendar-wrapper.price-cal.slide-up-enter-done > div.datepicker > div > div > div > div.DayPicker_focusRegion.DayPicker_focusRegion_1 > div > div.CalendarMonthGrid.CalendarMonthGrid_1.CalendarMonthGrid__vertical_scrollable.CalendarMonthGrid__vertical_scrollable_2 > div:nth-child(' + str(k+1) + ') > div > div > strong').text
                            # print(month)
                            if price:
                                skip = 0
                                price = int(re.sub(r"[^0-9]","", price))
                                if j == 0:
                                    prices_sunday.append([price, month, day])
                                elif j < 5:
                                    prices_weekday.append([price, month, day])
                                elif j == 5:
                                    prices_friday.append([price, month, day])
                                elif j == 6:
                                    prices_saturday.append([price, month, day])
                            else:
                                skip += 1
                        if skip >= 7:
                            break
                    if skip >= 7:
                        break

                prices_weekday.append([100000000, '0000.00', '0'])
                prices_sunday.append([100000000, '0000.00', '0'])
                prices_friday.append([100000000, '0000.00', '0'])
                prices_saturday.append([100000000, '0000.00', '0'])

                prices_weekday.sort(key=lambda x:x[0])
                prices_sunday.sort(key=lambda x:x[0])
                prices_friday.sort(key=lambda x:x[0])
                prices_saturday.sort(key=lambda x:x[0])

                min_weekday = prices_weekday[0]
                min_sunday = prices_sunday[0]
                min_saturday = prices_saturday[0]
                min_friday = prices_friday[0]

                data_list.append([city_name, loc_name, tel_name, grade, rate, reviews, min_weekday, min_friday, min_saturday, min_sunday, image])

                elem = driver.find_element_by_class_name('navbar')
                elem.find_element_by_xpath('//div[@class="navbar"]/img').click()
                driver.back()
                time.sleep(4)

                print(city_name, loc_name, tel_name)

                week_date = min_weekday[1] + '.' + min_weekday[2]
                fri_date = min_friday[1]+ '.' + min_friday[2]
                sat_date = min_saturday[1]+ '.' + min_saturday[2]
                sun_date = min_sunday[1]+ '.' + min_sunday[2]
                with open('hotels.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([city_name, loc_name, tel_name, grade, rate, reviews, min_weekday[0], week_date, min_friday[0], fri_date, min_saturday[0], sat_date, min_sunday[0], sun_date, image])
            driver.find_element_by_css_selector('#root > div.stay-wrapper > div > div:nth-child(2) > div.sub-navbar-wrapper > div.sub-navbar > div > div:nth-child(1) > div').click()

        
    
    
except Exception as e:
    print(e)
finally:
    driver.quit()



