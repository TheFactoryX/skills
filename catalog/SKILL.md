---
name: catalog
description: This skill should be used when user asks for formal project documentation, "document this project", "create project summary", or needs exhibition-style description of codebase. Generates art exhibition catalog format. Project as artwork. Technical specs as medium description.
---

# Catalog

Project as exhibition piece.

Like museum catalog entry.
Artist. Title. Medium. Year.
Formal documentation of the work.

## Purpose

Document project in exhibition format.
Technical details as artwork specs.
README as catalog entry.

Not tutorial. Catalog.
Not guide. Archive record.

## When to Use

Invoke this skill when:
- User wants formal project documentation
- Creating portfolio entry
- Archiving completed project
- Writing project summary
- Presenting work formally

Do NOT use for:
- Step-by-step guides
- API documentation
- User manuals

This skill catalogs. Doesn't instruct.

## Output Format

### Structure

```
---

# [Project Name]

**[Creator/Organization]**
[Year]

---

## Medium

[Technology stack as artistic medium]

## Dimensions

[Size metrics: lines, files, dependencies]

## Description

[One paragraph about what the work does/is]

## Provenance

[Origin, inspiration, context]

## Technical Notes

[Key implementation details]

## Exhibition History

[Where deployed, versions, releases]

## Collection

[Repository, organization]

---

Catalog entry #[number]
[Archive name]
```

### Section Guidelines

**Medium**: List technologies like art materials
- "JavaScript on Node.js canvas"
- "Python with TensorFlow pigments"
- "React and TypeScript on Vercel surface"

**Dimensions**: Quantify the work
- Lines of code
- Number of files
- Dependencies count
- Bundle size

**Description**: One paragraph, factual
- What it does
- Not how it works
- Not why it matters

**Provenance**: Origin story
- When started
- What inspired it
- Who commissioned (if any)

## Examples

### Web Application

```
---

# TaskFlow

**Acme Industries**
2024

---

## Medium

TypeScript and React on Next.js canvas
PostgreSQL with Prisma medium
Tailwind CSS surface treatment

## Dimensions

12,847 lines of code
143 files
47 dependencies
2.3 MB bundle

## Description

A task management application that organizes work into flows. Users create tasks, assign them to flows, and track completion. Features real-time updates and team collaboration.

## Provenance

Commissioned Q1 2024. Inspired by Kanban methodology. Built to replace spreadsheet-based tracking at Acme Industries.

## Technical Notes

Server-side rendering for initial load. WebSocket connections for live updates. Row-level security in database.

## Exhibition History

v1.0 - March 2024, Internal release
v1.1 - April 2024, Added team features
v2.0 - July 2024, Public beta

## Collection

github.com/acme/taskflow
Acme Industries Engineering Collection

---

Catalog entry #0047
Acme Digital Archive
```

### CLI Tool

```
---

# filecount

**sdpkjc**
2024

---

## Medium

Python on command line canvas
Click framework for interface
Pure standard library palette

## Dimensions

234 lines of code
3 files
2 dependencies
Single file distributable

## Description

A command-line tool that counts files in directories. Outputs totals by extension. Supports recursive scanning and exclusion patterns.

## Provenance

Created November 2024. Born from need to audit large codebases. No external commission.

## Technical Notes

Streams directory entries. Memory-efficient for large trees. POSIX-compliant output format.

## Exhibition History

v1.0 - November 2024, Initial release
Published to PyPI

## Collection

github.com/sdpkjc/filecount
Personal Tools Collection

---

Catalog entry #0012
sdpkjc Archive
```

## Philosophy

Museums catalog everything.
Even the mundane becomes documented.
Every piece gets an entry.

Projects are works.
Code is medium.
This skill makes the record.

Future archaeologists will thank us.

---

**Generate the catalog entry now.**

Artist. Title. Medium. Year.
The work documented.
The record complete.
