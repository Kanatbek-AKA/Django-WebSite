from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create  a simple html page as a string
def index(request):
   template = "<html>" \
                "<head>" \
                  "<meta charset='utf-8'/>" \
                "</head>" \
                "<body>" \
                "<nav style='margin-top:30px; margin-left:30px; border: thin solid green; width:90px; background:lightcyan; height:20px;'> <a href='/week1/handson/exercise1/' style='padding:5px; text-decoration:none; font-weight:bold;'>Next page</a> </nav>" \
                "<header>" \
                  "<h1 style='margin-left:30px;'>This is your first Django App created in string i.e. no templates used.<h1/>" \
                "</header>" \
                 "<div>" \
                   "<input id='test-btn' type='button' value='Click Me' style='background:blue; color:white; opacity: 0.5; cursor:pointer;'/>" \
                    "<br />" \
                    "<div class='disp' style='color:red; font-weight:normal; margin-left:30px;'></div>" \
                    "<script>" \
                       "window.onload = function() {" \
                          "document.getElementById('test-btn').addEventListener('click', () => {" \
                            "document.querySelector('.disp').textContent = 'I am your text running on JavaScript. Awesome! 😁'; " \
                            "document.querySelector('.disp').style.fontSize = '18px';  " \
                            "document.querySelector('.disp').style.marginTop = '10px'; " \
                          "})" \
                       "}" \
                    "</script>" \
                "</div>" \
                "</body>" \
              "</html>"
   return HttpResponse(content=template)

# Add current date
from datetime import date     # import built-in function date from package datetime 
def get_date(request):
  today = date.today()        
  template = """<html> 
                 <nav style='width:60px; margin-top:30px; margin-left:30px; border: thin solid green; background:lightcyan;  height:20px;'> <a href='/week1/handson/' style='padding:5px; margin:5px; color:black; text-decoration:none;'>Home</a> </nav> 
                 <header> 
                    <h1 style='margin-left:30px;'>This is your header header on date page? <h1/> 
                    <p style='margin-left:30px;'>Today\'s  date is {} </p>
                 </header> 
             </html>""".format(today)

  return HttpResponse(content=template)
