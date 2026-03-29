/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 10,
  /** Term display string */
  term: 'Term 1',
  /** Main topic title for the large card */
  topicTitle: 'Homeostatic Systems Survey',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91604 — Osmoregulation, Blood Calcium & Blood pH',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-4-colour)',
  /** Description paragraph for the large card */
  description:
    'Four more homeostatic systems to broaden your understanding before ' +
    'choosing your internal topic. Lesson 1: Osmoregulation. Lesson 2: Blood ' +
    'calcium regulation. Lesson 3: Blood pH regulation. Lesson 4: Oxygen ' +
    'homeostasis and iron regulation — the EPO feedback loop and the ' +
    'hepcidin–ferroportin axis.',
  /** Standard badge info */
  standardCode: 'AS 91604',
  credits: 3,
  type: 'Internal' as const,
};
