---
name: contact-sheet
description: This skill should be used when user asks for project overview, file summary, "what's in this folder", "show me the structure", or needs quick visual of codebase contents. Generates contact-sheet style overview like film photography contact sheets. Thumbnails of everything. Quick reference.
---

# Contact Sheet

Overview of everything. Thumbnail view.

Like photographer's contact sheet.
All frames visible.
Quick scan. Pick what matters.

## Purpose

Generate project overview.
File by file.
Function by function.
Quick reference sheet.

Not deep analysis. Surface scan.
Not explanation. Enumeration.

## When to Use

Invoke this skill when:
- User asks "what's in here?"
- User asks "show me the structure"
- User wants project overview
- Starting work on unfamiliar codebase
- Need quick inventory of files
- Reviewing folder contents

Do NOT use for:
- Deep code analysis
- Debugging specific issues
- Understanding single file in detail

This skill surveys. Doesn't study.

## Output Format

### Structure

```
# Contact Sheet: [Project/Folder Name]

Exposed: [timestamp]
Frames: [count]

---

## Frame 01: [filename]
[one-line description]
`[key identifier or signature]`

## Frame 02: [filename]
[one-line description]
`[key identifier or signature]`

## Frame 03: [filename]
[one-line description]
`[key identifier or signature]`

...

---

End of roll.
```

### Frame Content

For each file, capture:
- **Filename**: The subject
- **One-line description**: What it is (not what it does)
- **Key identifier**: Main export, class name, or signature

### Style Rules

1. **One line per file**: Maximum brevity
2. **No explanations**: Just identification
3. **Technical terms**: Use actual code terms
4. **Sequential numbering**: Frame 01, 02, 03...
5. **No judgment**: Don't rate or recommend

## Examples

### Code Project

```
# Contact Sheet: /src/components

Exposed: 2024-01-15 14:30
Frames: 5

---

## Frame 01: Button.tsx
React button component
`export const Button`

## Frame 02: Modal.tsx
Dialog overlay component
`export const Modal`

## Frame 03: Input.tsx
Form input wrapper
`export const Input`

## Frame 04: Card.tsx
Content container component
`export const Card`

## Frame 05: index.ts
Barrel export file
`export * from`

---

End of roll.
```

### Mixed Folder

```
# Contact Sheet: /project-root

Exposed: 2024-01-15 14:30
Frames: 7

---

## Frame 01: package.json
Node project manifest
`"name": "project"`

## Frame 02: README.md
Project documentation
`# Project Name`

## Frame 03: .gitignore
Git exclusion rules
`node_modules/`

## Frame 04: tsconfig.json
TypeScript configuration
`"compilerOptions"`

## Frame 05: src/
Source directory
`[directory]`

## Frame 06: tests/
Test directory
`[directory]`

## Frame 07: .env.example
Environment template
`API_KEY=`

---

End of roll.
```

## Philosophy

Contact sheets show everything at once.
No hierarchy. No importance.
Just: what exists.

Photographer scans quickly.
Circles the good ones.
Moves on.

This skill provides the sheet.
User does the circling.

---

**Generate the contact sheet now.**

Quick scan.
All frames.
What's on this roll.
