"""
Content Moderation Engine - AI-Based Cyberbullying Detection Platform
Implements NLP-based text analysis, sentiment detection, and automated content moderation.
"""

import re
import json
import numpy as np


# Toxic word categories
TOXIC_KEYWORDS = {
    'profanity': ['stupid', 'idiot', 'loser', 'pathetic', 'useless', 'worthless', 'ugly',
                   'disgusting', 'kill yourself', 'go kill', 'disappear', 'hate', 'deserve'],
    'threats': ['beat', 'threat', 'make your life', 'make sure', 'spread photos', 'exposed'],
    'discrimination': ['village', 'poor', 'beggar', 'cheap clothes', 'accent', 'back where'],
    'mockery': ['laughing at', 'pretending', 'acting like', 'fake', 'pathetic excuse'],
    'intimidation': ['imprison', 'expelled', 'miserable', 'everyone hates', 'no one likes']
}


class SentimentAnalyzer:
    """Simple sentiment analysis based on keyword matching"""

    def __init__(self):
        self.positive_words = ['great', 'good', 'helpful', 'thanks', 'congratulations',
                                'enjoyed', 'amazing', 'useful', 'help', 'support',
                                'good luck', 'well done', 'brilliant', 'excellent']
        self.negative_words = list(set(
            w for words in TOXIC_KEYWORDS.values() for w in words
        ))

    def analyze_sentiment(self, text):
        text_lower = text.lower()
        pos_score = sum(1 for w in self.positive_words if w in text_lower)
        neg_score = sum(1 for w in self.negative_words if w in text_lower)

        total = pos_score + neg_score
        if total == 0:
            return 0.0  # neutral

        return round((pos_score - neg_score) / total, 4)


class ToxicityDetector:
    """Detects toxic content using keyword and pattern matching"""

    def __init__(self):
        self.categories = TOXIC_KEYWORDS

    def detect_toxicity(self, text):
        text_lower = text.lower()
        scores = {}
        for category, keywords in self.categories.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            scores[category] = score

        total_score = sum(scores.values())
        toxicity_level = self._classify_toxicity(total_score, text)

        return {
            'scores': scores,
            'total_score': total_score,
            'toxicity_level': toxicity_level,
            'is_toxic': total_score >= 2,
            'category': max(scores, key=scores.get) if total_score > 0 else 'none'
        }

    def _classify_toxicity(self, score, text):
        if score >= 5:
            return 'critical'
        elif score >= 3:
            return 'high'
        elif score >= 2:
            return 'medium'
        elif score >= 1:
            return 'low'
        return 'none'


class ContentModerator:
    """Main moderation engine that combines all detection modules"""

    def __init__(self):
        self.sentiment = SentimentAnalyzer()
        self.toxicity = ToxicityDetector()
        self.moderation_log = []

    def moderate_content(self, message):
        """Process a single message through all moderation checks"""
        text = message.get('text', '')

        # Sentiment analysis
        sentiment_score = self.sentiment.analyze_sentiment(text)

        # Toxicity detection
        toxicity_result = self.toxicity.detect_toxicity(text)

        # Determine moderation action
        action = self._determine_action(sentiment_score, toxicity_result)

        result = {
            'message_id': message.get('message_id'),
            'sender_id': message.get('sender_id'),
            'platform': message.get('platform'),
            'original_category': message.get('category'),
            'sentiment_score': sentiment_score,
            'toxicity_scores': toxicity_result['scores'],
            'total_toxicity': toxicity_result['total_score'],
            'toxicity_level': toxicity_result['toxicity_level'],
            'is_toxic': toxicity_result['is_toxic'],
            'primary_category': toxicity_result['category'],
            'moderation_action': action,
            'confidence': self._calculate_confidence(toxicity_result, sentiment_score)
        }

        self.moderation_log.append(result)
        return result

    def _determine_action(self, sentiment, toxicity):
        if toxicity['is_toxic'] and toxicity['total_score'] >= 5:
            return 'block_and_flag'
        elif toxicity['is_toxic'] and toxicity['total_score'] >= 3:
            return 'flag_for_review'
        elif toxicity['is_toxic']:
            return 'warning'
        elif sentiment < -0.5:
            return 'monitor'
        return 'allow'

    def _calculate_confidence(self, toxicity, sentiment):
        if toxicity['total_score'] >= 4:
            return round(0.90 + toxicity['total_score'] * 0.02, 2)
        elif toxicity['total_score'] >= 2:
            return round(0.75 + toxicity['total_score'] * 0.05, 2)
        return round(0.50 + abs(sentiment) * 0.3, 2)

    def get_statistics(self):
        total = len(self.moderation_log)
        if total == 0:
            return {}

        actions = {}
        categories = {}
        for log in self.moderation_log:
            action = log['moderation_action']
            actions[action] = actions.get(action, 0) + 1

            cat = log['primary_category']
            if cat != 'none':
                categories[cat] = categories.get(cat, 0) + 1

        correct = sum(1 for log in self.moderation_log
                      if log['original_category'] == 'bullying' and log['is_toxic'] or
                      log['original_category'] == 'safe' and not log['is_toxic'])

        return {
            'total_messages': total,
            'actions': actions,
            'categories': categories,
            'accuracy': round(correct / total, 4),
            'detection_rate': round(
                sum(1 for l in self.moderation_log if l['is_toxic']) /
                max(sum(1 for l in self.moderation_log if l['original_category'] == 'bullying'), 1), 4
            )
        }


if __name__ == '__main__':
    print("Testing Content Moderation Engine...")

    with open('/home/ubuntu/project/cyberbullying/cyberbullying_data.json', 'r') as f:
        data = json.load(f)

    moderator = ContentModerator()
    results = []

    for msg in data['messages'][:200]:
        result = moderator.moderate_content(msg)
        results.append(result)

    stats = moderator.get_statistics()
    print(f"\nModeration Statistics:")
    print(f"  Total Messages Processed: {stats['total_messages']}")
    print(f"  Accuracy: {stats['accuracy']}")
    print(f"  Detection Rate: {stats['detection_rate']}")
    print(f"\n  Actions:")
    for action, count in stats['actions'].items():
        print(f"    {action}: {count}")
    print(f"\n  Categories:")
    for cat, count in stats['categories'].items():
        print(f"    {cat}: {count}")
    print("\nModeration engine test complete!")
