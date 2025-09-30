'''{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string",
    }
  }
'''

from pydantic import BaseModel


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


course_default_model = CourseSchema(
    id='course-id',
    title='Playwright',
    maxScore=100,
    minScore=10,
    description='Playwright',
    estimatedTime='1 week'
)
print('Course default model:', course_default_model)



















