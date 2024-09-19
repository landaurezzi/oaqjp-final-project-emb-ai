from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        key = 'dominant_emotion'
        # Statement: I am glad this happened
        # Dominant Emotion: joy
        result_1 = emotion_detection('I am glad this happened')
        self.assertEqual(result_1[key], 'anger')
        # Statement: I am glad this happened
        # Dominant Emotion: joy
        result_2 = emotion_detection('I am really mad about this')
        self.assertEqual(result_2[key], 'anger')
        # Statement: I am glad this happened
        # Dominant Emotion: joy
        result_3 = emotion_detection('I feel disgusted just hearing about this')
        self.assertEqual(result_3[key], 'anger')
        # Statement: I am glad this happened
        # Dominant Emotion: joy
        result_4 = emotion_detection('I am so sad about this')
        self.assertEqual(result_4[key], 'anger')
        # Statement: I am glad this happened
        # Dominant Emotion: joy
        result_5 = emotion_detection('I am really afraid that this will happen')
        self.assertEqual(result_5[key], 'anger')

unittest.main()