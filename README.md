# Tresillo Rythm: 

## Research question: 

<p align="center">
**"Did the popularity of the `Tresillo` increase over the past few decades?"**
</p>
- This above goal also inherently includes the question **Can we detect the `Tresillo` rhythm in music pieces given a MIDI file?**

## Motivation & Goals: 
-   Design an algorithm to detect the "Tresillo" rhythm pattern  given a MIDI file of a song

-   Long term developpement of the use of the "Tresillo" rhythm pattern in popular music (US-charts) 

-   The larger context of the research questions is the growing influence of Latin American music on US and European popular music. This reflects onto a general topic of globalized popular music.  
-   It seems that western popular music has become increasingly influenced by Latin music.When looking at the charts or listening to the radio, there seems to be more and more songs with Spanish lyrics or latin American artists. It would be very interesting to see if this perceived influence can be empirically traced and represented by underlying musical properties e.i. Rythm
-   An Analysis of Rhythmic Patterns with Unsupervised Learning - Pesek, Matevž; Leonardis, Aleš; Marolt, Matija

-   Possible outcomes may show a change over time, leading to new questions trying to explain the observed change. The use of the rhythm could also be static over time. 

## Concepts and data 

-   The concret focus of the project lays in analyzing popular songs (as e.g. expressed in charts) over a certain period of time by looking at their rhythmic structure to see if they use the tresillo rhythm. 

-   Writing a rhythm detection algorithm and applying it to a popular music dataset 

-   Billboard archive for chart informations, Spotify API, Millions song dataset 


## Methods 

-   Rhythm analysis 
    - It is important to note that there is a collection of Rhythms very similar to Tresillo in Latin American rhythms. One instance of this is the Cinquillo Rhythm, a common embellishment of tresillo by adding eighth notes to the Tresillo rhythm. This raises the question of what qualifies as a Tresillo beat as many song's add/embellish the beat with added notes (similar to Cinquillo). The Son-Clave also has the same triplet pattern in the first half of the beat, should we include it in our analysis aswell?
    - We need to detect the existence of tresillo beat in the song by either:
        1. Training a classifier by using the list of existing songs we know about.
        2. Write a program to detect the triplet pattern of the tresillo beat.
-   Time series analysis 

## Literature 
-   An Analysis of Rhythmic Patterns with Unsupervised Learning - Pesek, Matevž; Leonardis, Aleš; Marolt, Matija
-   "The latin tinge" -- John Storm Roberts 

-   RHYTHMIC PATTERN MODELING FOR BEAT AND DOWNBEATTRACKING IN MUSICAL AUDIO [Florian Krebs. Sebastian Böck, Gerhard Widmer] 

-   The Cambridge companion to rhythm 

-   From Genre Classification to Rhythm Similarity: Computational and Musicological Insights -Esparza, Tlacael Miguel; Bello, Juan Pablo; Humphrey, Eric J. 

*This questions is not directly addressed in any publication we could find, there are older puplications who examine the influence of latin music to the US music in general.*  

## Contribution/Help 

-   How to develop a algorithm that is fine grained enough to detect the underlaying tresillo rhythm 

-   Did the use of the tresillo rhythm increase over the past decades 

## Data Links

<https://colinraffel.com/projects/lmd/>

<https://www.mididb.com/genres/>
## Methods

**Classifier:** labeling around 100 “Tresillo” rhythm (given their base and drum line in a MIDI file), and 100 typical non-“Tresillo” . Training a simple classifier which can detect the “Tresillo” rhythm (logistic regression, SVM, nothing complicated)

**Modelling the “Tresillo” rhythm:** The “Tresillo” rhythm is clearly 
[musically defined](https://en.wikipedia.org/wiki/Tresillo_(rhythm)) therefore we might be able to programmatically define and extract it with a rule based approach



## Question for TA

-   How much manual labeling do we have to expect? Is the MIDI file format suitable for an ‘efficient’ programmatic data extraction & analysis?
-   Do you have additional resources & websites for popular music data? Are there legal restrictions on the data analysis of music?
-   In the methods part we describe a rule based approach and a machine-learning approach, what are your thoughts on that? Should we focus on one of those approaches?
-   How strict should we be in defining the rhythm?
-   Is the scope of the project managable (timewise and given our abilities)?
