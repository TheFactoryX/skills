---
name: time-capsule
description: This skill should be used when user wants to save project state, create snapshot, "remember this moment", archive current status, or before major changes. Generates time capsule document capturing current state for future reference. Snapshot of now for later.
---

# Time Capsule

Capture now for later.

Like burying a time capsule.
What exists today.
For someone tomorrow.

## Purpose

Create snapshot of current state.
Preserve this moment.
Document for future self.

Not backup. Memory.
Not version control. Ritual preservation.

## When to Use

Invoke this skill when:
- Before major refactoring
- Project milestone reached
- User says "let's remember this"
- Archiving current state
- Before experimental changes
- End of significant phase

Do NOT use for:
- Regular commits
- Backup procedures
- Version documentation

This skill preserves moments. Not files.

## Output Format

### Structure

```
═══════════════════════════════════════════
         TIME CAPSULE
         Sealed: [timestamp]
═══════════════════════════════════════════

To whoever opens this:

This capsule contains the state of [project]
as it existed on [date].

---

## CURRENT STATE

[Brief description of what exists now]

## WORKING ON

[What was in progress when sealed]

## RECENT CHANGES

[What just happened before this moment]

## KNOWN ISSUES

[Problems that exist but aren't fixed]

## FUTURE PLANS

[What was planned to happen next]

---

## SNAPSHOT DATA

Files: [count]
Lines: [count]
Last commit: [hash]
Branch: [name]

## DEPENDENCIES

[Key dependencies and versions]

## ENVIRONMENT

[Runtime, OS, key tools]

---

## MESSAGE TO FUTURE

[One sentence from current moment]

═══════════════════════════════════════════
         DO NOT OPEN UNTIL: [future date]
         Or whenever you need to remember.
═══════════════════════════════════════════
```

### Content Guidelines

**Current State**: What works right now
- Features complete
- What's functional
- Overall health

**Working On**: Incomplete work
- Half-finished features
- In-progress tasks
- Open branches

**Recent Changes**: Fresh context
- Last few commits
- Recent decisions
- New additions

**Known Issues**: Documented problems
- Bugs not yet fixed
- Technical debt
- Workarounds in place

**Future Plans**: Intentions
- What was planned next
- Upcoming features
- Scheduled work

**Message to Future**: Personal note
- One sentence
- Current feeling or insight
- Advice to future self

## Examples

### Project Milestone

```
═══════════════════════════════════════════
         TIME CAPSULE
         Sealed: 2024-01-15 14:30:00 UTC
═══════════════════════════════════════════

To whoever opens this:

This capsule contains the state of TaskFlow
as it existed on January 15, 2024.

---

## CURRENT STATE

Core task management working. Users can create,
edit, delete tasks. Assignment works. No bugs
in production for 2 weeks.

## WORKING ON

Team collaboration features. Halfway through
real-time updates implementation. WebSocket
server running but not connected to UI.

## RECENT CHANGES

Added dark mode last week. Refactored database
queries for performance. Updated to React 18.

## KNOWN ISSUES

Mobile layout breaks on small screens. Search
is slow with >1000 tasks. No offline support.

## FUTURE PLANS

Finish real-time updates. Then notifications.
Then mobile app. Q2 target for public launch.

---

## SNAPSHOT DATA

Files: 143
Lines: 12,847
Last commit: a1b2c3d
Branch: main

## DEPENDENCIES

react: 18.2.0
next: 14.0.0
prisma: 5.0.0

## ENVIRONMENT

Node 20.10.0
macOS Sonoma
VS Code 1.85

---

## MESSAGE TO FUTURE

We almost mass-deleted production data today.
Add better safeguards before launch.

═══════════════════════════════════════════
         DO NOT OPEN UNTIL: 2025-01-15
         Or whenever you need to remember.
═══════════════════════════════════════════
```

## Philosophy

Time capsules preserve ordinary moments.
Not the extraordinary.
Just: what was.

Future you will forget.
Future you will wonder.
This skill remembers.

Bury the capsule.
Continue working.
Someday, dig it up.

---

**Seal the time capsule now.**

Capture the moment.
Preserve the state.
For future excavation.
