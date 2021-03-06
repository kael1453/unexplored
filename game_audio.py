"""
For all of the game's audio files, these are all loaded
into the game using the load_audio function.

Import this as 'a' for consistency.
"""
import arcade

# Example usage.
# arcade.play_sound(a.sound[f'jump_1'])

# Contains the names of all the audio files in the game
# once the 'add_audio_to_list()' is called.
audio_list = []

# Dictionary that contains the names of the sounds and their respective audio files.
# This is what is accessed whenever a sound is called.
sound = {}


def add_audio_to_list():
    """Loads all the names of the audio files and puts them into audio_list."""
    audio_list.append('ak_47_fire')
    audio_list.append('ak_47_reload')
    audio_list.append('clip_load')
    audio_list.append('explosion')
    audio_list.append('glock_17_fire')
    audio_list.append('glock_17_reload')
    audio_list.append('gun_pickup_1')
    audio_list.append('gun_pickup_2')
    audio_list.append('jump_1')
    audio_list.append('jump_2')
    for i in range(4):
        audio_list.append(f'landing_on_gravel_{i + 1}')
    audio_list.append('landing_on_stone')
    audio_list.append('landing_on_wood')
    for i in range(8):
        audio_list.append(f'run_grass_{i + 1}')
    for i in range(8):
        audio_list.append(f'run_gravel_{i + 1}')
    for i in range(8):
        audio_list.append(f'run_stone_{i + 1}')
    for i in range(8):
        audio_list.append(f'run_wood_{i + 1}')
    audio_list.append('shell_load')
    audio_list.append('shotgun_reload')
    for i in range(8):
        audio_list.append(f'walk_grass_{i + 1}')
    for i in range(8):
        audio_list.append(f'walk_gravel_{i + 1}')
    for i in range(8):
        audio_list.append(f'walk_stone_{i + 1}')
    for i in range(8):
        audio_list.append(f'walk_wood_{i + 1}')
    return audio_list


def load_audio():
    for i in audio_list:
        # Load the audio into the dictionary.
        sound[f'{i}'.format(i)] = arcade.load_sound(f'resources/audio/{i}.wav')
