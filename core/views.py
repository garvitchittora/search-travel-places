from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def selenium(string):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("useAutomationExtension", False)
    option.add_experimental_option("excludeSwitches",["enable-automation"])
    option.add_argument("disable-infobars");
    browser = webdriver.Chrome(executable_path='C:\\Users\\garvi\\Downloads\\chromedriver', options=option)
    browser.get("https://www.google.com/")
    names = browser.find_elements_by_xpath("//input[@class='gLFyf gsfi']")
    names[0].send_keys(string)
    python_button = browser.find_elements_by_xpath("//input[@class='gNO89b']")
    python_button[0].submit()
    browser.maximize_window()

def abc(request):
   text = """<h1>welcome to abc !</h1>"""
   return HttpResponse(text)	

def write_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main(request):
	if request.method=='POST':
		x = {}
		x['where']=request.POST['where']
		x['check_in']=request.POST['check_in']
		x['check_out']=request.POST['check_out']
		x['guest_no']=request.POST['guest_no']

		with open('data.json') as json_file:
		    data = json.load(json_file)
		    temp = data['pets']

		    y = {	
		    		"where":x['where'],
					"check_in":x['check_in'],
					"check_out":x['check_out'],
					"guest_no":x['guest_no']
			    }
		    temp.append(y)
		    string=x['where']+' check in '+x['check_in']+' check out '+x['check_out']+' guest number '+x['guest_no']
		write_json(data)
		selenium(string)
	return render(request, "form.html", {})
	        

