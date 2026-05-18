/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 15,
  /** Term display string */
  term: 'Term 2',
  /** Main topic title for the large card */
  topicTitle: 'Animals in Time: Biological Rhythms',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91603 • Lesson 1: introduction to biological rhythms in animals',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-3-colour)',
  /** Description paragraph for the large card */
  description:
    'Back to plant and animal responses. This week we look at how animals ' +
    'time their lives — daily, tidal, monthly and yearly. Lesson 1 lays the ' +
    'foundation: the four rhythm classes, the four words examiners want ' +
    '(endogenous, exogenous, zeitgeber, entrainment), the mammalian ' +
    'eye → SCN → pineal → melatonin pathway, and the three activity ' +
    'patterns (diurnal, nocturnal, crepuscular). Two embedded videos, an ' +
    'interactive check-yourself, and the Scipad pages to do tonight. ' +
    'Lessons 2 to 4 (actograms, NZ case studies, Excellence writing) will ' +
    'be set later in the week.',
  /** Standard badge info */
  standardCode: 'AS 91603',
  credits: 5,
  type: 'External' as const,
};
