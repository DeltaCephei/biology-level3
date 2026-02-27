/**
 * NCEA Level 3 Biology Standards — shared data
 *
 * Single source of truth for standard metadata. Imported by index.astro,
 * standards/index.astro, and standards/[code].astro.
 */

export interface StandardWeek {
  num: number;
  title: string;
  hasContent?: boolean;
}

export interface Standard {
  code: string;
  title: string;
  fullTitle: string;
  credits: number;
  type: 'Internal' | 'External';
  colour: string;
  weeks: StandardWeek[];
}

export const standards: Standard[] = [
  {
    code: '91601',
    title: 'Practical Investigation',
    fullTitle: 'Carry out a practical investigation in a biological context, with guidance',
    credits: 4,
    type: 'Internal',
    colour: 'var(--standard-1-colour)',
    weeks: [],
  },
  {
    code: '91602',
    title: 'Socio-Scientific Issue',
    fullTitle: 'Integrate biological knowledge to develop an informed response to a socio-scientific issue',
    credits: 3,
    type: 'Internal',
    colour: 'var(--standard-2-colour)',
    weeks: [],
  },
  {
    code: '91603',
    title: 'Animal & Plant Responses',
    fullTitle: 'Demonstrate understanding of the responses of plants and animals to their external environment',
    credits: 5,
    type: 'External',
    colour: 'var(--standard-3-colour)',
    weeks: [
      { num: 2, title: 'Introduction to the Course & Structure', hasContent: false },
      { num: 3, title: 'Simple Animal Responses', hasContent: true },
    ],
  },
  {
    code: '91604',
    title: 'Homeostasis',
    fullTitle: 'Demonstrate understanding of how an animal maintains a stable internal environment',
    credits: 3,
    type: 'External',
    colour: 'var(--standard-4-colour)',
    weeks: [],
  },
  {
    code: '91605',
    title: 'Evolution & Speciation',
    fullTitle: 'Demonstrate understanding of evolutionary processes leading to speciation',
    credits: 4,
    type: 'External',
    colour: 'var(--standard-5-colour)',
    weeks: [],
  },
];

/** Lookup a single standard by its code (e.g. '91603') */
export function getStandard(code: string): Standard | undefined {
  return standards.find((s) => s.code === code);
}
