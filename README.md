# Requirements Engineering

# User stories based off of user requirements

## Administrator
### ([x])Persona Signs up for administrator previledges
### ([x])administrator logs into Foosa Force application
### ([x])administrator views and approves / incoming registered users
### ([x])administrator views list of all approved students that they are monitoring
### ([x])administrator filters list of students based on predefined filters
### ([x])administrator responds to initial alert from student in distress
### ([x])administrator views analysis dashboard
### ([x])interact with student through messaging center in current 




## General User
### ([x])Persona signs up for general user priveledges
### ([x])user add new friend to friend group
### ([x])user removes friend from friend group
### ([x])respond to other alerts from friend
### ([x])interact with the system in case of theiry own alert
### ([x])view their own analysis dashboard










# Functional Requirements

🟢 ADMINISTRATOR
🟠 GENERAL USER



> ### 🟢Persona Signs up for administrator previledges
>
>- persona navigates to the Fossa force registration page
>- webserver responds to request for registration page
>- persona selects if they would like to sign up as user or administrator
>   - administrators must input affiliated institution information
>- persona enters requested information for sign up
>   - data entered properly, user taken to next step
>   - data entered incorrectly, error message (user prompted to fix errors)
>- information submitted to webserver
>- database queried for any pervious user with administrator priveledges with the same information
>   - if CONFLICT error message sent back (user already exists) 
>   - if NO CONFLICT data entered into database
>       -  new administrator taken to home page of portal

> ### 🟢Administrator logs into Foosa Force application
> 
>- persona navigates to the Foosa force login page
>- webserver responds to request for login page
>- persona enters username and password
>   - both fields entered properly, user taken to next step
>   - fields not entered correctly (warning message displayed asking user to correctly fill out login form)
>- fully entered data fields sent to webserver
>- database queried for corresponding username and password combination
>   - username and password DO NOT match (error message sent back to the user)
>   - username and password combination MATCH
>       - either general user or administrator status determined by account information
>- user taken to administrator portal based off of administrator priveledges as determined by previous step

> ### 🟠Persona signs up for general user priviledges
>
>- persona navigates to the Fossa force registration page
>- webserver responds to request for registration page
>- persona selects if they would like to sign up as user or administrator
>   - administrators must input affiliated institution information
>- persona enters requested information for sign up
>   - data entered properly, user taken to next step
>   - data entered incorrectly, error message (user prompted to fix errors)
>- information submitted to webserver
>- database queried for any pervious user with administrator priveledges with the same information
>   - if CONFLICT error message sent back (user already exists) 
>   - if NO CONFLICT data entered into database
>       -  new user taken to their home screen
>- message on user home screen stating their account is awaiting review

> ### 🟢Administrator views and approves/denies add request for new user sign-up
>
>- notification system within administrator portal alerts administrator to new user registered with Foosa Force application
>- administrator either navigates to dedicated registration/approval module or responds to notification which will take him there automatically
>- enter into registration/approval module
>- database is queried for all pending approval status users who are not with admin priveledges that are affiliated with the same institution, and populates screen with these users
>- each enter will have a button beside their name with either approve or reject
>- APPROVED the users information will be updated within the database
>   - email or other notification letting the user know of their APPROVED application status.
>   - notification module on user screen updates status to APPROVED and unlocks all setting for that user
>- DENIED the users information will be updated within the database
>   - email or other notification letting the user know of their DENIED application status.
>   - notification module on usre screen updates status to DENIED locks account down or other action to be taken.

> ### 🟢administrator views list of all approved students that they are monitoring
>
>- administrator previously logged in
>- user select to view "Main" portal from website sidebar
>- website sends request to database to query for all approved students affiliated with that institution or Administrator
>- list and relevent data as stipulated by the "Main" view is returned to webserver
>- website loaded and populates view with list of all students returned by the database
>- relevant data is displayed accordingly for each student
>- each student in this list can be selected which will open up a more detailed view
>   - particular student will be queried in the database with all data for that student being used for populate a dashboard for that particular student.


> ### 🟢administrator filters list of students based on predefined filters
>
>- administrator previously logged in
>- administrator previously selected to view "Main" list of students
>- administrator selects drop down bar to filter list of students
>- list of predetermined filters displayed to the administrator
>- each filters logic has been determined programatically
>- a filter is selected, and the predefined query is sent to the database
>- query results are sent to the webserver to populate the administrators view with

> ### 🟠User adds new friend to friend group
>
>- user previously logs in
>- user selects friend list from sidebar button
>- user selects "add" button within the friend view
>- search bar appears in view
>- user enters in username of friend
>- database queried for that particular username
>- FOUND - small icon displaying that user with an add button beside their name
>   - user responds by clicking add button
>   - users affiliated with one another in the database or added to their respsective friend groups within the program.
>- NOT FOUND - message returned to the user stating "No such username found"

> ### 🟠User removes friend from friend group
>
>- user previously logs in
>- user selects friend list from sidebar button
>- list of current friends queried from database and populated friend list
>- icon for "..." is presented at the end of each other
>- user selected this button and is presented with a menu with multiple option
>   - one of these options is to remove friend
>- user selects remove friend button from this list
>- prompt is displayed to the user asking "are you sure you would like to remove this friend from your friend list?"
>- OK is selected
>   - prompt disappears
>   - the friend will become unaffiliated with this user and the database will be updated
>- CANCEL is selected
>   - the prompt disappears
>   - no update made to the database and the friend remains in that users group.

> ### 🟢administrator views dashboard view (more information on dashboard view to be discussed)
>
>- administrator previously logged in
>- administrator selects dashboard view from the sidebar menu
>- logic of each view will be pre-determined progrematically in application
>- latest data will be queried for in the database
>- graphs build uisng relevent frameworks
>- webpage will be populated with the latest up to date information for the administrator to view



> ### 🟢administrator responds to initial alert from student in distress
>
>- administrator previously logged in
>- administrator can be in any portion of the website
>- incoming alert displays in the center of the screen stating that student stress level show sign of distress
>   - in the background twilio sends notification to the users phone asking if they can
>   - new event logged and this users chat is added to the messaging center
>- DISMISS - the administrator dismisses the alert... and the user is added to the messaging center in the background
>- CHECK - the administrator respods to the alert and is taken directly the messaging portal
>   - live data from the IoT device is visible to the administrator
>- administrator is able to see conversation between user in distress and himself and see if friends were alerted to this users state

> ### 🟠Respond to alert in the even of friend in distress
>
>- case will be written for one particular user responding to a distress alert from another user whom they have previously added into their friend group
>- user does not have to be logged into the system to respond to distress situation from a friend
>- server side application senses a friend in distress
>- alert sent to administrator to start communication process
>- Twilio system triggered to send alert to the user who is in distress
>- if distress alert is confirmed or message automatically times out, location data of user in distress is sent back to foosa program
>- all associated friends are immediately contacted using twilio system
>- location data of all associated friends are requested
>- users have an option to share
>- all locations from users who shared location information is calculated to find the closest friend
>- if this location falls within a viable responce distance the location of the student in distress will be shared with the friend most easily able to respond
>- both the distressed user and the friend who is responding to the distress will be added into the admin message thread for the administrator to monitor and interact with.
>- only an administrator should be able to close and active distress situtation

> ### 🟢interact with student through messaging center in current distress
>
>- the administrator has previously logged into the system
>- a user has already had a distress event that was noticed
>- the system alerts the administrator to the distress event
>- new entry is made in the messaging system consisting of a conversation with that particular user
>- Twilio message is sent to the user in the background
>- messaging portal shows that this message has been sent
>- administrator awaits responce by the distressed user
>- once responce has been recived, the responce is added into the chat interface
>- other friends are contacted in the background and friend with closest location is asked if they can check on the distressed user
>- Once a friend responds and accepts the request by the user to help the distressed user, they also will be added into the chat for collaboration purposes
>- due to the SMS communication between the administrator and each of the users... the administrator will have access to both users involved but each user will only be able to interact with the administrator ( or with each other through their own channels)
>- once the distress event has been resolved the log of all communication will be saved for analysis
>- the location of the initating distress event will be added into the database for the administrator analysis screen

> ### 🟠General User interacts with system in the case of their own distress alert
>
>- this interaction will be limited to the user in distress
>- The system as it processes the live IoT data will calculate a stress score above a certain threshold
>- once this threshold has been passed, the system through the twilio API will send out a message to the user
>- The user will receive a message asking if they are safe
>- if they respond the appropriate safe responce, the alert will be canceled
>- if they message that they are in distress, or do not respond within an alotted time period, the system will automatically notify the administrator
>- this usercase flows directly into the following
>   - user responding to a friend in distress
>   - administrator using messaging portal to interact with user in distress

> ### 🟠administrator views dashboard view (more information on dashboard view to be discussed)
>
>- general user previously logged in
>- general user selects dashboard view from the sidebar menu
>- logic of each view will be pre-determined progrematically in application
>- latest data will be queried for in the database
>- graphs build uisng relevent frameworks
>- webpage will be populated with the latest up to date information for the user to view
