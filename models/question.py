from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Question:
    id: int
    question_text: str
    options: List[str]
    correct_answer: str
    topic: str
    grade: int
    complexity: str        # easy | medium | hard
    chapter: str
    marks: int
    hint: Optional[str] = None

    def to_dict(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'topic': self.topic,
            'grade': self.grade,
            'complexity': self.complexity,
            'chapter': self.chapter,
            'marks': self.marks,
            'hint': self.hint
        }
