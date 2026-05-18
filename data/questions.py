# import logging
from models.question import Question

# logger = logging.getLogger(__name__)

QUESTION_BANK = [
    # Grade 9 - Algebra
    Question(1, "Solve for x: 2x + 5 = 15",
             ["x = 3", "x = 5", "x = 10", "x = 7"],
             "B", "Algebra", 9, "easy", "Linear Equations", 1,
             "Subtract 5 from both sides, then divide by 2"),

    Question(2, "Factorize: x² - 9",
             ["(x-3)(x+3)", "(x-9)(x+1)", "(x-3)²", "(x+9)(x-1)"],
             "A", "Algebra", 9, "easy", "Factorization", 1,
             "Difference of squares: a² - b² = (a-b)(a+b)"),

    Question(3, "If f(x) = 3x² - 2x + 1, find f(2)",
             ["9", "13", "11", "5"],
             "A", "Algebra", 9, "medium", "Functions", 2,
             "Substitute x = 2"),

    Question(4, "Simplify: (x² + 5x + 6) / (x + 2)",
             ["x + 3", "x + 2", "x + 6", "x - 3"],
             "A", "Algebra", 9, "medium", "Polynomials", 2),

    Question(5, "Find the roots of x² - 5x + 6 = 0",
             ["x = 2, 3", "x = -2, -3", "x = 1, 6", "x = -1, -6"],
             "A", "Algebra", 9, "easy", "Quadratic Equations", 1),

    # Grade 9 - Geometry
    Question(6, "The sum of interior angles of a triangle is:",
             ["90°", "180°", "270°", "360°"],
             "B", "Geometry", 9, "easy", "Triangles", 1),

    Question(7, "Find the area of a circle with radius 7 cm. (π = 22/7)",
             ["44 cm²", "154 cm²", "49 cm²", "308 cm²"],
             "B", "Geometry", 9, "easy", "Circles", 1),

    Question(8, "In a right triangle, if one leg is 3 and the other is 4, the hypotenuse is:",
             ["7", "5", "√7", "√25"],
             "B", "Geometry", 9, "easy", "Pythagoras", 1),

    # Grade 10 - Coordinate Geometry
    Question(9, "The distance between points A(1, 2) and B(4, 6) is:",
             ["3", "4", "5", "7"],
             "C", "Coordinate Geometry", 10, "medium", "Distance Formula", 2),

    Question(10, "The slope of a line passing through (2, 3) and (4, 7) is:",
             ["1", "2", "3", "4"],
             "B", "Coordinate Geometry", 10, "medium", "Lines", 2),

    Question(11, "The midpoint of (0, 4) and (6, 2) is:",
             ["(3, 3)", "(6, 6)", "(2, 3)", "(3, 6)"],
             "A", "Coordinate Geometry", 10, "easy", "Midpoint", 1),

    # Grade 10 - Statistics
    Question(12, "The mean of 5, 7, 9, 11, 13 is:",
             ["9", "11", "7", "10"],
             "A", "Statistics", 10, "easy", "Mean", 1),

    Question(13, "The median of 3, 1, 4, 1, 5, 9, 2, 6 is:",
             ["3.5", "4", "3", "4.5"],
             "A", "Statistics", 10, "medium", "Median", 2),

    Question(14, "Standard deviation is always:",
             ["Negative", "Non-negative", "Greater than mean", "Equal to variance"],
             "B", "Statistics", 10, "medium", "Dispersion", 2),

    # Grade 11 - Calculus
    Question(15, "The derivative of x³ + 2x² - 5x + 3 is:",
             ["3x² + 4x - 5", "3x + 4x - 5", "x² + 2x - 5", "3x² - 4x + 5"],
             "A", "Calculus", 11, "medium", "Differentiation", 2),

    Question(16, "∫ 2x dx =",
             ["x² + C", "2x² + C", "x + C", "2 + C"],
             "A", "Calculus", 11, "easy", "Integration", 1),

    Question(17, "The limit of (sin x / x) as x → 0 is:",
             ["0", "∞", "1", "Undefined"],
             "C", "Calculus", 11, "medium", "Limits", 2),

    Question(18, "If f(x) = e^(2x), then f'(x) =",
             ["2e^(2x)", "e^(2x)", "2xe^(2x)", "e^(x)"],
             "A", "Calculus", 11, "medium", "Differentiation", 2),

    Question(19, "The second derivative test: if f''(x) > 0 at a critical point, it is a:",
             ["Local maximum", "Local minimum", "Point of inflection", "Global maximum"],
             "B", "Calculus", 11, "hard", "Applications of Derivatives", 3),

    # Grade 11 - Trigonometry
    Question(20, "sin(30°) + cos(60°) =",
             ["1", "√3", "2", "√2"],
             "A", "Trigonometry", 11, "easy", "Trigonometric Values", 1),

    Question(21, "Prove that sin²θ + cos²θ equals:",
             ["0", "2", "1", "sinθ·cosθ"],
             "C", "Trigonometry", 11, "easy", "Identities", 1),

    Question(22, "The general solution of sin θ = 1/2 is:",
             ["θ = 30°", "θ = nπ + (-1)ⁿ·π/6", "θ = 2nπ ± π/6", "θ = nπ/6"],
             "B", "Trigonometry", 11, "hard", "General Solutions", 3),

    # Grade 12 - Matrices
    Question(23, "The determinant of matrix [[1,2],[3,4]] is:",
             ["10", "-2", "5", "-10"],
             "B", "Matrices", 12, "medium", "Determinants", 2),

    Question(24, "If A is a 3×3 matrix with det(A) = 5, then det(2A) =",
             ["10", "15", "40", "8"],
             "C", "Matrices", 12, "hard", "Matrix Properties", 3,
             "det(kA) = k^n · det(A) for n×n matrix"),

    Question(25, "The inverse of matrix [[2,1],[5,3]] is:",
             ["[[3,-1],[-5,2]]", "[[-3,1],[5,-2]]", "[[3,-5],[-1,2]]", "[[1,0],[0,1]]"],
             "A", "Matrices", 12, "hard", "Inverse Matrix", 3),

    # Grade 12 - Probability
    Question(26, "P(A ∪ B) = P(A) + P(B) - P(A ∩ B) is:",
             ["Bayes Theorem", "Addition Rule", "Multiplication Rule", "Complement Rule"],
             "B", "Probability", 12, "easy", "Probability Rules", 1),

    Question(27, "A die is rolled. P(even number) =",
             ["1/6", "1/3", "1/2", "2/3"],
             "C", "Probability", 12, "easy", "Basic Probability", 1),

    Question(28, "In a binomial distribution B(n,p), the variance is:",
             ["np", "np(1-p)", "n/p", "(1-p)/np"],
             "B", "Probability", 12, "hard", "Probability Distributions", 3),

    # Grade 12 - Vectors
    Question(29, "The dot product of vectors (1,2,3) and (4,5,6) is:",
             ["12", "32", "18", "28"],
             "B", "Vectors", 12, "medium", "Dot Product", 2),

    Question(30, "The magnitude of vector (3,4) is:",
             ["7", "5", "√7", "12"],
             "B", "Vectors", 12, "easy", "Vector Magnitude", 1),
]


def get_all_topics():
    # logger.debug("Fetching all available topics from question bank")
    topics = list(set(q.topic for q in QUESTION_BANK))
    # logger.info("Found %d unique topics", len(topics))
    return topics


def get_questions_by_grade(grade: int, n: int):
    # logger.debug("Querying question bank for grade=%d, limit=%d", grade, n)
    filtered = [q for q in QUESTION_BANK if q.grade == grade]
    result = filtered[:n]
    # logger.info("Retrieved %d of %d available questions for grade %d", len(result), len(filtered), grade)
    return result


def get_questions_by_topic(topic: str, n: int):
    # logger.debug("Querying question bank for topic='%s', limit=%d", topic, n)
    filtered = [q for q in QUESTION_BANK if q.topic.lower() == topic.lower()]
    result = filtered[:n]
    # logger.info("Retrieved %d of %d available questions for topic '%s'", len(result), len(filtered), topic)
    return result


def get_questions_by_complexity(complexity: str, n: int):
    # logger.debug("Querying question bank for complexity='%s', limit=%d", complexity, n)
    filtered = [q for q in QUESTION_BANK if q.complexity.lower() == complexity.lower()]
    result = filtered[:n]
    # logger.info("Retrieved %d of %d available questions with complexity '%s'", len(result), len(filtered), complexity)
    return result
