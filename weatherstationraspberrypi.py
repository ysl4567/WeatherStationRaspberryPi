#import various python libraries as well as sensehat libraries 
import time
from sense_hat import SenseHat
import smtplib
from datetime import datetime

#clearing SenseHat() each time the code runs
sense = SenseHat()
sense.clear

#defining a variable
def sendmail (from_addr, to_addr_list, cc_addr_list, subject, messaage, login, password, smtpserver):


#setting up the formatting of the email
    header = 'From: %s \n' % from_addr 
    header += 'To: %s \n' % join (to_addr_list)
    header += 'CC: %s \m' % ','.join (cc_addr_list)
    header += 'Subject: %s \n \n' % subject
    mesesage = header + message


#calling up smtp server. These are all SMTP specific functions
#starttls is "a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS
    server= smtplib.SMTP (smtpserver)
    server.starttls()
    server,login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

#a variable 'average_temp' returns the av temp based on the humidity and pressure readings. The return means it will show the value     
def average_temp():
    temp1=sense.get_temperature_from_humidity()
    temp2=sense.get_temperature_from_pressure()
    
    return (temp1+temp2)/2


#a variable 'weather_report_display'. There are several parameters inside of the parenthesis. The message head is the formatting.   
def weather_report_display(hour=[], temp=[], humidity=[], pressure=[] ):
    message_head = 'Time        ' + 'Temperature' + 'Humidity'\
                   + 'Pressure' + '\n' +53 * '-' + '\n'
    message = ''

#a 'for' loop. The formatting and will show the values. 
    for x,y in enumerate(hour):
        message = message + '{0:20s} | {1:^10s} | {2:10s} | {3:^10a}'.format(
            hour[x],temp[x],humidity[x],pressure[x]) + '\n'
    message = message_header + message
    return message

#who to send the email to, the "send", "cc" and "subject" part of a normal email
    from_email = 'sudo.nano.etc.ssmtp.ssmtp@gmail.com'
    recipients_list = ['-' ]
    cc_list = ['-']
    subject = "Hourly Weather Report"
    username = 'sudo.nano.etc.ssmtp.ssmtp@gmail.com'
    password = 'Joemama'
    server = 'smtp.gmail.com:587'

    hour= []
    temp = []
    humidity = []
    pressure = []

#a "while" loop. While the length or the time value is less than 24 hours, it will run the code below.
#It will calculate the hour temp humidity and pressure

    while true:
        if len(hour)>24:
            hour = []
            temp = []
            humidity = []
            pressure = []
#once each variable is calculated, it will be rounded and added to the end of the string for formatting purposes. 
            hour.append (datetime.now().strftime('%Y-%m-%d %M:%M:%S'))
            temp.append(str(round(average_temp())))
            humidity.append(str(round(sense.get_humidity())))
            pressure.append(str(round(sense.get_pressure())))

#print in this specific order 
            message = weather_report_dsiplay(hour,temp.huimdty,pressure)
            print(message)
#next perform this function. using the email information above, deliver the information
            try:
                sendemail(from_email, recipients_list, cc_list, subject, message,username,password,server)
                print("Alert %d delivered successfully" % count )
#if something fails do this: 
            except:
                print("message sending failed", "Check login credential and mail server")
                exit()
            time.sleep(10)
            



            

            
            
            
        



    

    

    

    
    
    
    
        
            
    
    
    
    




    




 

