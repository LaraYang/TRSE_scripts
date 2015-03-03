#!/bin/bash
# copy over Taraz's TMS dataset.


for s in 106 107 108 109 110 111 112 113 114 115 116 117 118; do
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/both_faces.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_both_face.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/both_scenes.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_both_scene.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/categorize_faces.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_categorize_face.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/categorize_scenes.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_categorize_scene.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/relevant_faces.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_relevant_face.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/relevant_scenes.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_relevant_scene.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/irrelevant_faces.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_irrelevant_face.txt
	cp /home/despoB/kaihwang/TRSETMS/${s}/PRE/behavior/irrelevant_scenes.txt /home/despoB/kaihwang/TRSE/TRSE_scripts/${s}_irrelevant_scene.txt

done