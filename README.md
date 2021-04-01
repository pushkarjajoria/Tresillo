# Tresillo Rythm: 

## Research question: 

**Can we detect the “Tresillo” rhythm in music pieces given a MIDI file? Did the popularity of the “Tresillo” increase over the past few decades?**
-   Design an algorithm to detect the "Tresillo" rhythm pattern  given a MIDI file of a song

-   Long term developpement of the use of the "Tresillo" rhythm pattern in popular music (US-charts) 

-   The larger context of the research questions is the growing influence of Latin American music on US and European popular music. This reflects onto a general topic of globalized popular music.  
-   It seems that western popular music has become increasingly influenced by Latin music.When looking at the charts or listening to the radio, there seems to be more and more songs with Spanish lyrics or latin American artists. It would be very interesting to see if this perceived influence can be empirically traced and represented by underlying musical properties e.i. Rythm


-   Possible outcomes may show a change over time, leading to new questions trying to explain the observed change. The use of the rhythm could also be static over time. 

## Concepts and data 

-   The concret focus of the project lays in analyzing popular songs (as e.g. expressed in charts) over a certain period of time by looking at their rhythmic structure to see if they use the tresillo rhythm. 

-   Writing a rhythm detection algorithm and applying it to a popular music dataset 

-   Billboard archive for chart informations, Spotify API, Millions song dataset 


## Methods 

-   Rhythm analysis 
-   Time series analysis 

## Literature 

-   "The latin tinge" -- John Storm Roberts 

-   RHYTHMIC PATTERN MODELING FOR BEAT AND DOWNBEATTRACKING IN MUSICAL AUDIO [Florian Krebs. Sebastian Böck, Gerhard Widmer] 

-   The Cambridge companion to rhythm 

-   From Genre Classification to Rhythm Similarity: Computational and Musicological Insights -Esparza, Tlacael Miguel; Bello, Juan Pablo; Humphrey, Eric J. 

*The questions is not directly addressed in any publication I could find, there are older puplications who examine the influence of latin music to the US music in general.*  

## Contribution/Help 

-   How to develop a algorithm that is fine grained enough to detect the underlaying tresillo rhythm 

-   Did the use of the tresillo rhythm increase over the past decades 

## Data Links

<https://colinraffel.com/projects/lmd/>

<https://www.mididb.com/genres/>
## Methods

**Classifier:** labeling around 100 “Tresillo” rhythm (given their base and drum line in a MIDI file), and 100 typical non-“Tresillo” . Training a simple classifier which can detect the “Tresillo” rhythm (logistic regression, SVM, nothing complicated)

**Modelling the “Tresillo” rhythm:** The “Tresillo” rhythm is clearly musically defined 
[musically defined](https://en.wikipedia.org/wiki/Tresillo_(rhythm)) therefore we might be able to programmatically define and extract it with a rule based approach



## Question for TA

-   How much manual labeling do we have to expect? Is the MIDI file format suitable for an ‘efficient’ programmatic data extraction & analysis?
-   Do you have additional resources & websites for popular music data? Are there legal restrictions on the data analysis of music?
-   In the methods part we describe a rule based approach and a machine-learning approach, what are your thoughts on that? Should we focus on one of those approaches?
-   How strict should we be in defining the rhythm?
-   Is the scope of the project managable (timewise and given our abilities)


