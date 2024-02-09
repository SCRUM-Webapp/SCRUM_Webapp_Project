# SCRUM_Webapp:
Webapp managing the SCRUM Sprints developed for LV "Webentwicklung" at the Berlin School of Economics and Law

# Teamname:
Sprint-Flitzer

# Contributors: 
Vasco Pogade und Nicolas Jobstvogt

# Goals: 
Wir streben eine sehr gute Note an.
<p>Vasco: möglichst viel über die Entwicklung von Webanwendungen zu lernen und auszutesten, ob Webentwicklung etwas ist, wo ich auch später tätig sein will.</p>
<p>Nicolas: Ich möchte meine Python-Kenntnisse verbessern und ich bin interessiert, mich mit dem neuen Softwarestack auseinander zu setzen.</p>

# GitHub Pages:  
Here is the link to our GitHub Pages: https://scrum-webapp.github.io/SCRUM_Webapp_Project/

# How to get it to work?

Step 1: Clone the Repository to your prefered working environment:
```bash
git clone https://github.com/SCRUM-Webapp/SCRUM_Webapp_Project.git
```
Step 2: Create a Virtual Environment within your project directory:
```
python -m venv venv
```
Step 3: Activate the Virtual Environment:
```bash
source venv\Scripts\activate
```
Step 4: Install required packages:
```
pip install -r requirements.txt
```
Step 5: Initialize the database:
```
flask init-db
```
Step 6: Run the application:
```
flask run
```
Step 7: Visit the address showing on the console  
  
Step 8: We have purposely not added any example tickets with `insert_sample()` so create some of your own tickets and:  
Have fun!!!