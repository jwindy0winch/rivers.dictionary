# rivers.dictionary

# Overview
# Program Requirements:
Make a dictionary containing three rivers, and the country each river runs through:
●	Use a loop to print a statement about each river 
●	Use a loop to print the name of each river included in the dictionary 
●	Use a loop to print the name of each country included in the dictionary

# Defined Scope:
Iterate a dictionary containing three rivers that include the countries each river runs through. Using a loop print a statement about each river that includes the name of each river/country included in the dictionary. 

# Intended Usage:
A user searching for information about what countries a specific river runs through.

# Processing Logic
# Control & Data Flow:
The Rivers Program starts by defining the ‘Rivers’ Dictionary, which includes River Names; as each KEY, and Countries the rivers run through; as the VALUES, in a KEY-VALUE PAIR sequence. 
Chunk 2 on Line 8; begins by initilizing a first ‘for’ loop, which iterates over each KEY-VALUE PAIR in the ‘Rivers’ dictionary. While inside the loop, a ‘join( )’ is used to concatenate the list of countries into a string. After the string is formatted, a print statement is used; which initilizes an f-string and displays the river name and various countries it runs through, each on its own line using the new line ‘\n’ character.
 Chunk 3 on Line 13; begins by printing the ‘Rivers:’ title and includes the New Line ‘/n’ Character for both the title and each following  KEY in the upcoming Loop. Next, a second ‘for’ loop is initiated, which iterates over each KEY in the ‘Rivers’ dictionary and prints the name of each River/KEY.
The Final Chunk on Line 18, begins by print the ‘Countries:’ title and includes the New Line ‘\n’ Character for both the title and each following VALUE in the upcoming Loop. Next a new list is created, which collects and saves all the country names in the ‘all_countries’ list. A third ‘for’ loop iterates over each VALUE in the ‘Rivers’ dictionary. Within a fourth ‘for’ loop, the ‘all_countries’ list is appended by country and sorted alphabetically using the ‘sort()’function. Finally, a fifth ‘for’ loop iterates the ‘all_countries’ list and prints each countries name; alphabetically. 

# Process Specifications
# (PDL) Program Design Language: 
Initilizes a dictionary named ‘Rivers’ for which contains the names of Three Rivers as Keys and Three lists of Countries as Values. For each River and its associated Countries; concatenation of countries are put into a string and a printed statement containing each River and the Countries that River runs through with each River having it’s own associated line. The names of all Rivers in the Dictionary are then Printed. A new list collects all countries from the dictionary, sorts the countries alphabetically, and prints the names of all countries. 

# Pseudo Code:
Initialize a Dictionary named ‘Rivers’, which includes River names as KEYS and the list of Countries as VALUES.
For each River in the ‘Rivers’ dictionary:
	Convert the list of Countries into a String with each VALUE separated with a comma.
	Print “The [River name] runs through [List of Countries]” with each ‘River’ on its own line. 
Print “Rivers:” on its own line.
For each River in the ‘Rivers’ Dicionary:
	Print the River name name, each on its own line.
Print “Countries:” on its own line.
Initialize an emply list ‘all_countries’. 
For each list of Countries in the ‘Rivers’ Dictionary:
	For each country in the list:
		Append the Country to the ‘all_countries’ list. 
Sort the ‘all_countries’ list Alphabetically.
For each Country in the ‘all_countries’ list:
	Print the Country on its own line. 
 
# Flow Chart:
START → Initialize ‘Rivers’ Dictionary → START Loop through Rivers and Countries → Convert Countries list to a String → Print River Name and Associated Countries → END LOOP
Print Names of  all Rivers in Dictionary → Print Names of all Countries in Alphabetical order → END of PROGRAM

# Flow of Subroutines, Methods, & Functions:
	No identified subroutines, methods, or functions. 
 
# Specific Algorithms:
	The Rivers Program utalizes Looping, Sorting, and String Concatenation. The program uses Looping to iterate over the Rivers, Countries, and Keys of the Dictionary. Sorting is used with the ‘sort( )’ algorithm. A ‘join ( )’ algorithm  is used to concatenate the list of countries into a string, with String Concatenation.

# Data (INPUT/OUTPUT)
●	Rivers:
○	Type: Dioctionary
○	Dimension: 1-dimensional
○	Description: The Dictionary contains the names of Rivers as Keys and Lists of Countries as Values.
○	Range of Values: Dictionary with String of Keys; River Names, and Lists of Values; Countries
○	Initial Value:
■	‘Nile River’: [‘Egypt’, ‘Sudan’, ‘Uganda’, ‘Ethopia’, ‘Kenya’, ‘Tanzania’, ‘Rwanda’, ‘Burundi’, ‘Democratic Republic of the Congo’]
■	‘Amazon River’: [‘Brazil’, ‘Peru’, ‘Colombia’, ‘Venezuela’, ‘Ecuador’, ‘Bolivia’, ‘Guyana’]
■	‘Mississippi River’: [‘United States of America’, ‘Canada’]
●	River:
○	Type: String
○	Dimension: Scalar
○	Description: Variable that holds the name of each River as the loop iterates through the dictionary. 
○	Range of Values: Series of strings reporesting each of the three river names
○	Initial Value: No initial value outside the loop
●	Countries:
○	Type: List
○	Dimension: 1-dimensional
○	Description: Variable holds the list of associated Countreis with each river during each iteration of the loop
○	Range of Values: Lists containing the strings of country names
○	Initial Value: No initial value outside the loop
●	countries_str:
○	Type: String 
○	Dimension: Scalar
○	Description: Variable holds the String Representation of Countries associated with each River. 
○	Range of Values: Strings with comma-separated Country names
○	Initial Value: No initial value outside the loop
●	all_countries:
○	Type: List
○	Dimension: 1-dimensional
○	Description: Variable accumulates ALL Countries from the Values of the Dictionary.
○	Range of Values: Lists containing Strings of Country Names
○	Initial Value: No initial value. Starts as an Empty List.

# Software Components: 
Class: River
●	Properties:
○	‘Name’: Name of the River; String
○	‘Countries’: List of Countries where the River runs through
●	Methods: 
○	‘Init’ (self, name: str, countries: list): Initializes a River object with a Name and list of countries
○	‘Get_name’ (self, str): Returns the name of the River
○	‘Get_countries’ (self, str): Returns the Name of the Country
Class: Country
●	Properties:
○	‘Name’: Name of the Country; String
●	Methods: 
○	‘Init’ (self, str): Initalizes a Country object with a  Name
○	‘Get_name’ (self, str): Returns the Name of the Country
Class: Country


# UML class diagram:
●	CLASS: River
○	Properties:
■	Name: String
■	Countries: List of Strings
○	Methods:
■	Init (Name: str, Countries: list)
■	Get_name ( ): str
■	Get_countreis ( ) list
●	CLASS: Country
○	Properties:
■	Name: String
○	Methods:
■	Init (Name: str)
■	Get_name ( ): str

# Algorithms defined in Processing Logic:
No Algorithms defined but the Rivers Program uses Loops; Prints Statements about each river and their associated countries, Prints Names of Rivers contained in the Dictionary, and Prints Names of Countreis in Alphabetical Order using ‘sort ( )’. 



# Testing
Input Data:
●	‘Nile River’: [‘Egypt’, ‘Sudan’, ‘Uganda’, ‘Ethopia’, ‘Kenya’, ‘Tanzania’, ‘Rwanda’, ‘Burundi’, ‘Democratic Republic of the Congo’],
●	‘Amazon River’: [‘Brazil’, ‘Peru’, ‘Colombia’, ‘Venezuela’, ‘Ecuador’, ‘Bolivia’, ‘Guyana’],
●	‘Mississippi River’: [‘United States of America’, ‘Canada’].

Expected Output Data:
●	Looped Statement about each River and Countries it runs through: 
○	“The Nile River runs through Egypt, Sudan, Uganda, Ethiopia, Kenya, Tanzania, Rwanda, Burundi, Democratic Republic of the Congo”
○	“The Amazon River runs through Brazil, Peru, Colombia, Venezuela, Ecuador, Bolivia, Guyana.”
○	“The Mississippi River runs through United States of America, Canada.”
●	Loop to Include every River in the Dictionary: 
○	Nile River
○	Amazon River
○	Mississippi River
●	Loop to include every Country in the Dictionary; in order alphabetically, optional: 
○	Bolivia
○	Brazil
○	Burundi
○	Canada
○	Colombia
○	Democratic Republic of the Congo
○	Ecuador
○	Egypt
○	Ethiopia
○	Guyana
○	Kenya
○	Peru
○	Rwanda
○	Sudan
○	Tanzania
○	United States of America
○	Uganda
○	Venezuela

Success Criteria: 
●	Each River and the Country it runs through should be correct. 
●	The Names of all Rivers should be listed correctly. 
●	The Names of all Countries should be listed correctly
○	Optional: Countries should be listed correctly in Alphabetical order
