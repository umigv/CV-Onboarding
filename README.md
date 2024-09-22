# CV-Onboarding
Onboarding resources for University of Michigan Autonomous Robotic Vehicle Team (2024-25)

## Announcements:
1) If you skipped the computer science section make sure to still follow the make your own branch instructions inside of [Git Intro](https://github.com/umigv/CV-Onboarding/blob/main/Introduction/Git_intro.md)
2) **IMPORTANT**: A bug arose for the YOLO training notebooks in the last week. You **MUST** use the updated version (9/22) of the YOLO notebooks in order for your code to work. The updated version is linked to, but if you already copied the Colabs, you will need to do that with the updated version. We are not sure if this fix will become redundant or cause other issues in the future (falls back to an outdated version), so please let Ryan or Matt know if you can't get the training stage to work. "TypeError: unhashable type: 'numpy.ndarray'" likely means you are on the old notebooks.
3) Make sure you fill out the Google form at the start of each meeting [this check in](https://forms.gle/yRPz1u5exbgAoyWV6)
4) We will add you to the dropbox on this Sunday's meeting
5) Common errors section added under tutorials
6) *Note:* if you rush through setting up your python environment and do it improperly, it may cause difficult to debug errors later on and may require totally restarting

Hi everyone! Welcome to the team. Please go through onboarding sections that you have been assigned to get you prepared for the year. Please complete [this check in](https://forms.gle/yRPz1u5exbgAoyWV6) at the beginning of each meeting.


## Tutorials:
1. [Background Information](./Introduction/background_info.md)
2. [Introduction to Computer Science](./Introduction/cs_intro.md)
3. [Introduction to Computer Vision](./Introduction/cv_intro.md)
4. [Introduction to Machine Learning](./Machine_Learning/ml_intro.md)
5. [Computer Vision Techniques](./CV_Techniques/cv_advanced.md)
6. [Advanced Machine Learning](./Machine_Learning/ml_advanced.md)

## Common Errors
1. This is not a git repo. Make sure you 1) properly cd into the CV onboarding and 2) git init, to initialize the repository on your device 3) if those don't work make sure you have git on your computer
3. YOLO training  "TypeError: unhashable type: 'numpy.ndarray'", see announcement 2 above
4. YOLO api key unauthorized. This should not happen but it has to some members. If it happens to you let Ryan know and he will manually send you an api key
5. Make sure you actually INSTALLED python onto your computer
6. In general make sure you are properly cd'd into the right place with the terminal you are using

## Find a Project that Fits Your Interests:
[Here](https://docs.google.com/document/d/1ef634SJfdRXIakzqJhP0OFhtHrR2Q5_G9onW3h-ZJHI/edit) is a list of projects that we are interested in pursuing as a team. As you move through onboarding it may be a good idea to read through this list to see what you are interested in and focus mostly on the onboarding that relates closely to the project. 

Additionally, we are always open to new projects and ideas so feel free to pitch any project to either Matt or Ryan at any time throughout the year.

##

[Integration Resources](./Integration/integration.md) 

Julia (Optional: for those interested in CV applications of computational programming)
1. [Introduction to Julia Programming](./Julia/julia_intro.md)
2. [Using Julia for ARV](./Julia/julia_advanced.md)
- Let us know if you have any ideas for Julia projects you would like to pursue.



## Finished Onboarding
Once you have finished onboarding, navigate to [this link](https://github.com/AwrodHaghiTabrizi/UMARV-CV-ScenePerception) and familiarize yourself with the repository as this is where most of our projects and models will be kept. Make sure to carefully follow any instructions on the readme.
