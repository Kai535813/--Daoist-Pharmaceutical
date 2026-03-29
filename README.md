# Daoist Pharmaceutical Overview:

## How to Setup and Play:
* Insure that pygame is downloaded
  * Open your terminal
  * For mac OS, input python3 -m pip install pygame
  * For Windows, input python -m install pygame
* If pygame is installed, then the game should be ready to be ran from either your terminal or an IDE of your choice
  * For VScode, we notcied that the defalt settings does not have "ExecuteInFileDir" enabled, turn it on through your settings, or the game likely wont run
* The game will open a seperate window called pygame once the program starts in which you will interact with and play the game
* Once the game starts, diseases and resources will start randomly spawning
* Time in game is measured in "Months"
* The player has reputation and money, once repuation drops below 0, the game ends, but the player can go into debt regarding money
* Diseases (red pixels that spawn on the map) will actively decrease the player's reputation as it spreads
* The player can choose to cure the disease by clicking on a red pixel and pressing accept
* The game will then prompt the player to select a medicine and the amount to use; when clicking on the disease its symptoms and the money required to build a pharmacy will also be displayed
* The game is designed for the player to slowly figure out which medicines are effective against which symptoms through trial and error, but it is also to learn the effectiveness of each medicine by reading the "medicineI" dictionary at the top of the Disease file
* Once a medicine and amount is assigned to a disease, the disease will begin to visually shrink at a rate dictated by the effectivness of the medicine
  * The medicine assigned to the disease will deplete over time, if the amount of medicine is not adequate, the disease will resume spreading, if there is an adequate amount of medicine, the disease will shrink until it disappears and it therefore cured (this all happens over time)
* The player starts off with some medicine and can either source more medicine from the market or by paying to extract medicines from yellow pixels

## Original Concept of the Game:
![opening screen](https://github.com/Mo59471/Programming-Group-Project-Immune-System-Tower-Defense-Oriental-Medicine-Tycoon/raw/main/%E9%81%93%E5%BE%B7%E5%AE%B6%E8%A3%BD%E8%97%A5%E4%BC%81%E6%A5%AD-DaoistPharmaceutical/Photos/Daoist%20Pharamaceutical%20Welcome%20Page.jpg?raw=true)
![difficulty select](https://github.com/Mo59471/Programming-Group-Project-Immune-System-Tower-Defense-Oriental-Medicine-Tycoon/blob/main/道德家製藥企業-DaoistPharmaceutical/Photos/Daoist%20Pharmaceutical%20Option%20Page.jpg?raw=true)

Opening scene: The player as the Jade Emperor's Son is sent down to East Asia for causing trouble in the Imperial Court in order to cure the people. Game then switches to screen showing a map of East Asia. Icons appear to represent sickness and the player can user medicine to cure. UI will have icons to represent how much medicine the user has and what type. Each sickness has different attributes and therefore require different medicines. The medicine of the player will either be sourced through market purchases or individual sourcing from natrual resources. The stages of the game will be in cycles of "years" and after a certain number of cycles, new features of the game will be gradually added. The scope the player opperates will be porportional to their reputation, so players will likely be able to expand their scope as they play the game. The player loses the game once their reputation drops to a given level, meaning that the player can be in debt, but will drop the player's reputation in fixed periods of time after a grace period. 
![primary gameplay](https://github.com/Mo59471/Programming-Group-Project-Immune-System-Tower-Defense-Oriental-Medicine-Tycoon/blob/main/%E9%81%93%E5%BE%B7%E5%AE%B6%E8%A3%BD%E8%97%A5%E4%BC%81%E6%A5%AD-DaoistPharmaceutical/Photos/Daoist%20Pharmaceutical%20Main%20Gameplay.png?raw=true)
![Market](https://github.com/Kai535813/--Daoist-Pharmaceutical/blob/main/images/Market.jpg?raw=true)
* Jade Emperor's Son sent down to Earth to cure people
* Story-driven elements
* CCP and Western Medicine-relationships with either to compete with the other
* Money and Reputation system
* Placebo effect modifier?
* Demographic differences, old people are easier to heal, younger people are harder to heal, but because they use social media, they can rapidly increase reputation
* Taoist powers infused into medicine to make them more effective?
* System for buying or natrually sourcing medicine
* Special medicines or techniques sold by CCP and Western Medicine that can only be purchased given the players relations are good enough 
* Some medicines may be unethical with could decrease reputation if exposed.

![Game Over](https://github.com/Mo59471/Programming-Group-Project-Immune-System-Tower-Defense-Oriental-Medicine-Tycoon/blob/main/道德家製藥企業-DaoistPharmaceutical/Photos/Game%20Over.png?raw=true)
## List of Chinese Medicine Ingredients for the Game:

### Starting Medicine
* Mercury
* Arsenic
* Ginger
* Goji Berry
* Cannabis 

### Mid-Range Medicine
* Aristolichic Acid
* Ginseng
* Sea Cucumber
* Dried Seahorse
  
### High End Medicine
* Swallow Nest
* Rhinoceros Horn
* Tiger Bone

## UML:
![DaoistUML](https://github.com/Kai535813/--Daoist-Pharmaceutical/blob/main/images/DaoistPharmaceuticalUML.png?raw=true)
  
&nbsp;

## Team Contributions:

1. **Ethan Tang**
   - Framework of main file along with primary game logic
   - Disease class display functionality
   - Implemented disease random spawning and displaying
   - Programmically drew the map
   - UML
  
&nbsp;

2. **Mo Spiegel**
   - Button Class, Disease Class logic
   - Implemented Button collision detection, hoverability, and clickability
   - Implemented Main File timer
   - Most of the UI design
  
&nbsp;

3. **Kai Yun Chao**
   - Market Class
   - Implemented Market displaying, called through a button click
   - Effects of medicines against certain symptoms
   - All of the research on Chinese Traditional Medicine
   - GUI mock-up 
  
&nbsp;

3. **Simon Sakata**
   - Resource Class
   - Implemented resource random spawining and displaying
   - Playtesting
   
## ToDo List:
**Top Priority Tasks:**
* Add a pause Button to stop the in-game timer
  
**Long-Term Tasks:**
* Get started on reputation system
* Implement story elements
* Add age demographics to Disease class
* Implement soundtrack possibly written by Thompson??
