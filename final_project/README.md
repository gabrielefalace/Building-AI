# Classification of pigmented lesions of the nail bed

Final project for the Building AI course

## Summary

A system for recognizing potentially cancerous lesions of the nail bed.


## Background

Pigmented lesions in the nail bed can have a variety of sources: some more benign (such as hematoma), some more concerning (melanoma). 
Under-nail melanoma is really dangerous as the discoloration is often neglected or dismissed as unimportant and often is diagnosed as cancer too late.

Machine Learning can be used to classify the different lesions based on caracteristics or even images of the affected nails.


## How is it used?

The users could take pictures of the nail and answer some questions. The system would answer with a class "benign"/"potentially cancerous".

## Data sources and AI methods

Data should be gathered from dermatologists who work on these problems daily, collecting instances of both the above mentioned classes. 

The primary input would be images of the lesions. The Secondary source could be answers to questions (e.g. I hit my nail with an hammer could be useful to take into consideration). 

I would propose using a CNN to classify images and then use the additional information to skew the prediction a bit (towards the cautious side, promting the patient to maybe get that extra check).

## Challenges

The project is a high risk one (dealing with potentially life threatening conditions) and should undergo heavy MDR compliance.

## What next?

The ML project per se, if evolved, could be a consumer app where the user could self check nail discolorations and track them. The model could be extended also to cope with other pigmented lesions, not only those in the nail bed.

## Acknowledgments


