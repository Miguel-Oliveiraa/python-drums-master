CONFIG = {
    'hit_velocity_threshold': 1000,
    'drum_cooldown': 0.3,
    'drums': [
        {'name': 'Snare', 'pos': (0.5, 0.7), 'radius': 80, 'sound': 'sounds/snare_1.wav'},
        {'name': 'HiHat', 'pos': (0.3, 0.7), 'radius': 70, 'sound': 'sounds/hihat_1.wav'},
        {'name': 'Crash', 'pos': (0.7, 0.5), 'radius': 70, 'sound': 'sounds/crash_1.wav'},
    ],
    'camera_index': 0,
    'hands_config': {
        'max_num_hands': 2,
        'min_detection_confidence': 0.7,
        'min_tracking_confidence': 0.7
    },
    'fps': 60
}