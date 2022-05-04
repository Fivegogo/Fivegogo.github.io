---
title: MUSIC-Synthetic dataset
summary: 3333
dataset: true
# Optional external URL for project (replaces project detail page).
external_link: https://zenodo.org/record/4079386#.X4PFodozbb2

image:
  caption: 
  focal_point: Smart

---
We build category-balanced multi-source videos by artificially synthesizing solo videos from the MUSIC dataset to facilitate the learning and evaluation of multiple-soundings-sources localization in the cocktail-party scenario. Concretely, we first randomly choose four 1-second solo audiovisual pairs of different categories, then mix random two of the four audio clips with jittering as the multi-source audio waveform, and concatenate four frames of these clips as the multi-source video frame. That is, in the synthesized audiovisual pairs, there are two instruments making sound while the other two are silent. Therefore, this synthesized dataset is quite proper for the evaluation of discriminatively sounding object localization and we also find it generalizes well in the real-world scenarios. For more details about this dataset, please refer to our paper. [Download this dataset here](https://zenodo.org/record/4079386#.X4PFodozbb2)