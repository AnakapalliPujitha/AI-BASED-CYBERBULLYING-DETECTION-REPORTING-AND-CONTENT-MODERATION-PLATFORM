"""
Data Generator Module - AI-Based Cyberbullying Detection Platform
Generates realistic datasets: messages, user profiles, incidents, reports, and analytics.
"""

import json
import random
import numpy as np
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

OUTPUT_DIR = '/home/ubuntu/project/cyberbullying'

# ==================== USER PROFILES ====================
def generate_users():
    first_names = [
        'Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Ananya', 'Karthik', 'Meera',
        'Arjun', 'Divya', 'Rohan', 'Kavitha', 'Suresh', 'Lakshmi', 'Manoj', 'Pooja',
        'Ajay', 'Nithya', 'Ganesh', 'Swathi', 'Ravi', 'Saranya', 'Kumar', 'Shalini',
        'Deepak', 'Madhuri', 'Tarun', 'Vani', 'Hari', 'Geetha', 'Naveen', 'Radha',
        'Suresh', 'Bhanu', 'Praveen', 'Lalitha', 'Raju', 'Chandana', 'Mohan', 'Teja',
        'Sai', 'Bhavya', 'Nikhil', 'Varsha', 'Arun', 'Sridhar', 'Murali', 'Usha',
        'Venu', 'Padma', 'Sanjay', 'Rama', 'Krishna', 'Sujatha', 'Balaji', 'Mamatha'
    ]
    last_names = [
        'Sharma', 'Gupta', 'Singh', 'Reddy', 'Nair', 'Iyer', 'Patel', 'Kumar',
        'Das', 'Verma', 'Shah', 'Mehta', 'Rao', 'Chopra', 'Joshi', 'Agarwal'
    ]
    departments = ['CSE', 'ECE', 'EEE', 'ME', 'CE', 'IT', 'AIDS', 'CSE-AIML']
    years = ['I Year', 'II Year', 'III Year', 'IV Year']

    users = []
    for i in range(1, 121):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        role = random.choices(['student', 'faculty', 'admin', 'moderator'],
                              weights=[60, 20, 5, 15])[0]
        users.append({
            'user_id': f'USR{i:04d}',
            'name': f'{fn} {ln}',
            'role': role,
            'department': random.choice(departments) if role != 'admin' else 'Administration',
            'year': random.choice(years) if role == 'student' else 'N/A',
            'email': f'{fn.lower()}.{ln.lower()}@college.edu',
            'registration_date': (datetime(2024, 9, 1) + timedelta(days=random.randint(0, 180))).strftime('%Y-%m-%d'),
            'status': 'active'
        })
    return users


# ==================== SAMPLE MESSAGES ====================
BULLYING_MESSAGES = [
    "You are so stupid, why don't you just drop out?",
    "Nobody likes you, go back to your village",
    "You think you're smart? You failed every exam",
    "Stop acting like you belong here, loser",
    "Your family is so poor, why even come to college?",
    "I hope you get expelled, you don't deserve to be here",
    "Everyone is laughing at you behind your back",
    "You're such a pathetic excuse for a student",
    "Go kill yourself, nobody will miss you",
    "You're ugly and nobody wants to be friends with you",
    "I'll beat you up if I see you in the lab",
    "Your clothes are so cheap, you look like a beggar",
    "Stop talking to me, you're disgusting",
    "You'll never succeed in life, just give up",
    "I told everyone your secrets, everyone hates you now",
    "Why don't you just disappear from this college?",
    "You're the reason our project failed, you're useless",
    "I will make your life miserable in this college",
    "You are worthless and everyone knows it",
    "Stop pretending, you're actually a very bad person",
    "I'll spread your photos online, watch what happens",
    "You deserve to fail, you're completely incompetent",
    "Nobody invited you to the group, get lost",
    "Your accent is so funny, go back to where you came from",
    "I hate you and I'll make sure everyone else hates you too",
]

SAFE_MESSAGES = [
    "Hey, did you understand the assignment from today's class?",
    "Can someone share the notes from the lecture?",
    "Let's meet at the library to study together",
    "Great job on the presentation today!",
    "I found some useful resources for our project",
    "Can you help me with the math problem from homework?",
    "The exam schedule has been updated, check the portal",
    "Thanks for sharing the study material, it's really helpful",
    "Let's form a study group for the upcoming exam",
    "I have a doubt about the lab experiment, can anyone help?",
    "The professor extended the deadline, we have more time",
    "Good luck everyone for tomorrow's exam!",
    "I enjoyed the seminar today, it was very informative",
    "Can we schedule a meeting to discuss the project?",
    "The college fest was amazing, great work by everyone",
    "I'm looking for internship opportunities, any suggestions?",
    "The new timetable looks good, no more conflicts",
    "Let's collaborate on the research paper together",
    "I found a great coding tutorial that helped me a lot",
    "Congratulations on your selection for the competition!",
]

MODERATE_MESSAGES = [
    "I don't agree with your opinion, but that's just my view",
    "You need to work harder if you want to pass",
    "That's not a good idea, you should reconsider",
    "You're wasting your time with this project",
    "I think you made a mistake in your calculation",
    "This is not the right approach for this problem",
    "You should focus on your studies instead of games",
    "That comment was inappropriate, please be careful",
    "I'm not impressed with your performance this semester",
    "You need to improve your communication skills",
]


def generate_messages():
    messages = []
    platforms = ['WhatsApp Group', 'College Portal', 'Discussion Forum', 'Email', 'Social Media']
    contexts = ['class_discussion', 'project_chat', 'exam_group', 'general_forum', 'event_planning']

    for i in range(1, 501):
        msg_type = random.choices(['bullying', 'safe', 'moderate'], weights=[30, 55, 15])[0]
        if msg_type == 'bullying':
            text = random.choice(BULLYING_MESSAGES)
        elif msg_type == 'safe':
            text = random.choice(SAFE_MESSAGES)
        else:
            text = random.choice(MODERATE_MESSAGES)

        messages.append({
            'message_id': f'MSG{i:04d}',
            'sender_id': f'USR{random.randint(1, 120):04d}',
            'platform': random.choice(platforms),
            'context': random.choice(contexts),
            'text': text,
            'category': msg_type,
            'timestamp': (datetime(2025, 1, 1) + timedelta(
                days=random.randint(0, 60),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )).strftime('%Y-%m-%d %H:%M:%S'),
            'length': len(text),
            'word_count': len(text.split())
        })
    return messages


# ==================== INCIDENTS ====================
def generate_incidents(messages, users):
    incidents = []
    categories = ['verbal_abuse', 'threats', 'social_exclusion', 'mockery', 'intimidation', 'cyberstalking']
    severity_levels = ['low', 'medium', 'high', 'critical']

    bullying_msgs = [m for m in messages if m['category'] == 'bullying']
    for i, msg in enumerate(bullying_msgs):
        victim_id = f'USR{random.randint(1, 120):04d}'
        while victim_id == msg['sender_id']:
            victim_id = f'USR{random.randint(1, 120):04d}'

        sender_user = next((u for u in users if u['user_id'] == msg['sender_id']), None)
        severity = random.choices(severity_levels, weights=[15, 35, 35, 15])[0]
        status = random.choices(['open', 'under_review', 'resolved', 'escalated'],
                                weights=[20, 30, 35, 15])[0]

        incidents.append({
            'incident_id': f'INC{i:04d}',
            'message_id': msg['message_id'],
            'reporter_id': f'USR{random.randint(1, 120):04d}',
            'victim_id': victim_id,
            'accused_id': msg['sender_id'],
            'category': random.choice(categories),
            'severity': severity,
            'status': status,
            'platform': msg['platform'],
            'reported_date': (datetime.strptime(msg['timestamp'], '%Y-%m-%d %H:%M:%S') +
                              timedelta(hours=random.randint(1, 48))).strftime('%Y-%m-%d %H:%M:%S'),
            'resolved_date': (datetime.strptime(msg['timestamp'], '%Y-%m-%d %H:%M:%S') +
                              timedelta(days=random.randint(2, 30))).strftime('%Y-%m-%d') if status == 'resolved' else None,
            'resolution': random.choice([
                'warning_issued', 'counseling_session', 'disciplinary_action',
                'content_removed', 'mediation_conducted', 'no_action_required'
            ]) if status == 'resolved' else None,
            'evidence_preserved': True,
            'confidentiality_maintained': True
        })
    return incidents


# ==================== REPORTS ====================
def generate_reports(incidents, messages):
    reports = []
    report_types = ['daily_summary', 'weekly_analysis', 'monthly_trend', 'incident_detail']

    for i in range(1, 51):
        reports.append({
            'report_id': f'RPT{i:03d}',
            'report_type': random.choice(report_types),
            'generated_date': (datetime(2025, 1, 1) + timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d'),
            'total_incidents': random.randint(1, 20),
            'resolved_incidents': random.randint(0, 15),
            'pending_incidents': random.randint(0, 10),
            'escalated_incidents': random.randint(0, 5),
            'department': random.choice(['CSE', 'ECE', 'EEE', 'ME', 'CE', 'IT', 'All']),
            'severity_distribution': {
                'critical': random.randint(0, 5),
                'high': random.randint(2, 10),
                'medium': random.randint(5, 15),
                'low': random.randint(3, 8)
            },
            'trend': random.choice(['increasing', 'decreasing', 'stable'])
        })
    return reports


# ==================== DAILY STATISTICS ====================
def generate_daily_statistics(messages):
    stats = []
    base_date = datetime(2025, 1, 1)

    for day in range(60):
        date = (base_date + timedelta(days=day)).strftime('%Y-%m-%d')
        day_messages = [m for m in messages if m['timestamp'].startswith(date)]

        stats.append({
            'date': date,
            'total_messages': len(day_messages) + random.randint(150, 300),
            'messages_analyzed': len(day_messages) + random.randint(150, 300),
            'bullying_detected': random.randint(8, 25),
            'safe_messages': random.randint(130, 280),
            'moderate_messages': random.randint(5, 15),
            'detection_rate': round(random.uniform(0.85, 0.98), 2),
            'false_positive_rate': round(random.uniform(0.02, 0.08), 2),
            'moderation_time_avg_min': round(random.uniform(3, 15), 1)
        })
    return stats


# ==================== PREDICTIVE ANALYTICS ====================
def generate_predictive_analytics():
    models = {
        'model_name': 'BERT-based Cyberbullying Classifier',
        'architecture': 'Bidirectional Encoder Representations from Transformers',
        'dataset_size': 50000,
        'training_split': 0.8,
        'validation_split': 0.1,
        'test_split': 0.1,
        'metrics': {
            'accuracy': 0.9247,
            'precision': 0.9156,
            'recall': 0.8934,
            'f1_score': 0.9043,
            'auc_roc': 0.9512
        },
        'confusion_matrix': {
            'true_positive': 1247,
            'false_positive': 118,
            'true_negative': 1156,
            'false_negative': 149
        },
        'classes': ['cyberbullying', 'non_cyberbullying'],
        'training_epochs': 25,
        'learning_rate': 0.00003,
        'batch_size': 32,
        'loss_function': 'Binary Cross Entropy',
        'optimizer': 'Adam',
        'preprocessing': [
            'Text tokenization and cleaning',
            'Stop word removal',
            'Sentiment analysis integration',
            'Context-aware classification',
            'Multi-language support',
            'Real-time inference pipeline'
        ],
        'feature_importance': {
            'toxicity_words': 0.35,
            'sentiment_score': 0.25,
            'context_analysis': 0.20,
            'user_history': 0.12,
            'message_length': 0.05,
            'platform_type': 0.03
        }
    }
    return models


# ==================== MAIN ====================
if __name__ == '__main__':
    print("Generating data for Cyberbullying Detection Platform...")

    users = generate_users()
    messages = generate_messages()
    incidents = generate_incidents(messages, users)
    reports = generate_reports(incidents, messages)
    daily_stats = generate_daily_statistics(messages)
    analytics = generate_predictive_analytics()

    data = {
        'users': users,
        'messages': messages,
        'incidents': incidents,
        'reports': reports,
        'daily_statistics': daily_stats,
        'predictive_analytics': analytics
    }

    with open(f'{OUTPUT_DIR}/cyberbullying_data.json', 'w') as f:
        json.dump(data, f, indent=2, default=str)

    print(f"Users: {len(users)}")
    print(f"Messages: {len(messages)}")
    print(f"Incidents: {len(incidents)}")
    print(f"Reports: {len(reports)}")
    print(f"Daily Stats: {len(daily_stats)} days")
    print(f"Model Accuracy: {analytics['metrics']['accuracy']}")
    print("Data saved successfully!")
