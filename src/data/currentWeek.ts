/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 11,
  /** Term display string */
  term: 'Term 1',
  /** Main topic title for the large card */
  topicTitle: 'Your Internal — Writing Time',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91604 — "Keeping it Steady" • due Fri 8 May, 23:59',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-4-colour)',
  /** Description paragraph for the large card */
  description:
    'The AS 91604 internal is live. Lesson 1: introduction to the standard, ' +
    'the four-part report, the AI Use policy, and where support lives. ' +
    'Lessons 2 & 3 (double): textbook site access via a personal email, ' +
    'dry-run feedback, Milestone 1 sign-off, then supervised writing time ' +
    'on Parts A and B. Due Friday 8 May, 23:59 via Teams.',
  /** Standard badge info */
  standardCode: 'AS 91604',
  credits: 3,
  type: 'Internal' as const,
};
