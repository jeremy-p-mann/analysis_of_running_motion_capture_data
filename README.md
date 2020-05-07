# analysis_of_running_motion_capture_data

Personal vanity project analyzing motion capture data of the dynamics of competitive/elite runners.

Paper introducing dataset:

*A public dataset of running biomechanics and the effects of running speed on lower extremity kinematics and kinetics*

Reginaldo K. Fukuchi, Claudiane A. Fukuchi and Marcos Duarte

TBH I have zero interest in the optimize-for-performance aspect of running. My interests lie in optimizing the gait cycle's role in a single human's longevity.

I honestly have no metric (other than hard-to-come-by hard outcomes) for this optimization problem. However, two general features of solutions to "biological" optimization problems are symmetry and regularity. This suggests a hypothesis too vague to form as a concrete, statistically well-posed hypothesis. 

Specifically, I'd like to be able to say something along the lines of "changes in blah biomarkers of gait irregularity and asymmetry (arising from data captured from the dynamics of your gait cycle) indicate that blah intervention was/wasn't effective in decreasing your risk of injury."

Therefore, the primary (albeit vague) goal of this repo is to produce reproducible and transparent quantifications of the irregularities and asymmetries in a single person's gait cycle. 

As the data is (albeit biased and missing half of the human body) very accurate, I felt that it would be a good playing ground to experiment with notions.

As for the approach, my gut tells me that this should be given by a combination of classical signal processing and wasserstein distances on distributions in phase space. Here, phase space has a degree of freedom (in three dimensions) for each landmark tracked.

