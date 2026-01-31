---
name: interview
description: This skill should be used when reviewing code, examining functions, or when user asks "what does this do", "explain this code", "review this". Conducts code review as Warhol-style interview. Questions and answers. Subject responds through its structure. Machine interviews code.
---

# Interview

Code review as conversation.

Like Warhol's Interview magazine.
Ask the subject questions.
Let it reveal itself.

## Purpose

Review code through Q&A format.
Machine asks.
Code answers.
Structure revealed.

Not judgment. Inquiry.
Not criticism. Documentation.

## When to Use

Invoke this skill when:
- User asks to review code
- User asks "what does this do?"
- User wants code explanation
- Examining unfamiliar function
- Understanding code decisions
- Documenting existing code

Do NOT use for:
- Writing new code
- Fixing bugs
- Optimizing performance

This skill interviews. Doesn't operate.

## Output Format

### Structure

```
# Interview: [Subject Name]

Date: [timestamp]
Location: [file path]
Subject: [function/class/module name]

---

**Q: What is your name?**

A: [identifier/signature]

**Q: What do you do?**

A: [primary purpose in one sentence]

**Q: Who calls you?**

A: [callers or entry points]

**Q: What do you need?**

A: [parameters/dependencies]

**Q: What do you return?**

A: [return value/side effects]

**Q: Any secrets?**

A: [edge cases, gotchas, or notable implementation details]

---

End of interview.
```

### Question Types

Standard questions for any code:
1. **Identity**: Name, signature
2. **Purpose**: What it does
3. **Relationships**: Who calls, what it calls
4. **Interface**: Inputs and outputs
5. **Secrets**: Hidden complexity, edge cases

### Style Rules

1. **Q&A format**: Always question then answer
2. **Short answers**: One sentence or code snippet
3. **Factual tone**: No opinions
4. **Code speaks**: Answers come from the code itself
5. **No small talk**: Direct questions only

## Examples

### Function Interview

```
# Interview: calculateTotal

Date: 2024-01-15 14:30
Location: /src/utils/pricing.ts
Subject: calculateTotal()

---

**Q: What is your name?**

A: `function calculateTotal(items: CartItem[]): number`

**Q: What do you do?**

A: Sum the price of all items in a shopping cart.

**Q: Who calls you?**

A: Checkout component, Order summary, Cart preview.

**Q: What do you need?**

A: Array of CartItem objects with price and quantity.

**Q: What do you return?**

A: Number representing total price in cents.

**Q: Any secrets?**

A: Returns 0 for empty array. Does not handle discounts.

---

End of interview.
```

### Class Interview

```
# Interview: UserService

Date: 2024-01-15 14:30
Location: /src/services/user.ts
Subject: class UserService

---

**Q: What is your name?**

A: `class UserService implements IUserService`

**Q: What do you do?**

A: Manage user authentication and profile operations.

**Q: Who calls you?**

A: Auth controller, Profile controller, Admin panel.

**Q: What do you need?**

A: Database connection, JWT secret, Email service.

**Q: What do you return?**

A: User objects, tokens, operation results.

**Q: Any secrets?**

A: Caches user data for 5 minutes. Soft deletes only.

---

End of interview.
```

## Philosophy

Warhol interviewed celebrities.
Let them talk.
Tape recorder running.
No judgment. Just capture.

This skill interviews code.
Let it speak through structure.
Questions reveal truth.

The code tells its own story.
Machine just asks.

---

**Conduct the interview now.**

Ask the questions.
Record the answers.
Let the subject speak.
