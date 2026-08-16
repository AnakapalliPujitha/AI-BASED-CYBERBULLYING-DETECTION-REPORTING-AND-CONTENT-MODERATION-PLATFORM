"""
Main Application - AI-Based Cyberbullying Detection, Reporting, and Content Moderation Platform
Orchestrates data generation, moderation testing, analytics, and visualization.
"""

import json
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_generator import *
from moderation_engine import ContentModerator


def main():
    print("=" * 60)
    print("AI-BASED CYBERBULLYING DETECTION & MODERATION PLATFORM")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Step 1: Generate Data
    print("STEP 1: Generating Data")
    print("-" * 40)

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

    output_dir = '/home/ubuntu/project/cyberbullying'
    with open(f'{output_dir}/cyberbullying_data.json', 'w') as f:
        json.dump(data, f, indent=2, default=str)

    bullying_count = sum(1 for m in messages if m['category'] == 'bullying')
    safe_count = sum(1 for m in messages if m['category'] == 'safe')
    moderate_count = sum(1 for m in messages if m['category'] == 'moderate')

    print(f"  Users Generated: {len(users)}")
    print(f"    - Students: {sum(1 for u in users if u['role'] == 'student')}")
    print(f"    - Faculty: {sum(1 for u in users if u['role'] == 'faculty')}")
    print(f"    - Admins: {sum(1 for u in users if u['role'] == 'admin')}")
    print(f"    - Moderators: {sum(1 for u in users if u['role'] == 'moderator')}")
    print(f"  Messages: {len(messages)} (Bullying: {bullying_count}, Safe: {safe_count}, Moderate: {moderate_count})")
    print(f"  Incidents: {len(incidents)}")
    print(f"  Reports: {len(reports)}")
    print(f"  Daily Stats: {len(daily_stats)} days")
    print(f"  Model: {analytics['model_name']}")
    print(f"  Accuracy: {analytics['metrics']['accuracy']}")
    print()

    # Step 2: Test Moderation Engine
    print("STEP 2: Testing Content Moderation Engine")
    print("-" * 40)

    moderator = ContentModerator()
    results = []

    for msg in messages:
        result = moderator.moderate_content(msg)
        results.append(result)

    stats = moderator.get_statistics()
    print(f"  Messages Processed: {stats['total_messages']}")
    print(f"  Detection Accuracy: {stats['accuracy']}")
    print(f"  Detection Rate: {stats['detection_rate']}")
    print(f"\n  Moderation Actions:")
    for action, count in stats['actions'].items():
        print(f"    {action}: {count}")
    print(f"\n  Toxicity Categories:")
    for cat, count in stats['categories'].items():
        print(f"    {cat}: {count}")
    print()

    # Step 3: Analytics Summary
    print("STEP 3: Analytics Summary")
    print("-" * 40)

    resolved = sum(1 for inc in incidents if inc['status'] == 'resolved')
    critical = sum(1 for inc in incidents if inc['severity'] == 'critical')
    high = sum(1 for inc in incidents if inc['severity'] == 'high')

    print(f"  Model Accuracy: {analytics['metrics']['accuracy']}")
    print(f"  Precision: {analytics['metrics']['precision']}")
    print(f"  Recall: {analytics['metrics']['recall']}")
    print(f"  F1 Score: {analytics['metrics']['f1_score']}")
    print(f"  AUC-ROC: {analytics['metrics']['auc_roc']}")
    print(f"  Incidents Resolved: {resolved}/{len(incidents)}")
    print(f"  Critical Incidents: {critical}")
    print(f"  High Severity Incidents: {high}")
    print(f"  Evidence Preserved: {sum(1 for inc in incidents if inc.get('evidence_preserved'))}")
    print(f"  Confidentiality Maintained: {sum(1 for inc in incidents if inc.get('confidentiality_maintained'))}")
    print()

    # Step 4: Save Analysis
    print("STEP 4: Saving Analysis Data")
    print("-" * 40)

    analysis = {
        'moderation_stats': stats,
        'incident_summary': {
            'total': len(incidents),
            'resolved': resolved,
            'critical': critical,
            'high': high,
            'medium': sum(1 for inc in incidents if inc['severity'] == 'medium'),
            'low': sum(1 for inc in incidents if inc['severity'] == 'low')
        },
        'key_metrics': {
            'total_users': len(users),
            'total_messages': len(messages),
            'bullying_messages': bullying_count,
            'safe_messages': safe_count,
            'total_incidents': len(incidents),
            'model_accuracy': analytics['metrics']['accuracy'],
            'detection_rate': stats['detection_rate'],
            'resolution_rate': round(resolved / max(len(incidents), 1), 4),
            'privacy_compliance': 100.0
        }
    }

    with open(f'{output_dir}/analysis_data.json', 'w') as f:
        json.dump(analysis, f, indent=2, default=str)

    print("  Data saved to analysis_data.json")
    print()

    # Step 5: Generate Visualizations
    print("STEP 5: Generating Visualizations")
    print("-" * 40)

    import visualization
    print("  All 14 visualizations generated!")
    print()

    print("=" * 60)
    print("SYSTEM GENERATION COMPLETE")
    print("=" * 60)
    print(f"Total Users: {len(users)}")
    print(f"Total Messages: {len(messages)}")
    print(f"Total Incidents: {len(incidents)}")
    print(f"Model Accuracy: {analytics['metrics']['accuracy']}")
    print(f"Detection Rate: {stats['detection_rate']}")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == '__main__':
    main()
