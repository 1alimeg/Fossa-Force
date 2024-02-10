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
- LIST VIEW
    - user icon
    - user name
    - Any new alerts
    - current stress score
    - accessible through which messaging channel (sms, facebook, whatsapp)
    - other quick access relevant information
    - filter function for this view
- MAP VIEW
    - heat map "danger zone" based off of stress analytics
    - user icon with location on map based off of filtered mode
    - filter selector at the top righ

- MESSAGING PORTAL
    - list view of all currently active "situations"
    - individual cases should upon up to a messaging environment
    - possible inclusion of contact EMS services
    - messaging between admin and "in danger" user is displayed inline with current status and steps taken for help
        - friend contacted
        - EMS services called
        - false alarm

    - the information from the steps taken in the messaging portal could be used for future prediction and analysis


- verify and accept new registered users into database
- messaging portal with current users in dangerous situation
    - current state of user



- Case report /export function
    - allows each true case to be logged for future reference
    - linked in with predictive module



- filtering of MAP and LIST VIEW
    - list all registered users
    - based on groups
    - based on stress status (list from most to least stressed with alert at top)
        - map view can be selected only selected stress status
    - Only show danger alerts
        - either in list view or on the map
    - predictive (possible new alerts based on personal history)
    

## User (dashboard)
- ability to register for service (user side)
- Login in to user homepage
- 
- modify account information and account settings
    - automatically share location information upon alert
    - request access to location upon alert  (opt in for auto location sharing)  required for quick response through system   *** the user won't have time to really message  back and forth with emergency services or researchers in the event of an emergency***
    - set up/modify safe zone
    - send location data if friend has an alert (are you within reach)

- add/ removefriend to personal friend-group or watch-list
- see current stress score for yourself
- see historical alerts for yourself
- 
- 



## User (phone interaction with Twilio notification)
- "are you safe" initiation message
    - time out no responce "location automatically shared"
    - respond back with one letter
        - "Y"  I am fine  cancels alert  (the statistics are entered into ML for evaluation)
- "help your friend they are in distress"
    - send location to see if you are the closest person
    - fastest response and closest person will have infromation released to them regarding their location





# Functional Requirements

🔴🟠🟡🟢🔵🟣

## Stress Score
    - use ML to process or specific stress scenarios as outlined below
    - have to figure out specific timeline for events as opposed to snapshot sort of thinking with these scenarios

### Studying
- 🟢Pulse Rate - 
- 🟢body temp - 
- 🟡priximity to unfamiliar objects -  (other people in the library)
- 🟢ambient noise -  (quiet speaking in library)
- 🟢stress indicator -  (low stress levels)
- 🟢user behaviour -  (sedentary)
- 🟢movement pattern -  (normal)


### Walking to Class/home
- 🟡pulse rate -  (slightly elevated from walking)
- 🟢body temp - 
- 🟢proximity to unfamiliar objects -  (not many people you are near when walking)
- 🟢ambient noise -  variable but generally quiet
- 🟢stress indicator -  (low stress levels)
- 🟡user behaviour -  (active)
- 🟢movement pattern -  (normal)

### Group Study
- 🟢pulse rate -  (sendentary with small increases due to joking around with friends)
- 🟢body temp - 
- 🟢proximity to unfamiliar objects -  (more familiar devices around )
- 🟡ambient noise -  (variable quiet speaking and can include loud joking around)
- 🟢stress indicator -  (low stress levels)
- 🟢user behaviour -  (sedentary)
- 🟢movement pattern -  (normal)

### Physical Activity
- 🔴pulse rate -    (variable from yellow to red due to level of activity)
- 🟡body temp -   (variable yellow to red due to level of activity)
- 🟡proximity to unfamilar objects -  (friends and strangers at the gym)
- 🟡ambient noise -  (general higher level of noise in gym environment)
- 🟡stress indicator -  (physical stress)
- 🟡user behaviour -  (active)
- 🟢movement pattern -  (normal for physical activity)

### Studying
- 🟢pulse rate - 
- 🟢body temp -
- 🟡proximity to unfamiliar objects -  (other people in the library)
- 🟢ambient noise -  (quiet speaking in library)
- 🟢stress indicator - (low stress levels)
- 🟢user behaviour -  (sedentary)
- 🟢movement pattern -  (normal)

### Exam Stres
- 🟡pulse rate -  (high and possibly irregular pulse)
- 🟢body temp -   (increased though not high due to mental stress)
- 🟡proximity to unfamiliar objects - (Possibly near class mates, and other students)
- 🟢ambient noise -  (generally quiet)
- 🔴stress indicator -  (high stress)
- 🟢user behaviour -  (sedentary)
- 🟢movement pattern -  (normal)

### Active Assault Scenario
- 🔴pulse rate -    (high due to fear or activity)
- 🟢body temp -   (high due to stress or at least quickly ramping up)
- 🔴proximity to unfamiliar objects -  (single or multiple unfamiliar objects... though this has some flexibility due to the statistics regarding people you know harming or assaulting you... can be further discuessed)
- 🔴ambient noise -  (possible yelling followed by acute drop off... much more silent)
- 🔴stress indicator -  (high stress indicated)
- 🔴user behaviour -  (stressed)
- 🔴movement pattern -  (irregular)

### Drunk (like bloody wasted and unconscious)
- 🔵pulse rate -   (lower heart rate than regular)
- 🔵body temp -   (decreased body temperature due to vasodilation)
- 🟢proximity to unfamiliar object -  (no one around)
- 🟢ambient noise -  (quiet)
- 🟡stress indicator -  (unconscious so I don't know how the stress indicator level is evaluated)
- 🟢user behaviour -  (sedentary)
- 🟡movement patterns -  (irregular previous to unconscious state)








## Alert system

- incoming message
    - system sensed danger (are you OK alert)
    - 

- automated message, (Are you in danger)


- alert to close friends (would require constant location tracking)
    - mass alert to all friends (would you like to share location)
    - if location is actively being shared, the closest friend can be notified that their friend is in distress.


## Predictive Alert System (where administrator can see people who may be in danger or approaching a dangerous situation)
- alter the situation before something happens
- based off of "hot spot zones"
- based off of past user behaviour
- events that could alter user safety
    - calendar events could be implemented to put this into the predictive system.
- 




# UML data classes


### systemUser

- Attributes
    - first name
    - last name
    - mobile phone number
    - address
    - email
    - date of birth
- Setters/Getters
- Constructors
- 

### Administrator (extends user)

- Attributes
    - [] Student (list of all students who are being tracked by the service)




### Student (extends systemUser)

- Attributes
    - [] FriendGroup (list of all peer students who this student has added as a friend)

- preferred notification type
    - SMS
    - facebook Messenger
    - WhatsApp




