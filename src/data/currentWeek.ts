/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 6,
  /** Term display string */
  term: 'Term 1',
  /** Main topic title for the large card */
  topicTitle: 'Physiological Triggers of Migration',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91603 — How Animals "Know" When to Migrate',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-3-colour)',
  /** Description paragraph for the large card */
  description:
    'How do animals "know" when to migrate? Explore the cascade from photoperiod ' +
    'detection through the hypothalamus and hormonal triggers to Zugunruhe — ' +
    'migratory restlessness. NZ case studies, interactive quiz, and graded exam ' +
    'questions with model answers.',
  /** Standard badge info */
  standardCode: 'AS 91603',
  credits: 5,
  type: 'External' as const,
};
