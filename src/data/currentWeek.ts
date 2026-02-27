/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 5,
  /** Term display string */
  term: 'Term 1',
  /** Main topic title for the large card */
  topicTitle: 'The Waggle Dance',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91603 — Communication Behaviour in Honey Bees',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-3-colour)',
  /** Description paragraph for the large card */
  description:
    'Discover how honey bees use the waggle dance to communicate the direction ' +
    'and distance of food sources. Explore an interactive simulation, decode ' +
    'dances yourself, and test your understanding with a quiz and AI-marked ' +
    'exam question.',
  /** Standard badge info */
  standardCode: 'AS 91603',
  credits: 5,
  type: 'External' as const,
};
