# Tresillo Rhythm: 

## Research Question: 

**Has the popularity of the `Tresillo` increased over the past few decades?**  
This goal inherently includes the question **Can we detect the `Tresillo` rhythm in music pieces given a MIDI file?**

## Motivation & Goals: 
The Tresillo beat has gained popularity in recent decades in US pop music. A noticeable number of pop and dance music songs utilize this beat to create memorable and highly successful music with it. From Ed Sheeran’s “Shape of You” to Sia's “Cheap Thrills” and the music of US American rapper Drake (e.g., Passionfruit). This development has been noticed by several institutional and independent media outlets (e.g., [Syncopation, Dancehall & Coldplay by Jasper Emmitt](https://medium.com/@jasperemmitt/syncopation-dancehall-coldplay-ede27c6d01cf) and [Tresillo - The Rhythm of 2010s Pop Music](https://www.youtube.com/watch?v=DZ_yT_ukkKA)). The originally Latin rhythm pattern, consisting of a triplet beat played over one bar of 4/4 meter, has traveled the world and is used in many different genres ([dance music](https://www.youtube.com/watch?v=JGwWNGJdvx8), [jazz](https://www.youtube.com/watch?v=4CtyQXFtu2U), [opera](https://www.youtube.com/watch?v=KJ_HHRJf0xg)).

In this work, we have conducted an empirical study of the influence and usage of the Tresillo rhythm. We have traced the increased/decreased use of the Tresillo rhythm in Western popular music. Using feasible top 100 Billboard songs over 20 years as our main data, possible outcomes may show a change over time, leading to new questions trying to explain the observed change. The use of the rhythm could also be static over time.
However, preceding the empirical tracking of the popularity of the rhythm, we have created a rhythm detection algorithm that can detect the use of the Tresillo rhythm given a suitable data format (e.g., MIDI).

## Concepts 

The concrete focus of the project lies in analyzing popular songs (i.e., top Billboard songs over the years) by looking at their rhythmic structure to see if they use the Tresillo rhythm. We have written a rhythm detection algorithm and applied it to a popular music dataset. Furthermore, using this dataset, we want to visualize the use of the Tresillo rhythm over time. 

## Data Links
There is no single source for the corpus, so we have created it from a bigger dataset like the [Lakh Midi Dataset](https://colinraffel.com/projects/lmd/ "The Lakh MIDI Dataset v0.1") by filtering over the metadata based on fuzzy searches from a list of songs. This list of songs is available on Billboard archives, or from [independent sources](https://data.world/kcmillersean/billboard-hot-100-1958-2017 "Billboard Hot weekly charts - Data.world") which have scraped the data from their websites.
Another dataset to consider is [MidiDB](https://www.mididb.com/genres/).