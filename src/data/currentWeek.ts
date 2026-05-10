/**
 * Current Week Configuration
 *
 * Update this file each week to change what appears in the
 * "This Week" section on the homepage. Single place to edit.
 */

export const currentWeek = {
  /** Week number (matches /week/:num route) */
  number: 13,
  /** Term display string */
  term: 'Term 2',
  /** Main topic title for the large card */
  topicTitle: 'Why Paper Beats Browser',
  /** Standard code + description for the subtitle */
  topicSubtitle: 'AS 91603 prep • Lesson 1: paper retrieval practice on Wks 3–6',
  /** Standard accent colour variable */
  accentColour: 'var(--standard-3-colour)',
  /** Description paragraph for the large card */
  description:
    'Laptops shut, paper out. Four free-recall prompts on the pre-homeostasis ' +
    'topics from Weeks 3 to 6, five to seven minutes each, closed-book. The ' +
    'point is for you to feel why closed-book paper recall is the most ' +
    'efficient revision tool you have. The page explains the science: ' +
    'generation effect, desirable difficulties, and the honest version of ' +
    'the paper-vs-browser argument. Lessons 2 to 4 will be set later in the week.',
  /** Standard badge info */
  standardCode: 'AS 91603',
  credits: 5,
  type: 'External' as const,
};
