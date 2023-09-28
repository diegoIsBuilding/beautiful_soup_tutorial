#Import Beautiful Soup
from bs4 import BeautifulSoup

#Access home.html with bs4 file objects
''' The open() function opens a file and returns it as a file object

    The 'with statement in Python helps with resourse management
    It make sure that you dont accidently leave any resource open
    
    Traditionally: 
    The same statement below would be written as 
    file = open('home.html', 'r')
    
    try:
        content = file.read(-1)
    finally:
        file.close()
        
print(content)'''
with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    #Create an instance of beautiful soup
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_= 'card')
    for course in course_cards:
        course_name = course.h3.text
        course_button = course.button.text
        
        print(course_name)
        print(course_button)
    
    
    
    
    #print(course_cards)
    #print(course_html_tags)
    #print(content) #Returns the html file contents in a string
    