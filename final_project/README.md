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

The primary input would be images of the lesions. Like:
| Input       | Suspect Y/N   |
| ----------- | ------------- |
| image1      | Y             |
| image2      | N             |
| image3      | N             |
| ...         | ...           |

And a CNN could be built for this purpose.

The Secondary source could be answers to questions. Example:(e.g. did you hit your nail with an hammer? For how long has the lesion been there? Did the lesion change over time?).

The additional information could be used to build a second model (e.g. even simple rules) to be combined with the first to tweak the prediction a bit (towards the cautious side, promting the patient to maybe get that extra check).

## Challenges

The project is a high risk one (dealing with potentially life-threatening conditions) and should undergo heavy MDR compliance.

## What next?

The system could be provided with a consumer app, where the user could self-check nail discolorations and track them.
The model could be extended also to cope with other pigmented lesions, not only those in the nail bed.

## Acknowledgments

https://www.aimatmelanoma.org/melanoma-101/types-of-melanoma/cutaneous-melanoma/acral-lentiginous-melanoma/
https://www.aad.org/public/diseases/skin-cancer/types/common/melanoma/nail-melanoma
https://en.wikipedia.org/wiki/Subungual_hematoma
https://en.wikipedia.org/wiki/Melanonychia

