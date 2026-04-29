# Bloodstained Randomizer Setup Guide

## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases/latest)
- [The Bloodstained AP World](https://github.com/vgfreak95/BloodstainedAP/releases/latest)
- [Lakifume's True Randomizer](https://github.com/Lakifume/True-Randomization/releases/latest)
- [Bloodstained Modding SDK](https://github.com/vgfreak95/BloodstainedModdingSDK/releases/latest)

## Terms for File locations
- Game Shipping Directory = steamapps\common\Bloodstained Ritual of the Night\BloodstainedRotN\Binaries\Win64

## How to play
First, you need a room to connect to. For this, you or someone you know has to generate a game.  
This will not be explained here,
but you can check the [Archipelago Setup Guide](/tutorial/Archipelago/setup_en#generating-a-game).

You also need to have [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases/latest) installed
and the [The Bloodstained AP World](https://github.com/vgfreak95/BloodstainedAP/releases/latest) installed into Archipelago.

Next there are two different ways to host the world. Whether you choose to host it locally or on the webhost, instructions are still the same.

## Setup for True Randomizer
1. Download [Lakifume's True Randomizer](https://github.com/Lakifume/True-Randomization/releases/latest).
2. Open Data/config.ini and find [Archipelago] and change bEnable from false to true.
3. Extract the zip file and find the Randomizer.exe file.

## Using the True Randomizer
4. Open the True Randomizer by double-clicking `Randomizer.exe`, and in the bottom left, select Empty preset.
5. Change the Game Difficulty in the bottom left.
6. Press the Generate button. Generating adds AP specific assets into the game which the AP Mod reads from.

## Setup for the Bloodstained AP Client
1. Download [Bloodstained Modding SDK](https://github.com/vgfreak95/BloodstainedModdingSDK/releases/latest) `version.dll`.
2. Navigate the File Explorer to your `Game Shipping Directory` (see Terms), and drag `version.dll` into the directory.
3. Still inside `Game Shipping Directory` remove `UE4SS.dll` and ensure `version.dll` is in the directory.
4. Launch game and load a new save file, once loaded, press F2 to open ImGui window. Note: You cannot connect to AP in the title the gui won't let you!
5. Insert the correct archipelago slot information and press connect!

## Important Things To Note
- `index.txt` is a file which contains an index. Do not remove this file while doing a playthrough. After a playthrough is completed, manually
set the value to -1. I do not currently handle the ability to reset this file, and solely leave it up to the player for now as its WIP.
- Enemies and Shards are CURRENTLY NOT SUPPORTED. If you receive a duplicate shard, that is expected behavior. The required logic shards are in the item pool
so even if you get duplicate shards by defeating bosses, any shards collected from defeating bosses aren't intended, so please do not use them for a fair
game to ensure true completion.
- When Bael is defeated the victory will not trigger, this is intentional as I haven't figured out a good way to send this flag, probably in next release 1.0.2 or 1.0.3.
- Please report any crashes, as this software is still in its early beta stages.
