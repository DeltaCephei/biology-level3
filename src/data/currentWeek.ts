/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 9,
  /** Term display string */
  term: 'Term 1',
  /** Main topic title for the large card */
  topicTitle: 'Dry Run Submission & Our Planet',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91604 — Glucose Homeostasis Dry Run + AS 91603 — Animal Behaviours',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-4-colour)',
  /** Description paragraph for the large card */
  description:
    'Lessons 1–2: Complete and submit your glucose homeostasis dry run ' +
    '(deadline 23:59, 25 March). Checklist, Merit/Excellence tips, and links ' +
    'to Weeks 7–8 for reference. Lesson 3: Watch Our Planet S1E3 and identify ' +
    'animal behaviours — innate, learned, taxis, kinesis, and more.',
  /** Standard badge info */
  standardCode: 'AS 91604',
  credits: 3,
  type: 'Internal' as const,
};
