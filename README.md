





# Tresillo Rythm: 

## Research question: 

**Did the popularity of the `Tresillo` increase over the past few decades?**
- This above goal also inherently includes the question **Can we detect the `Tresillo` rhythm in music pieces given a MIDI file?**

## Motivation & Goals: 
The signature Tresillo beat in US pop music is steadily rising, noticeable by an increasing number of hits using this beat. From Ed Sheeran’s “Shape of you” to “Cheap Thrills” from sia. The influence can also be seen in a lot of tracks from Drake (For instance, Passionfruit). There is a noticeable increase in the number of western pop songs which use this signature latin rhythm with it’s triplet pattern and some other variants, without sounding like Latin songs. It would be very interesting to see how big of an influence this rhythm has right now and how it increased/decreased over the past years. This main aim of the project is to measure the use of the triplet pattern from tresillo rhythm on the western pop culture. We plan to do this by analysing the top 100 songs from billboard over the years. 
Possible outcomes may show a change over time, leading to new questions trying to explain the observed change. The use of the rhythm could also be static over time. 

## Concepts 

-   The concret focus of the project lays in analyzing popular songs (i.e top billboard songs over the years) by looking at their rhythmic structure to see if they use the tresillo rhythm. 

-   Writing a rhythm detection algorithm and applying it to a popular music dataset 

-   Using this data to visualize the popularity of Tresillo rhythm over the years. 


## Methods/Rhythm analysis

This empirical study requires us to classify songs into 2 categories, which are 
Song which have a triplet pattern running over a 4/4 meter 
Songs which either do not have this triplet pattern or the triplet pattern is part of some other meter.
Upon preliminary analysis and study, we have come up with the following directions to approach this problem. 
### Machine Learning Classifier
One of the ways to classify if a song belongs to a tresillo group defined above is to use a classifier such as an SVM or if need be, a neural network. The input to this classifier will be a (n x 8) timeseries, constructed from the first 30 bars of a song. To construct this time series matrix, we first need to find the bpm of a song. For this we can use the information provided in the midi file. If such information is not present in the midi file, depending on the number of such instances, we can either use the Echo Nest API provided by Spotify* to find the bpm of a song, otherwise we can ignore the song if the total number is limited.
Once we have the BPM for a song, we’ll mark 8 points (Eighth note points) on the time dimension and check if for activation (i.e. any beat from either the drum or the bass, if drum is not present) in the vicinity of these points, in the midi file.
This multihot array is stacked for `n` bars of a song to form the input timeseries.
To create the training dataset, there is no easy way to find a published list of songs with tresillo rhythm (and all its variants) by a qualified musician. We can do the task manually for a limited number of songs by checking the resources about that song online. The downside of this would be that there would not be 1 single scholarly source for this training dataset and also there would only be a limited number of songs from the manual labelling. Hence the model might not show a very high precision and recall.
As an extensions of the above, we can 
- Include 3 instruments (Rhythm Percussion and Bass) instead of 1.
- Consider 16th notes instead of 8th notes.
- Supplement with velocities of the beats aswell. (i.e. change the input from multihot to [0-1] velocity based activations.)
### Using Existing Literature

### Modeling Tresillo rhythm
This approach is most well suited if we have a single definition of tresillo rhythm. A preprocessing similar to the machine learning approach could then be extended to formally define the activation patterns and the strong beat. Although this is more formally defined and is not a black box, it would be difficult to model such an approach for a family of rhythms and their neighboring embellishments. 

## Literature 
- Pesek, M., Leonardis, A., & Marolt, M. (2020). An analysis of rhythmic patterns with unsupervised learning. Applied Sciences, 10(1), 178.
- Krebs, F., Böck, S., & Widmer, G. (2013, November). Rhythmic Pattern Modeling for Beat and Downbeat Tracking in Musical Audio. In Ismir (pp. 227-232).
- Esparza, T. M., Bello, J. P., & Humphrey, E. J. (2015). From genre classification to rhythm similarity: Computational and musicological insights. Journal of New Music Research, 44(1), 39-57.
- Rohrmeier, M. (2020). Towards a formalization of musical rhythm. In Proc. of the 21st Int. Society for Music Information Retrieval Conf.

## Data Links
There is no 1 single source for the corpus so we'll have to create it from a bigger dataset like the [Lakh Midi Dataset](https://colinraffel.com/projects/lmd/ "The Lakh MIDI Dataset v0.1") by filtering over the metadata based on fuzzy search from a list of songs. This list of songs is available on billboard archives.
Other dataset to consider is [MidiDB](https://www.mididb.com/genres/).
