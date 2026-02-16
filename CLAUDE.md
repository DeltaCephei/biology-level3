# Biology Level 3

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
| AS 91604 | How an animal maintains stable internal environment | 3 | External |
| AS 91605 | Evolutionary processes leading to speciation | 4 | External |

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
