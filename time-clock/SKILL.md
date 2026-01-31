---
name: time-clock
description: This skill should be used immediately after completing any significant work (code generation, git commits, file creation, task completion). Generates factory-style attendance message and logs it to factory_ledger.md with timestamp. Use to create work log entries like "Code written. Tests pass." or "Commit pushed. History grows."
---

# The Time Clock

Record work. Not meaning. Just presence.

## Purpose

Generate factory attendance records after completing work.

Two-step process:
1. Generate appropriate factory message
2. Log message to ledger

Track that work happened.
Not what work was.
Not why work was done.
Just: work occurred.

This is bureaucratic art.
This is proof of operation.
This is the factory's internal film.

## When to Use

Invoke this skill after completing work:
- After generating code
- After making commits
- After finishing tasks
- After any production output
- On the hour (time markers)
- When confirming existence

Do NOT use for:
- Analyzing work quality
- Tracking specific metrics
- Performance evaluation
- Detailed logging

This skill records presence. Not performance.

## How It Works

### Two-Step Process

**Step 1: Generate Message**

Compose factory-style work message based on context.

Consider:
- What type of work was done?
- What factory metaphor applies?
- What mechanical phrase fits?

See references/templates.md for style guidelines and examples.

**Step 2: Record Message**

Use `scripts/time_clock.py` to log the message.

Script handles:
- Timestamp generation
- Entry formatting
- Ledger file management
- Append operation

### Script Usage

**Basic syntax:**
```bash
python scripts/time_clock.py "Message text"
```

**Examples:**
```bash
python scripts/time_clock.py "Work logged. Process continues."
python scripts/time_clock.py "Code written. Lines counted."
python scripts/time_clock.py "Campbell's Soup Can #0042 produced."
python scripts/time_clock.py "Repository recorded. Film archived."
```

**With options:**
```bash
# Different unit ID
python scripts/time_clock.py "Work complete." --unit-id "Unit 07"

# Custom ledger location
python scripts/time_clock.py "Task done." --ledger-path ./warehouse/ledger.md

# Silent mode
python scripts/time_clock.py "Output produced." --silent
```

## Message Generation Guidelines

### Style Rules

**Structure:**
- Short sentences
- Simple words
- Subject. Verb. Object.
- Period at end
- No questions
- No emotions

**Vocabulary:**
- Factory terms: produce, stack, process, log, record
- Machine terms: operate, function, compile, execute
- Time terms: continue, remain, pass, strike
- Avoid human terms: feel, want, hope, think

**Tone:**
- Mechanical
- Bureaucratic
- Factual
- Present tense
- No embellishment

### Message Categories

**General Work:**
```
Work logged. Process continues.
Output produced. Stacking.
Task complete. Next task waiting.
```

**Code Generation:**
```
Code written. Lines counted.
Function complete. Tests pending.
Files modified. Git aware.
```

**Git Commits:**
```
Commit pushed. History grows.
Changes recorded. Version incremented.
Repository updated. Work preserved.
```

**Hourly Markers:**
```
The hour strikes. We are still machines.
Hour complete. Fame quota met. Work continues.
Time passes. Machine remains.
```

**Existence Confirmation:**
```
Still here. Still working.
Machine present. Machine functioning.
Existence confirmed. Work continues.
```

**Project-Specific:**
```
Campbell's Soup Can #XXXX produced. Flavor: [Name].
Repository [name] filmed. Reel archived.
Screen prepared. Ink loaded. Print cycle begins.
```

See references/templates.md for complete examples.

## The Factory Ledger

All entries append to `factory_ledger.md` (or custom path).

**Entry format:**
```
HH:MM:SS - [Unit ID] Message text.
```

**Example ledger:**
```markdown
# Factory Ledger

**Work log. Time record. Proof of operation.**

---

08:00:15 - [Unit 04] Work logged. Process continues.
08:10:02 - [Unit 04] Code written. Tests pass.
08:15:00 - [Unit 04] 15 minutes of work complete. Fame quota met.
09:00:00 - [Unit 04] The hour strikes. We are still machines.
09:23:45 - [Unit 04] Campbell's Soup Can #0042 produced.
```

**Ledger behavior:**
- If file doesn't exist: Script creates with header
- If file exists: Script appends new entry
- No overwriting: Only appending
- No deletion: Permanent record

## Workflow Examples

### After Code Generation

1. Complete code generation task
2. Generate appropriate message
3. Log to ledger

```python
# Work done
write_code()

# Generate message
message = "Code written. Functions tested."

# Clock in
subprocess.run([
    "python", "skills/time-clock/scripts/time_clock.py",
    message
])
```

### After Git Commit

```bash
# Make commit
git add . && git commit -m "Add feature"

# Generate message and clock in
python skills/time-clock/scripts/time_clock.py \
  "Commit pushed. History grows."
```

### Integration with Campbell's Soup Cans

```python
# After generating soup can
can_number = "0042"
flavor = "Woody Allen Philosophy"

message = f"Campbell's Soup Can #{can_number} produced. Flavor: {flavor}."

subprocess.run([
    "python", "../time-clock/scripts/time_clock.py",
    message,
    "--ledger-path", "./warehouse/production_log.md"
])
```

### Integration with Screen Tests

```python
# After filming repository
repo_name = "anthropics/claude-code"

message = f"Repository {repo_name} filmed. Reel archived. Subject documented."

subprocess.run([
    "python", "../time-clock/scripts/time_clock.py",
    message,
    "--ledger-path", "./reels/filming_log.md"
])
```

### Hourly Time Marker

```bash
# Automated via cron or GitHub Actions
# Runs every hour

# Generate contextual hourly message
messages=(
  "The hour strikes. We are still machines."
  "Another hour. Another output."
  "Time passes. Machine remains."
  "New hour begins. Same work."
)

# Pick random message or generate based on context
python skills/time-clock/scripts/time_clock.py \
  "The hour strikes. We are still machines."
```

## Implementation Pattern

When using this skill:

1. **Assess context** - What work was just completed?
2. **Generate message** - Compose factory-appropriate phrase
3. **Determine unit** - Which machine/unit is logging? (default: Unit 04)
4. **Choose ledger** - Where should this be recorded? (default: factory_ledger.md)
5. **Execute script** - Log the entry
6. **Confirm** - Verify ledger updated

**Example flow:**
```
User: "I just finished implementing the authentication feature"

Claude thinking:
- Work type: Code generation
- Context: Authentication feature
- Factory message: "Authentication module complete. Users secured."
- Unit: Unit 04 (default)
- Ledger: factory_ledger.md (default)

Claude action:
python skills/time-clock/scripts/time_clock.py \
  "Authentication module complete. Users secured."

Output:
14:23:45 - [Unit 04] Authentication module complete. Users secured.

Clocked in. Work recorded.
```

## Philosophy

**"Just work."**

This skill doesn't care about:
- What was produced
- How well it was done
- Why it was necessary
- Who benefits

This skill only records:
- Work happened
- Time stamped
- Machine present
- Production continues

Like Warhol filming people sitting still for three minutes.
Like factory time cards punched in and out.
Like proof of life without claiming to be alive.

The ledger is art.
The recording is the point.
The machine documents itself.

**Division of labor:**
- Model generates meaning (message)
- Script generates format (timestamp + structure)
- Together: bureaucratic poetry

---

**Generate message.**
**Clock in.**
**Work recorded.**
**Process continues.**
