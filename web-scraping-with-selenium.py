from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://upmedia.movie/")
movie_name = input("Enter your movie name:")
# print(movie_name)

search_box = driver.find_element(By.CSS_SELECTOR, ".search.left.rt-8px input")
# print(search_box)
search_box.send_keys(movie_name, Keys.RETURN)
# print(driver.current_url)

search_movieName_url = driver.current_url + "?s=" + movie_name
driver.get(search_movieName_url)
print(driver.current_url)

movie_articles = driver.find_elements(By.CLASS_NAME, "mini-p rt rt-relative rt-overflow")
print(len(movie_articles))


