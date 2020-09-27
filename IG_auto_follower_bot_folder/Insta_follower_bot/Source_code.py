# I'm using tkinter and selenium for making this bot!!
# and time module as well so as to set an interval between the process of following!

from tkinter import *
from selenium import webdriver                       
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

root = Tk()
root.resizable(width = False, height = False)
root.title("Insta_auto_follower_bot")
root.iconbitmap("myicon.ico")

username_label = Label(root, text = 'Username:')
username_label.grid(row = 0, column = 0, padx = 5, pady = 5)

pass_label = Label(root, text = "Password:")
pass_label.grid(row = 1, column = 0, padx = 5, pady = (0,5))

user_entry = Entry(root, width = 30)
user_entry.grid(row = 0, column = 1, padx = (0,5))

pass_entry = Entry(root, width = 30)
pass_entry.grid(row = 1, column = 1, padx = (0,5))

target_label = Label(root, text = "Target ID:")
target_label.grid(row = 2, column = 0, padx = 5, pady = (0,5))

target_entry = Entry(root, width = 30)
target_entry.grid(row = 2, column = 1, padx = (0,5))

def clicked():
	driver = webdriver.Chrome("chromedriver.exe")
	driver.maximize_window()
	driver.get("https://www.instagram.com/")

	try:
	    username = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.NAME, "username"))
	    )
	    username.send_keys(user_entry.get())

	    password = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.NAME, "password")) 
	    )
	    password.send_keys(pass_entry.get())
	    password.send_keys(Keys.RETURN)

	    notnow1 = WebDriverWait(driver, 10).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
	    )
	    notnow1.click()

	    notnow2 = WebDriverWait(driver, 10).until(
	        lambda x: x.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
	    )
	    notnow2.click()

	    searchid = WebDriverWait(driver, 10).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
	    )
	    searchid.send_keys(target_entry.get())
	    searchid.send_keys(Keys.RETURN)

	    clickid = WebDriverWait(driver, 10).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
	    )
	    clickid.click()

	    clickfollowers = WebDriverWait(driver, 10).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
	    )
	    clickfollowers.click()

	    for i in range(50):

	        time.sleep(5)
	        following = WebDriverWait(driver, 1000).until(
	            lambda x: x.find_element_by_xpath("//*[text()='Follow']")
	        )
	        following.click()
	                                  
	finally:     
	    driver.quit() 

activate_button = Button(root, text = "Activate", command = clicked)
activate_button.grid(row = 3, column = 0, columnspan = 2, pady = 5)

root.mainloop()