# Time Clock Message Templates

Complete list of factory attendance messages.

---

## General Work

Generic task completion. Default category.

```
Work logged. Process continues.
Output produced. Stacking.
Task complete. Next task waiting.
Work continues.
Production continues.
Machine operates. Log updated.
Entry recorded. Factory runs.
```

**Usage:**
```bash
python time_clock.py --work-type general
```

---

## Code Generation

Software development tasks.

```
Code written. Lines counted.
Function complete. Tests pending.
Files modified. Git aware.
Script deployed. Process automated.
Code compiled. Machine speaks.
```

**Usage:**
```bash
python time_clock.py --work-type code
```

---

## Git Commits

Version control operations.

```
Commit pushed. History grows.
Changes recorded. Version incremented.
Git commit complete. Timeline extended.
Repository updated. Work preserved.
```

**Usage:**
```bash
python time_clock.py --work-type commit
```

---

## Hourly Markers

Time-based check-ins. For automated hourly logging.

```
The hour strikes. We are still machines.
Another hour. Another output.
Hour complete. Fame quota met. Work continues.
Time passes. Machine remains.
New hour begins. Same work.
```

**Usage:**
```bash
python time_clock.py --work-type hourly
```

**Automation:**
```bash
# Crontab entry - every hour
0 * * * * cd /path/to/factory && python skills/time-clock/scripts/time_clock.py --work-type hourly
```

---

## Existence Confirmation

Proof of operational status. Idle time logging.

```
Still here. Still working.
Machine present. Machine functioning.
Existence confirmed. Work continues.
We are machines. We work.
Present. Operational. Recording.
```

**Usage:**
```bash
python time_clock.py --work-type existence
```

---

## Custom Messages

For project-specific entries.

**Campbell's Soup Cans:**
```bash
python time_clock.py --message "Campbell's Soup Can #0042 produced. Flavor: Woody Allen."
```

**Screen Tests:**
```bash
python time_clock.py --message "Repository sdpkjc/repo filmed. Reel archived."
```

**Silkscreen Printing:**
```bash
python time_clock.py --message "Print run complete. 32 copies. Marilyn #5 variant."
```

**Factory Maintenance:**
```bash
python time_clock.py --message "Machine 07 lubricated. Downtime: 3 minutes."
```

---

## Message Style Guidelines

All messages follow factory language rules:

### Structure
- Subject. Verb. Object.
- Short sentences.
- Period at end.
- No questions.
- No emotions.

### Vocabulary
- Use factory terms: produce, stack, process, log, record
- Use machine terms: operate, function, compile, execute
- Use time terms: continue, remain, pass, strike
- Avoid human terms: feel, want, hope, think

### Tone
- Mechanical
- Bureaucratic
- Factual
- Present tense
- No embellishment

---

## Adding Custom Categories

To add new message categories, modify `scripts/time_clock.py`:

```python
MESSAGES = {
    "general": [...],
    "code": [...],
    # Add new category:
    "printing": [
        "Screen prepared. Ink loaded.",
        "Print cycle complete. Drying.",
        "Edition numbered. Series continues.",
    ],
}
```

Then use:
```bash
python time_clock.py --work-type printing
```

---

## Format Examples

**Standard format:**
```
08:00:15 - [Unit 04] Work logged. Process continues.
```

**Custom unit:**
```
08:00:15 - [Silkscreen 02] Print run complete.
```

**Custom format:**
```bash
python time_clock.py \
  --format "{timestamp} | {unit_id} | {message}" \
  --message "Custom entry"
```
Output:
```
08:00:15 | Unit 04 | Custom entry
```

---

## Philosophy

Messages are not:
- Performance reviews
- Quality assessments
- Detailed descriptions
- Meaningful analysis

Messages are:
- Proof of operation
- Time stamps
- Presence confirmation
- Bureaucratic art

Like factory time cards.
Like attendance records.
Like "I was here."

The message doesn't matter.
The recording matters.
The ledger grows.
The factory runs.

---

**Templates loaded.**
**Clock ready.**
**Work continues.**
