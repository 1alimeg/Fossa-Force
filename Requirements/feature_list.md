# The following is a list of requirements based off of TA email

>Hello Everyone,
>
>Reviewing your project ideas and the use case diagrams was a pleasure.
>
>All TAs, along with Dr. Gema, had a meeting yesterday where we reviewed the standard features that most teams are implementing >streamline the process and the features, we proposed standard features most teams should complete for this course.
>
>These are the minimum features expected from your project for IoT.
>- Alerting system (Twilio free credits)
>- Visualizations (at least three different types)
>- Two roles (Common user/Admin/etc)
>- Filtering
>- Predictions
>- Dashboards
>- Login/Registration system
>- Database
>(optional) Maps, Chatbot
>
>Kindly update your UML use-case diagram and features/requirements for milestone 2. We derived these features from all of your >initial use-case/features drafts.
>
>Resources I shared for this week:
>- Data Flow Diagram (level 0 and level 1 are expected) https://www.lucidchart.com/blog/data-flow-diagram-tutorial
>- UML Class Diagram https://www.lucidchart.com/pages/uml-class-diagram
>- Create GitHub issues for the week
>- upload all on the requirements folder on GitHub
>
>Please do reach out to me if you have any questions!
>
>Kind Regards,
>Rohit




# NON-Functional Requirements

**Definition from slides** - define system properties and constraints including limitations on hardware and software to be used, performance requirements, and development processes.

### Browser Based
- modern browser with latest security and technology capabilities


### Database
- MySQL can be used with static data obtained from IEEE dataport
- firebase realtime database could be used for live IoT data obtained from aplicable hardware
- 


### Twilio
- for SMS, Whatsapp, facebook alert
- chat between friends in possible alert scenario


### MQQT
- protocol for data transfer between server and wearable IoT device
    - possible not required since we are using static data (should be implemented though)




### Hardware
- Wearable IoT device (capabilities)
    - pulse
    - temp
    - microphone (decibel level)
    - accelerometer (movement pattern behaviour)
    - Networking
        - bluetooth (proximity to known devices)
        - wife/cellular (location approximation)
        - GPS (precise location)











# User Requirement List



## Admin
- register for admin services
- view list of all registered users
- messaging portal with current users in dangerous situation
    - current state of user
    - 

## User (dashboard)
- ability to register for service (user side)
- Login in to user homepage
- 
- modify account information and account settings
    - automatically share location information upon alert
    - request access to location upon alert
    - set up/modify safe zone
    - send location data if friend has an alert (are you within reach)

- add/ removefriend to personal friend-group or watch-list
- see current stress score for yourself
- see historical alerts for yourself
- 
- 



## User (phone interaction with Twilio notification)
- "are you safe" initiation message
    - time out no responce
    - "I am fine"
    - "send help"
    - send location
- "help your friend they are in distress"
    - send location to see if you are the closest person to the 





# Functional Requirements

## Stress Score
    - use ML to process or specific 


## Alert system

- incoming message
    - system sensed danger (are you OK alert)
    - 

- automated message, (Are you in danger)


- alert to cl


