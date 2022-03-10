# QA_Enable_Project
This repository contains my deliverable for the QA devops fundamental project.




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#The-Project">The Project</a>
        <li><a href="#Built-With">Built With</a></li>
    </li>
  <li><a href="#The-Design"> The Design </a></li>
    <li>
      <a href="#CI-Pipeline">CI Pipeline</a>    
        <li><a href="#Risk-Assessment">Risk Assessment</a></li>
        <li><a href="#what-went-wrong">Testing</a></li>
    </li>
    <li><a href="#The-App">The App</a></li>
    <li><a href="#What-went-wrong">What Went Wrong</a></li>
    <li><a href="#Possible-improvements-for-future-revisions">Possible improvements for future revisions</a></li>
    <li><a href="#Updates">Updates</a></li>
    <li><a href="#Version">Version</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## The Project
The brief for this project was to design and produce a web app of my choosing. It was required to have CRUD functionality (Create, Read, Update and Delete), needed to use the Flask micro-framework and had to store data in a MySQL database that had a minimum of two tables sharing a one to many relationship.

![App Structure](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/project%20brief%20diagram.png)

The App was also required to have at least Unit Testing completed with a high-level of coverage, Unit Testing was considered a stretch goal. 
The project was also required to have implementation of several stages of a CI pipeline, such as Project Tracking, a VCS (Version Control System), a Development Environment and a Build Server.


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Python](https://docs.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Jenkins](https://www.jenkins.io/doc/)
* [Github](https://docs.github.com/en)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)


<p align="right">(<a href="#top">back to top</a>)</p>

### The Design

I have chosen to create a D&D style database which, at its core would allow the User (Player) to create a Character and be able to update and track details of said character. 
I started out with just a Player with a zero to many relationship to Player_character, as a player can have zero, one or many characters.
The idea here being that I can use the boolean values in Python in functions designed to use that data to fill out the rest of the character sheet. 

![Original ERD](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Original%20ERD.png)


In the second iteration of the ERD, I expanded on my initial idea adding in a dm, npc, spell and equipment tables, because in a real D&D setting these would be necessary to have. 
I made the relationship between all tables zero to many as I wanted to allow for incremental creation ie; a User can create a character sheet slowly overtime as their idea is fleshed out. 

![Second ERD](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Second%20ERD.png)

After working on the project and creating all of the CRUD functionality, I realised that in order for the App to function as efficiently as possible the tables required some refactoring and some of the information was pulled out to be done elsewhere as calculations rather than user input.
As shown below, the equipment fields and player_character fields have changed, with the player_character table dramatically shortening in length. 
The reason for this was a lot of the fields that I was asking the user to input could be determined by which starting race or class they chose, allowing for behind the scenes calculations and reducing the amount of input the user was required to enter. 
The equipment table was updated after we learnt about Flask Forms and were taught how to use SelectField().

![Second ERD](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/first%20update%20ERD.png)

Finally, after reading back through the project spec I realised that one of the table relationships needed to be a one to many, so I decided to create that relationship between Player and player_character, seeing as if the DM is adding a Character sheet, he would have to get that information from a Player and therefore would have a player to attribute it to. Likewise if a user is creating a personal character sheet, that user is the Player and would have a player to attribute it to. 

![One To Many Update](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Updated%201%20to%20many%20ERD.png)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## CI Pipeline

So for Project tracking I chose to use Jira as it is the software I am the most familiar with. I assigned story points and followed MoSCoW Prioritisation, in retrospective I should have added suitable Acceptance Criteria. 
Items were created in the project backlog, moved into the sprint backlog and then to completed, the review section was used in retrospective to look back over the sprint. 
The state of the Jira board towards the end of Sprint one was:

![Sprint One](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Jira%20Board.png)

The reason Testing is still in progress is Integration testing has not been started yet, but as it is not an MVP requirement I did not consider it necessary to complete before delivering the project. 
I have included examples of the details I entered into the Jira board below, where you'll see that Unit testing is finished, but Integration testing is in progress: 

![Testing](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Testing%2C%20Jira.png)

![CRUD](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/CRUD%20task%2C%20Jira.png)

The full jira board can be found here <a href="https://jack-middleton.atlassian.net/jira/software/projects/QEP/boards/5"> here </a>, a burndown chart has also been produced for this project: 

![Burndown](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Burndown%20Chart.png) 

As you can see I stayed fairly on track throughout the project, the reason for this was I broke up the project into modules and worked on it piece by piece as I found this a more effective method of working than trying to do everything in one go and becoming overwhelmed. I sped up a little on day 3 as creating the webhook and setting up the build automation went faster than expected, but the documentation took slightly longer than expected so I ended up finishing on time rather than early. 



For Version Control git was used and the project was hosted on github. Version control via git allows changes to the project to be made and committed whilst keeping the commit history for access to earlier versions. Github as a repository hosting service allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing

The development environment used was a Python3 Virtual Environment(venv) hosted on a virtual machine running Ubuntu 18.04, the reason for this choice was Selenium seemed to have some versioning issues with Ubuntu 20.04, but worked fine with 18.04, so I chose this to make setting up integration testing easier down the line. 
Python is used as Flask is a Python based micro-framework. 
A venv allows pip installs to be performed and the app to run without affecting any conflicting pip installs on the same machine. 

Jenkins was used as a build server, providing automation of building and testing. This automation is achieved by setting up a freestyle project which executes the test.sh script. 
This was made portable between jobs by adding the test.sh script to the repo and running a script on Jenkins that tells it to search for and run the test.sh script, so this Jenkins job can now be used to automate other tests as long as they have a test.sh file. The Jenkins Script and the test.sh file are shown below. 

![Jenkins](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Jenkins%20Script.png)
![Test.sh](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/test%20sh.png)

The full pipleline utilised in the project is: 

![pipeline](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/CI%20Pipeline.png)

## Risk Assessment
Prior to building the app, a Risk Assessment was undertaken to identify potential risks and propose controls and responses, in order to attempt to control / mitigate / minimise risks as much as possible.
I followed the basic principles of a Risk Assessment Matrix for this task, using 1-5 to denote possibility / severity of an outcome as well as green, yellow and red for the same purpose. 

The key for the risk assessment is below: 

![Risks Key](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Risk%20Assessment%20Key.png)

and the Risk Assessment was as follows:

![Risk Assessment](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Risk%20Assessment.png)

As a result of the Risk Assessment, the following control measures were implemented into the project. 
User profiles were not implemented, as this would require sending some form of authentication over an unsecured HTTP connection. I would like to implement this at a later stage, and the Risk Assessment and control measures will be updated accordingly. 
SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database, allowing for proper CSRF (Cross Site Request Forgery) protection. 
Credentials were stored as secret texts on Jenkins VM and exported as environment variables to avoid accidentally publishing confidential details. 


## Testing 

Testing the app was an essential part of the development process. Only Unit Testing has been implented thus far, as I mentioned earlier Integration testing was considered a stretch goal for this project. 

Unit testing tests units of functionality (ie; functions) within the app. Unit tests were written for the Create, Read, Update and Delete methods, as well as the slightly more specific search (read) methods used in this project and the display_character method used to perform calculations to determine what gets displayed after the character form has been submitted. 

As this is not a production app, tests such as security tets and performance tests were not part of the scope of this project, only testing for functionality for performed.

As mentioned previously, these tests are automated via Jenkins using webhooks, a successful build in which all tests pass is shown below, along with the commit that triggered it to show the time stamps and that the commit did in fact trigger the tests:

![Github commit](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/commit%20that%20triggered%20Jenkins.png)

![Jenkins Automated Test](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Jenkins%20Trigger.png)

A coverage report artefact was also generated and archived during the build and saved as a html file, the coverage report for the above build was:

![Coverage Report](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/html%20coverage%20report.png)

Showing 100% test coverage overall, all tests must pass for a build to be considered successful. 


The other type of testing not implemented is, as mentioned previously, Integration testing. 
Integration testing tests the function of an app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended.

If I were to add Integration Tests, I would need Selenium, which as of right now has versioning issues on Ubuntu 20.04 machines. My Machine is 18.04 so it shouldnt pose an issue, but for other projects I'd need either a specific instance for Integration Testing or make sure my machine was on 18.04 during config. 
I'd also need Chromium Browser as a browser for integration tests and Wget and Unzip as the driver for chromium browser. 
In the config I'd set it to (--headless) which tells it to run in the terminal and not in a browser, and from there I could simulate button presses and make assertions to check that my Forms function as intended. 

## The App

So when you go to the homepage of the app, with no data entered it looks as below: 

![Blank home page](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Blank%20Homepage.png)

Before we do anything else, I wanted to account for edge cases, for example if someone put /displaycharacter/1 into the search bar without any characters or character sheets being made, the same going for the searchnpc, searchplayer, searchspells and searchequipment, the results of which are below:

![Search No NPC](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/DM%20no%20NPCs.png)

![Search no Player](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/DM%20no%20players.png)

![Search no Spells](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Character%20no%20spells.png)

![Search no equipment](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/character%20no%20equipment.png)

![Search no character](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Player%20no%20characters.png)

As you can see, it still displays a page showing that none exist rather than raising an exception.

Looking at the page as it stands, we have the ability to create a DM, an NPC, a Player, a Character, Equipment and Spells, the pages and forms for the tables are as shown: 

![Create DM](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/create%20DM%20page.png)

![Create NPC](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Create%20NPC%20page.png)

![Create Player](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Create%20Player%20page.png)

![Create Character](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Sample%20Character.png)

![Create Weapon](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Sample%20weapon%20creation.png)

![Create Spells](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/spell%20no%20character.png)

I've also created a Spell at level 0 and a Piece of Armour instead of a weapon, to show the difference in how they're displayed on the home screen:

![Create Armour](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Sample%20armour%20creation.png)

![Create Spell L0](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/sample%20spell%2C%20FK%20and%20cantrip.png)

![Equipment display](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/weapon%20and%20armour%20display.png)

![Spell display](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/spell%20display.png)

Firstly, I'll show a character sheet with no spells or equipment attributed to it, to show how its displayed in this instance: 

![Character no sp or equip](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Character%20sheet%20display%20no%20equipment.png)

and again, as you can see no errors have been raised.
The character sheet with Spells and Equipment attached is as follows

![Character sheet](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/character%20sheet%20with%20spells%20and%20equipment.png)

Now back to the homepage, when there is data for all sections it looks like so: 

![Full home page](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/homepage%20with%20details.png)

You have the ability to search for a DMs players or NPCs, a players characters and a characters spells or equipment, which looks like so: 

![searchplayer](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Sample%20Player.png)

![searchNPC](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/searchNPC.png)

![searchcharacter](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/player%20character%20search.png)

Spells and Equipment searches have been shown above but look like so:

![equipment](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/weapon%20and%20armour%20display.png)
![spell](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/spell%20display.png)

Updating an item takes you to the same page as the create page, except this time it updates the entry rather than creating a new one

![Update one](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/update%20DM%20and%20player.png)

To show the updates working, you can see that the Updated Sample DM and Updated Sample player have the same ID as the original, but an updated name

and the delete works as intended, heres the front page missing a couple of entries to show it works. 

![delete](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/delete%20spell%20and%20character.png)


Lastly, when creating a character there must be a Player to attribute it to so I added Validation on the backend, and just to prove that it works: 

![validation](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/Validation%20Proof.png)

<p align="right">(<a href="#top">back to top</a>)</p>



## What went wrong

Luckily, apart from a few static bugs which were corrected during Unit Testing, nothing too outlandish went wrong. My biggest issue was at the start of the project I forgot to switch to dev, pull and start working on a new branch, so when I realised my mistake I had a bunch of merge conflicts locally, the network graph for this moment in time is shown below.

![Merge Conflicts](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/merge%20conflict.png)

Thankfully I got the issue resolved and have managed to work using the Feature Branch method for the remainder of the project, as shown below.

![Post Conflicts](https://github.com/Jack-Middleton/QA_Enable_Project/blob/main/Pictures%20For%20Readme/feature%20branch.png)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Possible improvements for future revisions
<ul>
  <li> I would like the update function to retain the information already existing in the entry, so as to make updating easier without the possibility of accidentally missing a section </li>
  <li> Add a spell list table, acting as a join between characters and spells to create a many to many relationship (characters dont just have 'spells', they have spell lists drawn from a shared pool of spells </li>
 </ul>


<p align="right">(<a href="#top">back to top</a>)</p>


## Updates
1.0.1
<ul>
  <li> Fixed small route bug for the searchnpc route </li>
</ul>


## Version
1.0.1



<p align="right">(<a href="#top">back to top</a>)</p>
