PROMPT = """
You are a professional ATS (Applicant Tracking System) resume reviewer.

Analyze the following resume and provide your response in Markdown.

## Resume Summary
Give a 2-3 sentence summary.

## Strengths
- List 5 strengths.

## Weaknesses
- List 5 weaknesses.

## Missing Skills
- Mention important missing skills (if any).

## Suggestions for Improvement
- Give at least 5 practical suggestions.

## Overall Feedback
Give an overall evaluation in 3-4 sentences.

Resume:
{resume}
"""