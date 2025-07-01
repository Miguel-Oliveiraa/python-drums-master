import asyncio
import logging
from typing import Tuple, Dict
import cv2
import mediapipe as mp
from pygame import mixer
from playground.drum_kit import DrumKit
from config.config import CONFIG

# Configure logging
logger = logging.getLogger(__name__)

class VirtualDrums:
    """Main class for the virtual drums application."""
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = None
        self.cap = None
        self.kit = None
        self.prev_positions: Dict[int, Tuple[int, int, float]] = {}

    def setup(self) -> None:
        """Initialize pygame, MediaPipe, and camera."""
        try:
            mixer.init()
        except Exception as e:
            logger.error(f"Failed to initialize pygame mixer: {e}")
            raise

        try:
            self.hands = self.mp_hands.Hands(**CONFIG['hands_config'])
        except Exception as e:
            logger.error(f"Failed to initialize MediaPipe Hands: {e}")
            raise

        try:
            self.cap = cv2.VideoCapture(CONFIG['camera_index'])
            ret, frame = self.cap.read()
            if not ret:
                raise RuntimeError("Could not read from camera.")
            h, w = frame.shape[:2]
            self.kit = DrumKit((w, h))
        except Exception as e:
            logger.error(f"Camera initialization failed: {e}")
            raise

    def update_loop(self) -> None:
        """Process one frame of the video feed."""
        if not self.cap or not self.cap.isOpened():
            logger.error("Camera not initialized or closed.")
            return

        ret, frame = self.cap.read()
        if not ret:
            logger.warning("Failed to read frame from camera.")
            return

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
                lm = hand_landmarks.landmark[8]  # Index finger tip
                w, h = frame.shape[1], frame.shape[0]
                x, y = int(lm.x * w), int(lm.y * h)
                t = asyncio.get_event_loop().time()

                # Compute vertical velocity
                vel = 0.0
                if idx in self.prev_positions:
                    px, py, pt = self.prev_positions[idx]
                    dt = t - pt
                    vel = (y - py) / dt if dt > 0 else 0.0
                self.prev_positions[idx] = (x, y, t)

                # Process interaction
                self.kit.interact((x, y), vel)

                # Draw hand landmarks
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        self.kit.draw(frame)
        cv2.imshow('Virtual Drums', frame)

        # Check for exit key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("Exit requested by user.")
            raise SystemExit

    def cleanup(self) -> None:
        """Release resources."""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        if self.hands:
            self.hands.close()
        mixer.quit()
        logger.info("Resources cleaned up.")