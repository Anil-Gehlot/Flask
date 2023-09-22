

#  2.Application Discovery Behavior

'''

The --app option is used to specify how to load the application.

	when we run "flask run" Flask starts a simple built-in web server to run our application. 

 	This server is helpful for testing your application during development, but it's not suitable for a production environment. 
 	In production, you would use a more robust web server like Nginx or Apache.

	when we run flask command, we can view our application on 'http://127.0.0.1.5000/' this local address.

	port conflict: if another application is already running on 5000 port then we will get  "OSError: [Errno 98]" on Unix system     
  	and "OSError: [WinError 10013]" on Windows.

    to handle this we can specify ports like 'flask run --port 8080 '





'''
