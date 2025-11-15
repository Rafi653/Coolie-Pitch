# Job Applications Tracker

Track your ongoing job applications, interview stages, and feedback.

## Structure
Store application data either as:
- JSON/YAML files (one per company)
- Database entries (via the web app)

## Information to Track
- Company name
- Role/Position
- Application date
- Current stage (Applied, Phone Screen, Technical, Onsite, Offer, Rejected)
- Contact person
- Interview dates
- Feedback notes
- Preparation notes
- Follow-up actions

## Example Entry
```yaml
company: Google
role: Senior Data Engineer
applied_date: 2024-01-15
current_stage: Technical Interview
stages:
  - date: 2024-01-15
    stage: Applied
  - date: 2024-01-22
    stage: Phone Screen
    feedback: "Went well, discussed experience with Spark"
  - date: 2024-02-05
    stage: Technical Interview
    notes: "Coding round scheduled"
next_steps:
  - "Review distributed systems"
  - "Practice SQL optimization"
```
