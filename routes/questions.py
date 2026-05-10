import logging
from flask import Blueprint, jsonify, request
from data.questions import (
    get_questions_by_grade,
    get_questions_by_topic,
    get_questions_by_complexity,
    get_all_topics,
    QUESTION_BANK
)

logger = logging.getLogger(__name__)

questions_bp = Blueprint('questions', __name__)

VALID_GRADES = [9, 10, 11, 12]
VALID_COMPLEXITY = ['easy', 'medium', 'hard']


@questions_bp.route('/questions/grade/<int:grade>/top/<int:n>', methods=['GET'])
def get_top_questions_by_grade(grade, n):
    """Get top N questions for a specific grade level."""
    logger.info("Fetching top %d questions for grade %d", n, grade)

    if grade not in VALID_GRADES:
        return jsonify({'error': f'Invalid grade. Must be one of {VALID_GRADES}'}), 400
    if n <= 0 or n > 100:
        return jsonify({'error': 'n must be between 1 and 100'}), 400

    questions = get_questions_by_grade(grade, n)
    return jsonify({
        'grade': grade,
        'requested': n,
        'returned': len(questions),
        'questions': [q.to_dict() for q in questions]
    })


@questions_bp.route('/questions/topic/<string:topic>/count/<int:n>', methods=['GET'])
def get_questions_by_topic_route(topic, n):
    """Get N questions for a selected topic."""
    logger.info("Fetching %d questions for topic: %s", n, topic)

    if n <= 0 or n > 100:
        return jsonify({'error': 'n must be between 1 and 100'}), 400

    questions = get_questions_by_topic(topic, n)
    return jsonify({
        'topic': topic,
        'requested': n,
        'returned': len(questions),
        'questions': [q.to_dict() for q in questions]
    })


@questions_bp.route('/questions/complexity/<string:complexity>/count/<int:n>', methods=['GET'])
def get_questions_by_complexity_route(complexity, n):
    """Get N questions filtered by complexity level."""
    logger.info("Fetching %d questions with complexity: %s", n, complexity)

    if complexity.lower() not in VALID_COMPLEXITY:
        return jsonify({'error': f'Invalid complexity. Must be one of {VALID_COMPLEXITY}'}), 400
    if n <= 0 or n > 100:
        return jsonify({'error': 'n must be between 1 and 100'}), 400

    questions = get_questions_by_complexity(complexity, n)
    return jsonify({
        'complexity': complexity,
        'requested': n,
        'returned': len(questions),
        'questions': [q.to_dict() for q in questions]
    })


@questions_bp.route('/questions/grade/<int:grade>/topic/<string:topic>/count/<int:n>', methods=['GET'])
def get_questions_by_grade_and_topic(grade, topic, n):
    """Get N questions filtered by both grade and topic."""
    if grade not in VALID_GRADES:
        return jsonify({'error': f'Invalid grade. Must be one of {VALID_GRADES}'}), 400

    questions = [q for q in QUESTION_BANK
                 if q.grade == grade and q.topic.lower() == topic.lower()][:n]
    return jsonify({
        'grade': grade,
        'topic': topic,
        'returned': len(questions),
        'questions': [q.to_dict() for q in questions]
    })


@questions_bp.route('/topics', methods=['GET'])
def get_topics():
    """Get all available maths topics."""
    return jsonify({'topics': sorted(get_all_topics())})


@questions_bp.route('/stats', methods=['GET'])
def get_stats():
    """Return stats about the question bank."""
    from collections import Counter
    grade_counts = Counter(q.grade for q in QUESTION_BANK)
    topic_counts = Counter(q.topic for q in QUESTION_BANK)
    complexity_counts = Counter(q.complexity for q in QUESTION_BANK)

    return jsonify({
        'total_questions': len(QUESTION_BANK),
        'by_grade': dict(grade_counts),
        'by_topic': dict(topic_counts),
        'by_complexity': dict(complexity_counts)
    })
