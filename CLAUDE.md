# Biology Level 3

## Non-Negotiable Stop Rule

If Eliot says `stop`, stop completely.

- Reply with exactly `Stopped.`
- Do not run tools.
- Do not continue queued work, resume hooks, journal, summarise, hand over, or explain.
- Wait for explicit reauthorisation before doing anything else.

Do not use bypass-permissions mode for multi-step, file-affecting, tool-using, journalling, memory, or long-running work. Use ask/permission mode so Eliot has a real interruption point.


## Project Context — REQUIRED READING

This project is **Biology Level 3** — NCEA Level 3 Biology course platform (Astro 5, dark-first theme), deployed to Vercel and GitHub Pages.

Before doing ANY work in this project, read these auto-memory files for current state:

1. `~/.claude/projects/-Users-eliotattridge/memory/MEMORY.md` — index of all memory files; contains the Biology Level 3 entry with current build status, deploy targets, theme toggle pattern, and Choice Chamber notes
2. `~/.claude/projects/-Users-eliotattridge/memory/choice-chamber-rewrite.md` — Choice Chamber simulator rewrite context (if relevant to your task)
3. `~/.claude/projects/-Users-eliotattridge/memory/bio-navigation-session.md` — navigation session notes (if relevant to your task)

**Why:** Project state lives in memory files, NOT in code or git history. Multiple parallel Claude sessions exist. Skipping the memory read causes Claude to suggest work that's already done, ignore deployments, or get key facts wrong. Memory wins over code for current state.

**How to apply:** Read these files as the FIRST tool calls of any conversation about this project, before any Glob/Grep/Bash exploration.

NCEA Level 3 Biology course platform for Year 13 students. Built with Astro. Deployed to GitHub Pages at `https://deltacephei.github.io/biology-level3/`.

**Status:** In Development (Phase 0/1)

## Tech Stack

- **Framework:** Astro (static-first, island architecture)
- **Styling:** Custom CSS with design tokens (dark mode default)
- **3D:** React Three Fiber (planned — loaded as Astro islands)
- **Audio:** ElevenLabs TTS (build-time generation via `generate_audio.py`)
- **Deployment:** GitHub Pages via GitHub Actions

## Project Structure

```
src/
  layouts/BaseLayout.astro    # Dark theme, fonts, global styles
  pages/
    index.astro               # Landing/dashboard page
    week/[N].astro            # Weekly content pages (week/1, week/2, etc.)
    flashcards.astro          # Flashcard practice
    quiz.astro                # Quiz practice
    braindump.astro           # Brain dump tool
    progress.astro            # Progress dashboard
    standards/                # Per-standard pages
    experiments/              # Interactive experiment pages
  components/
    WeekCard.astro            # Bento grid week card
public/
  audio/                      # Generated TTS audio files
```

## NCEA Standards Covered

| Standard | Title | Credits | Type |
|----------|-------|---------|------|
| AS 91601 | Practical investigation in a biological context | 4 | Internal |
| AS 91602 | Informed response to a socio-scientific issue | 3 | Internal |
| AS 91603 | Responses of plants and animals to external environment | 5 | External |
| AS 91604 | How an animal maintains stable internal environment | 3 | Internal |
| AS 91605 | Evolutionary processes leading to speciation | 4 | External |
| AS 91606 | Trends in human evolution | 4 | External |
| AS 91607 | Human manipulations of genetic transfer and its biological implications | 3 | Internal |

## Design Direction

- Dark mode default (deep navy/charcoal + bioluminescent accents)
- Bento grid layouts, organic shapes, bold typography (Space Grotesk + Inter)
- Scroll-driven animations, View Transitions API
- No emoji icons — SVG biological illustrations
- No mobile optimisation (phones banned at school, laptops only)

## Commands

```
npm run dev      # Dev server at localhost:4321
npm run build    # Production build to ./dist/
npm run preview  # Preview production build
```

## Content Approach

- Weekly content structured around the school year
- NotebookLM used at build time for source material (not runtime)
- Content reviewed by Eliot before committing
- Retrieval practice tools (flashcards, quizzes, brain dump) ported from psychology project approach
- Progress tracking via localStorage (Firebase Auth deferred to phase 3)

## Full Plan

See `biology-course-platform-plan.md` for the complete project plan including build phases, design vision, learning science foundation, and key decisions.


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
