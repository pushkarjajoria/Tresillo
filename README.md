





# Tresillo Rythm: 

## Research question: 

**Did the popularity of the `Tresillo` increase over the past few decades?**  
This above goal also inherently includes the question **Can we detect the `Tresillo` rhythm in music pieces given a MIDI file?**

## Motivation & Goals: 
The Tresillo beat seem to have gained popularity in recent decades in US pop music. It seems that a noticeable number of pop and dance music songs use this beat and creat memorable and highly successful music with it. From Ed Sheeran’s “Shape of you” to sia's “Cheap Thrills” or the music of US American rapper Drake (e.g.: Passionfruit). This devolpment has been noticed by several institutional and idependent media outlets (e.g.: [Syncopation, Dancehall & Coldplay by Jasper Emmitt](https://medium.com/@jasperemmitt/syncopation-dancehall-coldplay-ede27c6d01cf)). Similar story is also cover by many independent content creators as well, for instance in [Tresillo - The Rhythm of 2010s Pop Music](https://www.youtube.com/watch?v=DZ_yT_ukkKA) David Bennett talks about the origins and widespread of this rhythm. Although our aim is limited to pop music, the influence of this rhythm extends to other genres aswell. Habanera, a slight variation adding a back beat over the tresillo pattern, can be heard in the opera [Carmen](https://www.youtube.com/watch?v=KJ_HHRJf0xg) by French composer Georges Bizet. Originally a latin or african rhythm pattern, consisting of a tripplet beat played in the space of two macrobeats, the rythm has also been successfully 'westernised' and is now often employed without sounding 'latin'.  

//Latin or african rytm pattern?, //other word for westernised?

In our project we would like to conduct a empiric study of the influence and usage of the Tresillo rhythm. Thus we would like to trace the use of the Tresillo rhythm in western popular music. As main data we would inverstage feasibel top 100 billboard songs over the years. Possible outcomes may show a change over time, leading to new questions trying to explain the observed change. The use of the rhythm could also be static over time.
However preceeding, the empirical tracking of the popuarity of the rhythm, we will have to creat a rhythm detection algorithm which can detect the use of the  Tresillo rhythm given a suitable data format (e.g.: MIDI)



## Concepts // should we keep this part or change it to a comprehensive text?

-   The concret focus of the project lays in analyzing popular songs (i.e top billboard songs over the years) by looking at their rhythmic structure to see if they use the tresillo rhythm. 

-   Writing a rhythm detection algorithm and applying it to a popular music dataset 

-   Using this data to visualize the popularity of Tresillo rhythm over the years. 


## Methods/Rhythm analysis

This empirical study requires us to classify songs into 2 categories: 
1) Song which have a triplet pattern running over a 4/4 meter 
2) Songs which either do not have this triplet pattern or the triplet pattern is part of some other meter.

Upon preliminary analysis and study, we have come up with the following directions to approach this problem. 
### 1. Machine Learning Classifier
One of the ways to classify if a song belongs to a tresillo group, as defined above, is to use a classifier such as an SVM or if needed, a neural network. The input to this classifier will be a (n x 8) timeseries, constructed from the first `n` bars of a song. To construct this time series matrix, we first need to find the bpm of a song. For this we can use the information provided in the midi file. If such information is not present in the midi file, depending on the number of such instances, we can either use the Echo Nest API provided by Spotify* to find the bpm of a song, otherwise we can ignore the song if the total number is negible.
Once we have the BPM for a song, we’ll mark 8 points (Eighth note points) on the time dimension and check if for activation (i.e. any beat from either the drum or the bass, if drum is not present) in the vicinity of these points, in the midi file. This multihot array is stacked for `n` bars of a song to form the input timeseries.

To create a training dataset, optimally we would like to have a published data set, labeled by qualified musicians concerning the presence of the tresillo rhythm (and all its variants), however we are not aware of any such data set. However, we can do the task manually for a limited number of songs by checking the resources about a given song online. The downside of this is, that there would be not be one single scholarly source for this training dataset and furthermore we are probably only able to manually label a limited number of songs.  

As an extensions of the above, we can 
- Include 3 instruments (Rhythm, Percussion and Bass) instead of 1.
- Consider 16th notes instead of 8th notes.
- Supplement with velocities of the beats aswell. (i.e. change the input from multihot _0/1 activations_ to _[0,1] velocity based activations_.)
### 2. Using Existing Literature

### 3. Modeling Tresillo rhythm
This approach is most well suited if we have a single definition of tresillo rhythm. A preprocessing similar to the machine learning approach could then be extended to formally define the activation patterns and the strong beat. Although this is more formally defined and is not a black box, it would be difficult to model such an approach for a family of rhythms and their neighboring embellishments. 

### Limitations and Evaluation
Both proposed methods have inherent limitations and might not produce reliable results. 1) Concerning the Machine Learning method, data quality and quantity limitations might lead to an unreliable classifier. 2) Concerning modelling the Tresillo rhythm, it might require a lot of fine tuning and might be over-sensitive to small changes in parameters.  
Given those limitations, our project will require a through evaluation of the qulaity of our methods. Thus a test set is needed on which we can quantify the reliability of our methods with suitable metrics (precision, recall, accuracy, etc.)  

## Literature 
- Pesek, M., Leonardis, A., & Marolt, M. (2020). An analysis of rhythmic patterns with unsupervised learning. Applied Sciences, 10(1), 178.
- Krebs, F., Böck, S., & Widmer, G. (2013, November). Rhythmic Pattern Modeling for Beat and Downbeat Tracking in Musical Audio. In Ismir (pp. 227-232).
- Esparza, T. M., Bello, J. P., & Humphrey, E. J. (2015). From genre classification to rhythm similarity: Computational and musicological insights. Journal of New Music Research, 44(1), 39-57.
- Rohrmeier, M. (2020). Towards a formalization of musical rhythm. In Proc. of the 21st Int. Society for Music Information Retrieval Conf.

## Data Links
There is no 1 single source for the corpus so we'll have to create it from a bigger dataset like the [Lakh Midi Dataset](https://colinraffel.com/projects/lmd/ "The Lakh MIDI Dataset v0.1") by filtering over the metadata based on fuzzy search from a list of songs. This list of songs is available on billboard archives, or from [independed sources](https://data.world/kcmillersean/billboard-hot-100-1958-2017 "Billboard Hot weekly charts - Data.world") which have scraped the data from their websites.
Other dataset to consider is [MidiDB](https://www.mididb.com/genres/).
