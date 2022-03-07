# QA_Enable_Project

## Currently a placeholder README

<div id="top"></div>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#The-idea">The idea</a>
        <li><a href="#built-with">Built With</a></li>
    </li>
  <li><a href="Entity-Relationship-Diagrams"> Entity Relationship Diagrams </a></li>
    <li>
      <a href="#getting-started">Getting Started</a>    
        <li><a href="#what-went-well">What went well</a></li>
        <li><a href="#what-went-wrong">What went wrong</a></li>
    </li>
    <li><a href="#Possible-improvements-for-future-revisions">Possible improvements for future revisions</a></li>
    <li><a href="#API-Screenshots">APP Screenshots</a></li>
    <li><a href="#Database-screenshots-to-show-Data-is-being-persistence">Code Snippets</a></li>
    <li><a href="#Link-to-my-jira-board">Link to my Jira board</a></li>
    <li><a href="#Test-Coverage">Test Coverage</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## The idea
At its core, I wanted something that I could use in my home D&D games whilst also being a good project to showcase the things I've learnt so far on this bootcamp. 
So, going along with that, the original idea was to have a database of character sheet(s) and their associated players (if any), so that I could easily keep track and make changes, this came about because the mobile app I use requires you to pay to have more than 2 character sheets, and the online portals I have used have been clunky at best. 
It should also allow for incremental creation ie; not all fields have to be filled in during creation, to allow for more long term character design and planning, as well as associating players with their characters at a later date and vice versa. 

Using this idea as a starting point, I then thought it would be a good idea to expand on this, I decided to associate a DM with his respective players (if any)
and the DM to his planned NPC's. This then led to the idea that, some characters can cast spells, and almost all start with / need some way to track equipment. 


<details>
<summary>The MVP targets for this project were</summary>
<ul> 
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li> </li>
  <li></li>
  <li></li>
  <li> </li>
 </ul>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Python](https://docs.python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>

### Entity Relationship Diagrams 

The basic concept for this project is just a Player with a zero to many relationship to Player_character, as a player can have zero, one or many characters

![image](https://user-images.githubusercontent.com/81429555/154951193-dfc1e6bc-2565-4b34-8be6-8768badea6a8.png)

The idea here being that I can use the boolean values in Python in functions designed to use that data to fill out the rest of the character sheet

![image](https://user-images.githubusercontent.com/81429555/154954170-d4aa9741-9bd9-4e91-9956-526f0596ef1a.png)

in the second image, I expanded on my initial idea adding in a dm, npc, spell and equipment tables, because in a real D&D setting these would be necessary to have, even if all the fields are null

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started



### How I expected the challenge to go




### What went well


<p align="right">(<a href="#top">back to top</a>)</p>



## What went wrong

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Possible improvements for future revisions

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## API Screenshots

### Get All

### Create Method

### Delete By ID

### Update By ID


<p align="right">(<a href="#top">back to top</a>)</p>



## Database screenshots to show Data is being Persisted


### Create method


<p align="right">(<a href="#top">back to top</a>)</p>
### Delete


<p align="right">(<a href="#top">back to top</a>)</p>
###  Update 



<p align="right">(<a href="#top">back to top</a>)</p>




## Link to my Jira board


<p align="right">(<a href="#top">back to top</a>)</p>


## Testing and Coverage
### Unit Testing

### Test Results




<p align="right">(<a href="#top">back to top</a>)</p>
