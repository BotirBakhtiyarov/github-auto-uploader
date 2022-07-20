from selenium import webdriver
from time import sleep
import os

cwd = os.getcwd()
print(cwd)
#For User
print("----------------------------------------------------------------------")
username = input("Please Enter your GitHub username: ")
print("----------------------------------------------------------------------")
password = input("Please Enter your GitHub password: ")
print("----------------------------------------------------------------------")
name_of_project = input("Please Enter your Project Name: ")
print("----------------------------------------------------------------------")


#For Auto make Repositories
#############################################################################################
driver = webdriver.Edge(r'D:\\test\\msedgedriver.exe') #change it to your webdriver path
#############################################################################################

driver.get("https://github.com")
#for enter GitHub website
sleep(5)
driver.find_element("xpath",'/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
#Input login details
sleep(3)
driver.find_element("xpath",'//*[@id="login_field"]').send_keys(username)
driver.find_element("xpath",'//*[@id="password"]').send_keys(password)
sleep(2)
driver.find_element("xpath",'/html/body/div[3]/main/div/div[4]/form/div/input[12]').click()

print("----------------------------------------------------------------------------------")
print("WARNING! You have  20 seconds for verify your account to enter from this Device...")
print("----------------------------------------------------------------------------------")
#############################################################################################
#make new repository_name
sleep(20)
driver.find_element("xpath",'/html/body/div[1]/header/div[6]/details/summary').click()
sleep(1)
driver.find_element("xpath",'/html/body/div[1]/header/div[6]/details/details-menu/a[1]').click()

#enter Repositories details
sleep(1)
driver.find_element("xpath",'//*[@id="repository_name"]').send_keys(name_of_project)
sleep(1)
driver.find_element("xpath",'/html/body/div[5]/main/div/form/div[5]/button').click()
sleep(2)
url = driver.find_element("xpath",'/html/body/div[5]/div/main/turbo-frame/div/div/git-clone-help/div[2]/div[2]/div/pre/span[1]/span').text


##############################################################################################

#print(url)#Repository url
print("----------------------------------------------------------------------")
for_readme = input("Input your README file text to here: ")
git_readme = 'echo "'+ for_readme +'" >> README.md'
#print(git_readme)
os.system('start /wait cmd /c '+git_readme+' ')
sleep(1)
git_init = 'git init'
#print(git_init)
os.system('start /wait cmd /c  '+git_init+' ')
sleep(1)
git_add = 'git add .'
#print(git_add)
os.system('start /wait cmd /c  '+git_add+' ')
sleep(1)
commit_name = '"first commit"'
git_commit = "git commit -m "+ commit_name
#print(git_commit)
os.system('start /wait cmd /c  '+git_commit+' ')
sleep(1)
branch_name = '"main"'
git_branch = "git branch -M "+branch_name
#print(git_branch)
os.system('start /wait cmd /c  '+git_branch+' ')
sleep(1)
git_remote = 'git remote add origin '+url
#print(git_remote)
os.system('start /wait cmd /c  '+git_remote+' ')
sleep(1)
git_push = 'git push -u origin '+branch_name
#print(git_push)
os.system('start /wait cmd /c  '+git_push+' ')

print("----------------------------------------------------------------------")
print("All is Done! Thanks you for using my Auto-Upload project")
print("----------------------------------------------------------------------")

driver.get("https://instagram.com/botir.bakhtiyarov/")
