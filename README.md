# zeepai
A program to allow code based generation of basic zeepkist levels for human or AI use.

Many simple track pieces implemented.

Simply replace the track_sequence with the one ChatGPT gives you.

```
python .\trackgen.py
```

This will create AND SUBSEQUENLY OVERWRITE a folder in the zeepkist levels folder of windows %APPDATA%. Try out your track, save it with a new name if you want to keep it.

Below is the prompt I settled on for interfacing with ChatGPT. GPT-4 performed much better. The prompt had to be more strict to stop GPT-3.5 from going into a loop and never ending the track.

After entering the large prompt you can then do stuff like this:
```
Make me a track that starts off with a strong booster, 5 straight peices then a slope bottom up, 10 gap pieces and then 5 more straights and a finish.
```
and receive your track ready to go.

```
Your task is to design a track for the gravity-based racing game, "Zeepkist". You'll need to consider elements like gravity, momentum, turns and track inclination. Our track starts at the top of a hill. Your track design should follow the rules and pieces mentioned below, and should aim for excitement and fun. After reading the following guidelines and available pieces, please provide a short Python list with tuples describing the track sequence. 

Rules for track design:

0. The track sequence must have less than 30 items being fairly level or downhill.
1. Start the track with a 'start' piece and end with a 'finish' piece.
2. Include one or more 'checkpoint' and 'booster' pieces in between.
3. If the track is not starting on a downhill, place a 'booster' piece immediately after the start to accelerate the cars. It should probably have a force of 1-3 and a speed of 80-150.
4. Up sections must be preceded by a moderate 'booster' piece to maintain speed.
5. Avoid placing 'booster' pieces before small, sharp turns.
6. Avoid having sharp turns immediately after an uphill.
7. Curves are 90-degree turns extending across the grid space indicated in their name.
8. The track should be primarily level or downhill to minimize the need for boosters.
9. 'Left', 'right', 'up', and 'down' in piece names indicate the direction the track will take.
10. Jumps are good but there must be enough speed and landing clearance.
11. The gap pieces will leave a blank space for a jump, a level gap will need to follow an up piece or a fairly speedy 'booster' piece.
12. Boosters have a force and a speed where force is 1-10 and speed is 30-200. A force of 10 will immediately apply the speed. A force of 3 is a good mid-ground. 200 is the top speed and can only be maintained on straight or gently turning tracks, 80-120 is a good mid-ground.
13. Going off of an up for a jump or gap at 100 speed or more will result in a jump of approximately 4-5 grid spaces in a straight line. Ensure there is enough space to land.
14. An increase in 1 height results in a loss of about 30 speed.
15. A decrease of height 1 that is not a jump gains 20 speed.
16. Each length of turning a curve loses about 5 speed.
17. Ups that are a size 1 are harsh at high speeds.
18. Slope Tops are meant to be used at the tops of uphills and bottoms at the bottom of downhills or receiving end of a jump or gap down and not standalone.
0. The track sequence must have less than 30 items being fairly level or downhill.

Here are the track components at your disposal:

    Horizontal sections: gap_level_1, gap_down_1, flat_road_1
    Start and end: start_with_icon_1, finish_with_icon_1
    Booster: booster_1

    Turns: road_curve_left_1, road_curve_right_1, road_curve_right_2, road_curve_left_3, road_curve_right_3, road_curve_left_4, road_curve_right_4

    Steep Vertical sections: road_step_up_2, road_step_up_3, road_step_up_1, road_step_down_2, road_step_down_3, road_step_down_1

    Slopes: road_slope_up_top_2, road_slope_down_top_2, road_slope_down_bottom_2, road_slope_up_bottom_2, road_slope_up_flat_1, road_slope_down_flat, road_slope_up_top_1, road_slope_down_top_1, road_slope_up_bottom_1, road_slope_down_bottom_1, road_shallow_slope_bottom_2, road_shallow_slope_top_2, road_shallow_slope_up_flat_1, road_shallow_slope_down_flat_1

    Checkpoints: road_checkpoint_with_icon_1

Here's a simple track example for your reference:

python

track_sequence = [
    ("start_with_icon_1", {}), #start
    ("booster_1", {"booster_force": 1, "booster_speed": 150}), # booster specifications
    * [("flat_road_1", {}) for _ in range(4)], # four flat road sections
    ("road_checkpoint_with_icon_1", {}), # checkpoint
    ("road_curve_left_1", {}), # left turn
    ("road_curve_right_1", {}), # right turn
    ("booster_1", {"booster_force": 2, "booster_speed": 80}), #booster for uphill
    ("road_slope_up_bottom_1", {}),
    ("road_checkpoint_with_icon_1", {}), # checkpoint
    * [("flat_road_1", {}) for _ in range(4)], # four more flat road sections
    ("finish_with_icon_1", {}), #finish
]

Using the rules and components provided, please design an exciting, fun Zeepkist track as a Python list with tuples like in the example above. Try to ensure your track has a good balance of speed, thrill, and challenge!
```
